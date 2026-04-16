from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled


@dataclass(frozen=True)
class Video:
    creator: str
    url: str


VIDEOS: list[Video] = [
    Video(
        creator="Lauren Meyer",
        url="https://www.youtube.com/watch?v=YnQx2rn_K3Y&start=0",
    ),
    Video(
        creator="Matt McGarry",
        url="https://www.youtube.com/watch?v=ZllqhESam1k",
    ),
    Video(
        creator="Ann Handley",
        url="https://www.youtube.com/watch?v=Y18hiSY38WI",
    ),
    Video(
        creator="Tobias Knecht",
        url="https://www.youtube.com/watch?v=g0fIUPEE0Q8",
    ),
]


def slugify_filename(name: str) -> str:
    slug = name.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "transcript"


def extract_video_id(url: str) -> str:
    # Handles typical formats:
    # - https://www.youtube.com/watch?v=VIDEO_ID
    # - https://youtu.be/VIDEO_ID
    m = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url)
    if not m:
        raise ValueError(f"Could not parse video id from URL: {url}")
    return m.group(1)


def format_transcript(lines: list[dict]) -> str:
    # Keep it readable: one caption per line, trimmed, blank lines removed.
    cleaned: list[str] = []
    for item in lines:
        text = str(item.get("text", "")).replace("\n", " ").strip()
        if text:
            cleaned.append(text)
    return "\n".join(cleaned).rstrip() + "\n"


def main() -> int:
    out_dir = Path(__file__).resolve().parent / "youtube-transcripts"
    out_dir.mkdir(parents=True, exist_ok=True)

    ytt = YouTubeTranscriptApi()

    saved = 0
    skipped = 0

    for v in VIDEOS:
        video_id = extract_video_id(v.url)
        out_path = out_dir / f"{slugify_filename(v.creator)}.txt"

        try:
            transcript = ytt.fetch(video_id, languages=("en",))
        except (TranscriptsDisabled, NoTranscriptFound) as e:
            print(f"WARNING: Skipping {v.creator} ({video_id}) - {type(e).__name__}: {e}")
            skipped += 1
            continue

        out_path.write_text(format_transcript(transcript.to_raw_data()), encoding="utf-8")
        print(f"Saved: {out_path}")
        saved += 1

    print(f"Done. Saved={saved}, Skipped={skipped}, Folder={out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
