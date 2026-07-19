import re
import os
from pathlib import Path
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro, SAMPLE_RATE

# Configuration
MANUSCRIPT_DIR = Path("books/book-01/manuscript")
OUTPUT_DIR = Path("books/book-01/audiobook_tmp")
MODEL_PATH = Path("models/kokoro-v1.0.onnx")
VOICES_PATH = Path("models/voices-v1.0.bin")
VOICE = "af_sky"
LANG = "en-us"
SPEED = 1.2
PAUSE_BETWEEN_PARAGRAPHS = 0.5 # seconds
PAUSE_AT_END = 2.0 # seconds

def strip_markdown(text: str) -> str:
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("---"):
            continue
        if stripped.startswith("#"):
            stripped = stripped.lstrip("# ")
            # Optional: remove dashes like 'Chapter 1 — ' for better reading
            stripped = stripped.replace(" — ", " ")
            stripped = stripped.replace(" - ", " ")
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

def get_chapter_files():
    files = []
    prologue = MANUSCRIPT_DIR / "prologue.md"
    if prologue.exists():
        files.append(prologue)
    
    chapters_dir = MANUSCRIPT_DIR / "chapters"
    if chapters_dir.exists():
        # Get all chapter-*.md files, sorted properly
        chapter_files = sorted(chapters_dir.glob("chapter-*.md"))
        files.extend(chapter_files)
    
    return files

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print("Loading Kokoro model...")
    kokoro = Kokoro(model_path=str(MODEL_PATH), voices_path=str(VOICES_PATH))
    
    files = get_chapter_files()
    print(f"Found {len(files)} files to process.")
    
    pause_samples_paragraph = np.zeros(int(SAMPLE_RATE * PAUSE_BETWEEN_PARAGRAPHS), dtype=np.float32)
    pause_samples_end = np.zeros(int(SAMPLE_RATE * PAUSE_AT_END), dtype=np.float32)

    for file_idx, filepath in enumerate(files):
        print(f"Processing {filepath.name} ({file_idx + 1}/{len(files)})...")
        output_file = OUTPUT_DIR / f"{filepath.stem}.wav"
        
        # Skip if already exists (resume capability)
        if output_file.exists():
            print(f"  Already exists, skipping...")
            continue
            
        text = filepath.read_text(encoding="utf-8")
        text = strip_markdown(text)
        chunks = split_into_chunks(text)
        
        audio_segments = []
        for i, chunk in enumerate(chunks):
            # Print minimal progress
            print(f"  Synthesizing chunk {i + 1}/{len(chunks)} ({len(chunk)} chars)...")
            try:
                samples, _ = kokoro.create(
                    chunk,
                    voice=VOICE,
                    speed=SPEED,
                    lang=LANG,
                    is_phonemes=False,
                    trim=True,
                )
                audio_segments.append(samples)
                # Add pause between chunks (paragraphs)
                if i < len(chunks) - 1:
                    audio_segments.append(pause_samples_paragraph)
            except Exception as e:
                print(f"  Error synthesizing chunk {i + 1}: {e}")
                continue
        
        if audio_segments:
            # Add pause at end of chapter
            audio_segments.append(pause_samples_end)
            full_audio = np.concatenate(audio_segments)
            sf.write(str(output_file), full_audio, samplerate=SAMPLE_RATE)
            print(f"  Saved {output_file}")
        else:
            print(f"  No audio generated for {filepath.name}")

if __name__ == "__main__":
    main()
