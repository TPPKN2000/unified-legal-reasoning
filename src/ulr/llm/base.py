from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class LLMBackend(ABC):
    name: str = "llm"

    @abstractmethod
    def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        max_new_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
    ) -> str: ...

    def close(self) -> None:  # free GPU memory etc.
        pass
