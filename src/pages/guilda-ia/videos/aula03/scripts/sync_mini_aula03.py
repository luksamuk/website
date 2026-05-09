#!/usr/bin/env python3
"""Sync audio and video for Mini Aula 03 — Python Mínimo."""

import subprocess
import os

BASE = os.path.expanduser("~/git/website/src/pages/guilda-ia/videos/aula03")
VIDEOS = os.path.join(BASE, "scripts", "media", "videos", "python_minimo", "1080p60")
AUDIO = os.path.join(BASE, "media", "audio")
OUT = os.path.join(BASE, "media", "videos")
os.makedirs(OUT, exist_ok=True)

scenes = [
    ("Python_Scene1_Hook", "scene1.mp3"),
    ("Python_Scene2_Variaveis", "scene2.mp3"),
    ("Python_Scene3_ListasDicts", "scene3.mp3"),
    ("Python_Scene4_Funcoes", "scene4.mp3"),
    ("Python_Scene5_CondLoops", "scene5.mp3"),
    ("Python_Scene6_Ponte", "scene6.mp3"),
    ("Python_Scene7_CTA", "scene7.mp3"),
]

synced = []

for scene_name, audio_name in scenes:
    vid = os.path.join(VIDEOS, f"{scene_name}.mp4")
    aud = os.path.join(AUDIO, audio_name)
    out = os.path.join(OUT, f"{scene_name}_synced.mp4")

    # Get audio duration
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", aud],
        capture_output=True, text=True
    )
    audio_dur = float(result.stdout.strip())

    # Pad video to match audio duration, then overlay audio
    cmd = [
        "ffmpeg", "-y",
        "-i", vid,
        "-i", aud,
        "-filter_complex",
        f"[0:v]tpad=stop_mode=clone:stop_duration={audio_dur}[v]",
        "-map", "[v]",
        "-map", "1:a",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-c:a", "aac", "-b:a", "128k",
        "-shortest",
        out
    ]

    print(f"Syncing {scene_name} (audio: {audio_dur:.1f}s)...")
    subprocess.run(cmd, capture_output=True, text=True, check=True)
    synced.append(out)
    print(f"  → {out}")

# Concatenate all synced scenes
concat_list = os.path.join(OUT, "concat.txt")
with open(concat_list, "w") as f:
    for path in synced:
        f.write(f"file '{path}'\n")

final = os.path.join(BASE, "python_minimo_mini_aula.mp4")
cmd = [
    "ffmpeg", "-y",
    "-f", "concat", "-safe", "0",
    "-i", concat_list,
    "-c:v", "libx264", "-preset", "medium", "-crf", "18",
    "-c:a", "aac", "-b:a", "128k",
    final
]

print(f"\nConcatenating {len(synced)} scenes...")
subprocess.run(cmd, capture_output=True, text=True, check=True)
print(f"\n✅ Final video: {final}")

# Get final duration
result = subprocess.run(
    ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", final],
    capture_output=True, text=True
)
print(f"   Duration: {float(result.stdout.strip()):.1f}s")