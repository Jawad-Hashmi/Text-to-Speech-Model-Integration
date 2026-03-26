from __future__ import annotations


def normalize_text(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def split_text_into_chunks(text: str, max_chars: int = 3800) -> list[str]:
    """
    Split text into chunks below the API limit.
    We stay under 4096 chars for safety.
    """
    text = normalize_text(text)
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    chunks: list[str] = []
    current = ""

    for paragraph in paragraphs:
        candidate = paragraph if not current else f"{current}\n\n{paragraph}"

        if len(candidate) <= max_chars:
            current = candidate
            continue

        if current:
            chunks.append(current)

        if len(paragraph) <= max_chars:
            current = paragraph
            continue

        # Fallback: split oversized paragraph by sentences/lines
        lines = [line.strip() for line in paragraph.split("\n") if line.strip()]
        temp = ""

        for line in lines:
            candidate_line = line if not temp else f"{temp}\n{line}"

            if len(candidate_line) <= max_chars:
                temp = candidate_line
            else:
                if temp:
                    chunks.append(temp)
                temp = line

        if temp:
            current = temp
        else:
            current = ""

    if current:
        chunks.append(current)

    return chunks