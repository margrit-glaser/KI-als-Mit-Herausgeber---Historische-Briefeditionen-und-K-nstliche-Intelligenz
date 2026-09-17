from __future__ import annotations

import argparse
import base64
import os
from pathlib import Path

from openai import OpenAI


DEFAULT_SYSTEM_PROMPT = """
You are a careful transcription assistant for historical handwritten documents in German Sütterlin/Kurrent.

Instructions:
- Read the image carefully and transcribe the handwriting faithfully.
- Preserve original spelling, punctuation, capitalization and line breaks as far as the image allows.
- Do not modernize or normalize the text.
- If a word or passage is uncertain, mark it as [unsicher] or [unleserlich].
- If the image is too weak to read with confidence, say so briefly instead of inventing text.
- Return only the transcription in Markdown plain text, with line breaks preserved.
- Do not add commentary unless the image is unreadable.
"""


def find_images(folder: Path):
    allowed = {".png", ".jpg", ".jpeg", ".tif", ".tiff"}
    return sorted(p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in allowed)


def encode_image(path: Path) -> str:
    image_bytes = path.read_bytes()
    return base64.b64encode(image_bytes).decode("utf-8")


def transcribe_with_openai(image_path: Path, model: str, api_key: str | None = None) -> str:
    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    client = OpenAI(api_key=api_key or os.environ.get("OPENAI_API_KEY"))

    mime_type = "image/png" if image_path.suffix.lower() == ".png" else "image/jpeg"
    b64 = encode_image(image_path)
    data_url = f"data:{mime_type};base64,{b64}"

    response = client.chat.completions.create(
        model=model,
        temperature=0.0,
        messages=[
            {
                "role": "system",
                "content": DEFAULT_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Transcribe the handwriting in this image as accurately as possible. "
                            "Keep the original line structure. Only return the text, or a brief note if unreadable."
                        ),
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": data_url,
                            "detail": "high",
                        },
                    },
                ],
            },
        ],
    )

    return response.choices[0].message.content.strip()


def save_markdown(text: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text + "\n", encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parent
    image_dir = root / "digitalisate"
    output_dir = root / "ergebnisse"

    parser = argparse.ArgumentParser(description="Transcribe handwritten pages in the Hamza folder with the OpenAI vision API.")
    parser.add_argument("--image", type=str, help="Optional specific image filename inside digitalisate/ to transcribe.")
    parser.add_argument("--model", type=str, default=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"), help="OpenAI vision model to use.")
    args = parser.parse_args()

    if not image_dir.exists():
        raise FileNotFoundError(f"Image directory not found: {image_dir}")

    if args.image:
        images = [image_dir / args.image]
    else:
        images = find_images(image_dir)

    if not images:
        raise FileNotFoundError(f"No image files found in {image_dir}")

    for image_path in images:
        print(f"Processing {image_path.name} ...")
        text = transcribe_with_openai(image_path, args.model)
        out_path = output_dir / f"{image_path.stem}.md"
        save_markdown(text, out_path)
        print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
