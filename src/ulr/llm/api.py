"""Optional API backends (the paper used GPT / Claude / Gemini). SDKs imported lazily."""
from __future__ import annotations

import os
from typing import Optional

from .base import LLMBackend


class OpenAIBackend(LLMBackend):
    def __init__(self, model="gpt-4o", max_new_tokens=1024, temperature=0.0, name=None, **_):
        from openai import OpenAI

        self.client = OpenAI()
        self.model, self.max_new_tokens, self.temperature = model, max_new_tokens, temperature
        self.name = name or model

    def generate(self, prompt, system=None, max_new_tokens=None, temperature=None):
        msgs = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": prompt}]
        r = self.client.chat.completions.create(
            model=self.model,
            messages=msgs,
            max_completion_tokens=max_new_tokens or self.max_new_tokens,
            temperature=self.temperature if temperature is None else temperature,
        )
        return (r.choices[0].message.content or "").strip()


class AnthropicBackend(LLMBackend):
    def __init__(self, model="claude-sonnet-4-5", max_new_tokens=1024, temperature=0.0, name=None, **_):
        import anthropic

        self.client = anthropic.Anthropic()
        self.model, self.max_new_tokens, self.temperature = model, max_new_tokens, temperature
        self.name = name or model

    def generate(self, prompt, system=None, max_new_tokens=None, temperature=None):
        kw = {"system": system} if system else {}
        r = self.client.messages.create(
            model=self.model,
            max_tokens=max_new_tokens or self.max_new_tokens,
            temperature=self.temperature if temperature is None else temperature,
            messages=[{"role": "user", "content": prompt}],
            **kw,
        )
        return "".join(b.text for b in r.content if getattr(b, "type", "") == "text").strip()


class GeminiBackend(LLMBackend):
    def __init__(self, model="gemini-2.0-flash", max_new_tokens=1024, temperature=0.0, name=None, **_):
        from google import genai

        key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        self.client = genai.Client(api_key=key)
        self.model, self.max_new_tokens, self.temperature = model, max_new_tokens, temperature
        self.name = name or model

    def generate(self, prompt, system=None, max_new_tokens=None, temperature=None):
        from google.genai import types

        cfg = types.GenerateContentConfig(
            temperature=self.temperature if temperature is None else temperature,
            max_output_tokens=max_new_tokens or self.max_new_tokens,
            system_instruction=system,
        )
        r = self.client.models.generate_content(model=self.model, contents=prompt, config=cfg)
        return (r.text or "").strip()
