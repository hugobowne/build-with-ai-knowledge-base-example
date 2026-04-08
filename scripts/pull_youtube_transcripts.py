"""Pull transcripts from YouTube videos and save as markdown files.

Usage: uv run python scripts/pull_youtube_transcripts.py <video_ids_file>
"""

import sys
import time
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi

# Delay between requests to avoid IP blocking
REQUEST_DELAY_SECONDS = 5


def format_timestamp(seconds):
    """Convert seconds to HH:MM:SS format."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def pull_transcript(video_id, output_dir):
    """Pull transcript for a single video and save as markdown."""
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=["en"])

        # Build markdown with timestamps
        lines = []
        for snippet in transcript.snippets:
            ts = format_timestamp(snippet.start)
            text = snippet.text.strip()
            if text:
                lines.append(f"[{ts}] {text}")

        content = "\n".join(lines)
        output_path = output_dir / f"{video_id}.md"
        output_path.write_text(content)

        # Get duration from last snippet
        last_ts = format_timestamp(transcript.snippets[-1].start)
        print(f"OK {video_id} ({last_ts}) -> {output_path.name}")
        return True

    except Exception as e:
        if "IpBlocked" in type(e).__name__:
            print(f"BLOCKED {video_id} — IP blocked, stopping.")
            return None  # Signal to stop
        print(f"FAIL {video_id}: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run python scripts/pull_youtube_transcripts.py <video_ids_file>")
        sys.exit(1)

    ids_file = Path(sys.argv[1])
    video_ids = [line.strip() for line in ids_file.read_text().splitlines() if line.strip()]

    output_dir = Path(__file__).parent.parent / "raw" / "youtube"
    output_dir.mkdir(exist_ok=True)

    # Skip videos we already have
    existing = set(f.stem for f in output_dir.glob("*.md"))
    to_pull = [vid for vid in video_ids if vid not in existing]

    print(f"Total videos: {len(video_ids)}")
    print(f"Already have: {len(existing)}")
    print(f"To pull: {len(to_pull)}")
    print()

    success = 0
    fail = 0
    for i, vid in enumerate(to_pull):
        result = pull_transcript(vid, output_dir)
        if result is True:
            success += 1
        elif result is None:
            # IP blocked — stop immediately
            break
        else:
            fail += 1
        # Delay between requests to avoid rate limiting
        if i < len(to_pull) - 1:
            time.sleep(REQUEST_DELAY_SECONDS)

    print(f"\nDone. {success} pulled, {fail} failed, {len(existing)} skipped.")


if __name__ == "__main__":
    main()
