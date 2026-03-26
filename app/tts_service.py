from __future__ import annotations

from pathlib import Path

from openai import OpenAI

from app.config import Settings


class TTSService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.client = OpenAI(api_key=settings.openai_api_key)

    def generate_speech_file(
        self,
        text: str,
        output_file: Path,
        instructions: str | None = None,
    ) -> None:
        """
        Generate one audio file from one chunk of text.
        """
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with self.client.audio.speech.with_streaming_response.create(
            model=self.settings.model,
            voice=self.settings.voice,
            input=text,
            instructions=instructions,
            response_format=self.settings.response_format,
        ) as response:
            response.stream_to_file(output_file)