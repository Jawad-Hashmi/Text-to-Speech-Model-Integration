from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    openai_api_key: str
    model: str = "gpt-4o-mini-tts"
    voice: str = "coral"
    response_format: str = "mp3"
    max_input_chars: int = 4096


def get_settings() -> Settings:
    api_key = os.getenv("OPENAI_API_KEY", "").strip()

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. Add it to your .env file."
        )

    return Settings(openai_api_key=api_key)