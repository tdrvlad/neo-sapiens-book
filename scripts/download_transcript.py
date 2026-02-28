"""
Download the auto-generated transcript of a YouTube video using yt-dlp
and save it as a clean text file in /scratchpads.

Usage:
    python scripts/download_transcript.py <youtube_url> [output_filename]

Example:
    python scripts/download_transcript.py https://www.youtube.com/watch?v=rmBFaNgg4wk general-computer.txt
"""

import subprocess
import sys
import os
import json
import glob
import re


def download_transcript(url: str, output_name: str) -> None:
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    scratchpads_dir = os.path.join(repo_root, "scratchpads")
    tmp_dir = os.path.join(scratchpads_dir, "_tmp_transcript")
    os.makedirs(tmp_dir, exist_ok=True)

    print(f"Downloading transcript for: {url}")

    result = subprocess.run(
        [
            "yt-dlp",
            "--write-auto-sub",
            "--sub-lang", "en",
            "--skip-download",
            "--sub-format", "json3",
            "-o", os.path.join(tmp_dir, "transcript"),
            url,
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print("yt-dlp error:", result.stderr)
        sys.exit(1)

    # Find the downloaded subtitle file
    sub_files = glob.glob(os.path.join(tmp_dir, "*.json3"))
    if not sub_files:
        # Fallback: try vtt format
        result = subprocess.run(
            [
                "yt-dlp",
                "--write-auto-sub",
                "--sub-lang", "en",
                "--skip-download",
                "--sub-format", "vtt",
                "-o", os.path.join(tmp_dir, "transcript"),
                url,
            ],
            capture_output=True,
            text=True,
        )
        vtt_files = glob.glob(os.path.join(tmp_dir, "*.vtt"))
        if not vtt_files:
            print("No subtitle file found. Output from yt-dlp:")
            print(result.stdout)
            print(result.stderr)
            sys.exit(1)
        text = parse_vtt(vtt_files[0])
    else:
        text = parse_json3(sub_files[0])

    output_path = os.path.join(scratchpads_dir, output_name)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    # Clean up tmp dir
    for f in glob.glob(os.path.join(tmp_dir, "*")):
        os.remove(f)
    os.rmdir(tmp_dir)

    print(f"Transcript saved to: {output_path}")
    print(f"Characters: {len(text)}, Words: {len(text.split())}")


def parse_json3(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    lines = []
    for event in data.get("events", []):
        for seg in event.get("segs", []):
            lines.append(seg.get("utf8", ""))

    raw = "".join(lines)
    # Clean up newlines and duplicate spaces
    text = re.sub(r"\n+", " ", raw)
    text = re.sub(r" {2,}", " ", text).strip()
    return text


def parse_vtt(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        content = f.read()

    # Remove VTT header and timestamp lines
    lines = []
    for line in content.splitlines():
        if re.match(r"^\d{2}:\d{2}", line):  # timestamp
            continue
        if line.strip() in ("WEBVTT", "Kind: captions", "") or line.startswith("Language:"):
            continue
        # Strip inline tags like <00:00:01.000><c>
        line = re.sub(r"<[^>]+>", "", line)
        if line.strip():
            lines.append(line.strip())

    # Deduplicate consecutive identical lines (common in auto-captions)
    deduped = []
    for line in lines:
        if not deduped or line != deduped[-1]:
            deduped.append(line)

    return " ".join(deduped)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    url = sys.argv[1]
    output_name = sys.argv[2] if len(sys.argv) > 2 else "transcript.txt"
    download_transcript(url, output_name)
