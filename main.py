from __future__ import annotations

from datetime import datetime
from pathlib import Path

from app.config import get_settings
from app.file_utils import ensure_directory, read_text_file
from app.text_utils import split_text_into_chunks
from app.tts_service import TTSService


def create_run_directory(output_root: Path, job_name: str = "tts_job") -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = output_root / f"{job_name}_{timestamp}"
    ensure_directory(run_dir)
    return run_dir


def main() -> None:
    settings = get_settings()

    project_root = Path(__file__).resolve().parent
    input_dir = project_root / "input"
    output_root = project_root / "output"

    ensure_directory(input_dir)
    ensure_directory(output_root)

    script_file = input_dir / "script.txt"
    script_text = read_text_file(script_file)

    instructions = (
        "Speak in a calm, confident, professional promotional tone. "
        "Use slight pauses for impact. "
        "Keep the pacing smooth, clear, and premium."
    )

    chunks = split_text_into_chunks(
        script_text,
        max_chars=min(settings.max_input_chars - 200, 3800),
    )

    service = TTSService(settings)

    run_dir = create_run_directory(output_root, job_name="acadimyst")

    print(f"Loaded script from: {script_file}")
    print(f"Total chunks: {len(chunks)}")
    print(f"Saving files in: {run_dir}")

    for index, chunk in enumerate(chunks, start=1):
        output_file = run_dir / f"part_{index:02d}.{settings.response_format}"
        print(f"Generating: {output_file.name}")

        service.generate_speech_file(
            text=chunk,
            output_file=output_file,
            instructions=instructions,
        )

    print("Done. Audio parts saved successfully.")


if __name__ == "__main__":
    main()