"""Local Hugging Face backend (default for Colab T4). torch/transformers imported lazily."""
from __future__ import annotations

import gc
from typing import Optional

from .base import LLMBackend


class HFLocalBackend(LLMBackend):
    def __init__(
        self,
        model: str = "Qwen/Qwen2.5-3B-Instruct",
        dtype: str = "float16",
        load_in_4bit: bool = False,
        max_new_tokens: int = 512,
        temperature: float = 0.0,
        trust_remote_code: bool = False,
        name: Optional[str] = None,
        **_,
    ):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer

        self.name = name or model
        self.model_id = model
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.tok = AutoTokenizer.from_pretrained(model, trust_remote_code=trust_remote_code)
        kwargs = dict(device_map="auto", trust_remote_code=trust_remote_code)
        if load_in_4bit:
            from transformers import BitsAndBytesConfig

            kwargs["quantization_config"] = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_quant_type="nf4",
            )
        else:
            kwargs["torch_dtype"] = getattr(torch, dtype)
        self.model = AutoModelForCausalLM.from_pretrained(model, **kwargs)
        self.model.eval()

    def generate(self, prompt, system=None, max_new_tokens=None, temperature=None):
        import torch

        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        text = self.tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self.tok(text, return_tensors="pt").to(self.model.device)
        temp = self.temperature if temperature is None else temperature
        gen_kwargs = dict(
            max_new_tokens=max_new_tokens or self.max_new_tokens,
            pad_token_id=self.tok.pad_token_id or self.tok.eos_token_id,
        )
        if temp and temp > 0:
            gen_kwargs.update(do_sample=True, temperature=temp, top_p=0.95)
        else:
            gen_kwargs.update(do_sample=False)
        with torch.no_grad():
            out = self.model.generate(**inputs, **gen_kwargs)
        new_tokens = out[0, inputs["input_ids"].shape[1]:]
        return self.tok.decode(new_tokens, skip_special_tokens=True).strip()

    def close(self):
        import torch

        del self.model
        del self.tok
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
