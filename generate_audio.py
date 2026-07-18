import re
from pathlib import Path
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro, SAMPLE_RATE

CHAPTER_PATH = Path("julie-o-donnell-book-1/books/book-01/manuscript/chapters/01-the-farm.md")
OUTPUT_PATH = Path("julie-o-donnell-book-1/books/book-01/manuscript/chapters/01-the-farm.wav")
MODEL_PATH = Path("models/kokoro-v1.0.onnx")
VOICES_PATH = Path("models/voices-v1.0.bin")
VOICE = "af_sky"
LANG = "en-us"
SPEED = 1.2


def strip_markdown(text: str) -> str:
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if stripped.startswith("---"):
            continue
        if stripped.startswith("*"):
            stripped = stripped.lstrip("* ")
        cleaned.append(stripped)
    return "\n".join(cleaned)


def split_into_chunks(text: str, max_chars: int = 800):
    paragraphs = re.split(r"\n\s*\n", text)
    chunks = []
    current = ""
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if len(current) + len(para) + 1 <= max_chars:
            current = (current + "\n\n" + para).strip()
        else:
            if current:
                chunks.append(current)
            if len(para) <= max_chars:
                current = para
            else:
                sentences = re.split(r"(?<=[.!?])\s+", para)
                current = ""
                for sentence in sentences:
                    if len(current) + len(sentence) + 1 <= max_chars:
                        current = (current + " " + sentence).strip()
                    else:
                        if current:
                            chunks.append(current)
                        current = sentence
    if current:
        chunks.append(current)
    return chunks


def main():
    text = CHAPTER_PATH.read_text(encoding="utf-8")
    text = strip_markdown(text)
    chunks = split_into_chunks(text)

    kokoro = Kokoro(model_path=str(MODEL_PATH), voices_path=str(VOICES_PATH))

    audio_segments = []
    for i, chunk in enumerate(chunks):
        print(f"Synthesizing chunk {i + 1}/{len(chunks)} ({len(chunk)} chars)...")
        samples, sample_rate = kokoro.create(
            chunk,
            voice=VOICE,
            speed=SPEED,
            lang=LANG,
            is_phonemes=False,
            trim=True,
        )
        audio_segments.append(samples)

    full_audio = np.concatenate(audio_segments)
    sf.write(str(OUTPUT_PATH), full_audio, samplerate=SAMPLE_RATE)
    print(f"Saved audio to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
