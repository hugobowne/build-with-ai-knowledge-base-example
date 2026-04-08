"""Convert VTT subtitle files to clean markdown.

Strips cue numbers and timestamps, merges consecutive same-speaker lines
into paragraphs, preserves speaker labels, and inserts periodic timestamp
markers.
"""

import sys
from pathlib import Path

import webvtt


def clean_vtt(vtt_path: Path) -> str:
    captions = webvtt.read(str(vtt_path))

    paragraphs = []
    current_speaker = None
    current_lines = []
    last_marker_minutes = -5  # force first marker

    for caption in captions:
        text = caption.text.strip()
        if not text:
            continue

        # Parse timestamp for periodic markers
        start_seconds = _timestamp_to_seconds(caption.start)
        current_minutes = int(start_seconds // 60)

        # Check if this line has a speaker label
        if ":" in text and not text.startswith("["):
            parts = text.split(":", 1)
            speaker = parts[0].strip()
            content = parts[1].strip()
        else:
            speaker = current_speaker
            content = text

        # Insert timestamp marker every ~5 minutes
        if current_minutes - last_marker_minutes >= 5:
            marker = f"[~{current_minutes:02d}:00]"
            if current_speaker is not None and current_lines:
                # Flush current paragraph before marker
                paragraphs.append(
                    f"**{current_speaker}:** {' '.join(current_lines)}"
                )
                current_lines = []
            paragraphs.append(f"\n{marker}\n")
            last_marker_minutes = current_minutes

        if speaker != current_speaker:
            # New speaker — flush previous paragraph
            if current_speaker is not None and current_lines:
                paragraphs.append(
                    f"**{current_speaker}:** {' '.join(current_lines)}"
                )
            current_speaker = speaker
            current_lines = [content] if content else []
        else:
            if content:
                current_lines.append(content)

    # Flush last paragraph
    if current_speaker is not None and current_lines:
        paragraphs.append(f"**{current_speaker}:** {' '.join(current_lines)}")

    return "\n\n".join(paragraphs) + "\n"


def _timestamp_to_seconds(ts: str) -> float:
    parts = ts.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = float(parts[2])
    return hours * 3600 + minutes * 60 + seconds


def main():
    raw_dir = Path(__file__).parent.parent / "raw"
    out_dir = raw_dir / "_cleaned"
    out_dir.mkdir(exist_ok=True)

    vtt_files = sorted(raw_dir.glob("*.vtt"))
    if not vtt_files:
        print("No .vtt files found in raw/")
        sys.exit(1)

    for vtt_path in vtt_files:
        print(f"Cleaning {vtt_path.name}...")
        cleaned = clean_vtt(vtt_path)
        out_path = out_dir / vtt_path.with_suffix(".md").name
        out_path.write_text(cleaned)
        print(f"  → {out_path.relative_to(raw_dir.parent)}")

    print(f"\nDone. Cleaned {len(vtt_files)} files into {out_dir.relative_to(raw_dir.parent)}/")


if __name__ == "__main__":
    main()
