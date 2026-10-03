from __future__ import annotations

from typing import Any, Dict

from .base import LLMBackend


def spec_name(spec: Dict[str, Any]) -> str:
    return spec.get("name") or spec.get("model") or spec.get("type", "llm")


def build_backend(spec: Dict[str, Any]) -> LLMBackend:
    """spec example: {type: hf, model: Qwen/Qwen2.5-3B-Instruct, load_in_4bit: false, max_new_tokens: 512}"""
    t = spec.get("type", "hf")
    kw = {k: v for k, v in spec.items() if k != "type"}
    if t == "mock":
        from .mock import MockBackend

        return MockBackend(**kw)
    if t == "hf":
        from .hf_local import HFLocalBackend

        return HFLocalBackend(**kw)
    if t == "openai":
        from .api import OpenAIBackend

        return OpenAIBackend(**kw)
    if t == "anthropic":
        from .api import AnthropicBackend

        return AnthropicBackend(**kw)
    if t == "gemini":
        from .api import GeminiBackend

        return GeminiBackend(**kw)
    raise ValueError(f"Unknown backend type: {t}")
