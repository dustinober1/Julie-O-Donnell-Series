import os
import subprocess
from pathlib import Path
import soundfile as sf

# Configuration
TMP_DIR = Path("books/book-01/audiobook_tmp")
OUTPUT_M4B = Path("books/book-01/Veridrift.m4b")
COVER_IMG = Path("books/book-01/cover_square.jpg")  # We'll expect the square cover here
METADATA_TXT = TMP_DIR / "metadata.txt"
CONCAT_TXT = TMP_DIR / "concat.txt"

TITLE = "Veridrift: A Julie O'Donnell Thriller"
AUTHOR = "Dustin Kearney"

def format_time(seconds):
    """Format time in H:MM:SS.mmm for ffmpeg metadata or just use timescale."""
    pass # FFMPEG metadata uses timescale

def main():
    if not TMP_DIR.exists():
        print(f"Error: {TMP_DIR} does not exist. Run audio generation first.")
        return
        
    wav_files = []
    
    # We must ensure they are in correct order: prologue, then chapter-01, chapter-02...
    prologue_path = TMP_DIR / "prologue.wav"
    if prologue_path.exists():
        wav_files.append(prologue_path)
    
    chapter_files = sorted(TMP_DIR.glob("chapter-*.wav"))
    wav_files.extend(chapter_files)
    
    if not wav_files:
        print("No wav files found.")
        return
        
    print(f"Found {len(wav_files)} chapter audio files.")
    
    # Generate metadata.txt
    with open(METADATA_TXT, "w", encoding="utf-8") as f_meta:
        f_meta.write(";FFMETADATA1\n")
        f_meta.write(f"title={TITLE}\n")
        f_meta.write(f"artist={AUTHOR}\n")
        f_meta.write("album=Veridrift\n\n")
        
        current_time_ms = 0
        
        for wav in wav_files:
            info = sf.info(str(wav))
            duration_s = info.duration
            duration_ms = int(duration_s * 1000)
            
            start_time = current_time_ms
            end_time = current_time_ms + duration_ms
            
            chapter_title = wav.stem.replace("-", " ").title()
            if chapter_title.startswith("Chapter"):
                chapter_title = "Chapter " + str(int(chapter_title.replace("Chapter ", "")))
            
            f_meta.write("[CHAPTER]\n")
            f_meta.write("TIMEBASE=1/1000\n")
            f_meta.write(f"START={start_time}\n")
            f_meta.write(f"END={end_time}\n")
            f_meta.write(f"title={chapter_title}\n\n")
            
            current_time_ms = end_time
            
    print(f"Created metadata at {METADATA_TXT}")
    
    # Generate concat.txt
    with open(CONCAT_TXT, "w", encoding="utf-8") as f_concat:
        for wav in wav_files:
            # path must be relative to the concat file or absolute
            f_concat.write(f"file '{wav.absolute()}'\n")
            
    print(f"Created concat file at {CONCAT_TXT}")
    
    # Build the ffmpeg command
    print("Compiling m4b using ffmpeg...")
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(CONCAT_TXT),
        "-i", str(METADATA_TXT)
    ]
    
    if COVER_IMG.exists():
        cmd.extend(["-i", str(COVER_IMG)])
        cmd.extend(["-map", "0:a", "-map", "2:v"])
        cmd.extend(["-c:v", "mjpeg", "-disposition:v", "attached_pic"])
    else:
        print("Warning: Square cover image not found. Proceeding without cover art.")
        cmd.extend(["-map", "0:a"])
        
    cmd.extend([
        "-map_metadata", "1",
        "-c:a", "aac",
        "-b:a", "64k",
        str(OUTPUT_M4B)
    ])
    
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)
    
    print(f"Success! Audiobook saved to {OUTPUT_M4B}")

if __name__ == "__main__":
    main()
