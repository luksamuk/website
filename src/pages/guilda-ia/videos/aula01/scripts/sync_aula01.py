#!/usr/bin/env python3
"""Sincroniza vídeos Manim com áudios TTS para Aula 01"""

import subprocess
from pathlib import Path

VIDEO_DIR = Path.home() / "media/videos/aula01_nomenclaturas/1080p60"
AUDIO_DIR = Path.home() / "git/website/src/pages/guilda-ia/videos/aula01/audio"
SYNCED_DIR = Path.home() / "git/website/src/pages/guilda-ia/videos/aula01/videos/synced"
SYNCED_DIR.mkdir(parents=True, exist_ok=True)

SCENES = [
    ("Scene1Hook.mp4", "cena1_hook.mp3", "01_hook.mp4"),
    ("Scene2IA.mp4", "cena2_ia.mp3", "02_ia.mp4"),
    ("Scene3LLM.mp4", "cena3_llm.mp3", "03_llm.mp4"),
    ("Scene4Limites.mp4", "cena4_limites.mp3", "04_limites.mp4"),
    ("Scene5RAG.mp4", "cena5_rag.mp3", "05_rag.mp4"),
    ("Scene6Agente.mp4", "cena6_agente.mp3", "06_agente.mp4"),
    ("Scene7Resumo.mp4", "cena7_resumo.mp3", "07_resumo.mp4"),
    ("Scene8CTA.mp4", "cena8_cta.mp3", "08_cta.mp4"),
]

def get_duration(file_path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(file_path)],
        capture_output=True, text=True
    )
    return float(result.stdout.strip())

def fix_audio_pop(audio_path, output_path):
    """Remove Edge TTS click at sample 0"""
    import wave
    import numpy as np

    # Convert to WAV
    wav_path = output_path.with_suffix('.wav')
    subprocess.run([
        "ffmpeg", "-y", "-i", str(audio_path),
        "-acodec", "pcm_s16le", "-ar", "48000", "-ac", "1",
        str(wav_path)
    ], capture_output=True)

    with wave.open(str(wav_path), 'rb') as w:
        framerate = w.getframerate()
        raw = w.readframes(w.getnframes())

    samples = np.frombuffer(raw, dtype=np.int16)
    threshold = 500
    start_idx = 0
    for i, s in enumerate(samples):
        if abs(s) > threshold:
            start_idx = i
            break

    corrected = samples.copy()
    corrected[:start_idx] = 0
    fade_len = 50
    for i in range(fade_len):
        idx = start_idx - fade_len + i
        if 0 <= idx < len(corrected):
            corrected[idx] *= (i / fade_len)

    fixed_wav = output_path.with_name(output_path.stem + "_fixed.wav")
    with wave.open(str(fixed_wav), 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(framerate)
        w.writeframes(corrected.tobytes())

    return fixed_wav

def sync_scene(video_name, audio_name, output_name):
    video_path = VIDEO_DIR / video_name
    audio_path = AUDIO_DIR / audio_name
    output_path = SYNCED_DIR / output_name

    if not video_path.exists():
        print(f"  SKIP: {video_name} not found")
        return None
    if not audio_path.exists():
        print(f"  SKIP: {audio_name} not found")
        return None

    v_dur = get_duration(video_path)
    a_dur = get_duration(audio_path)
    tempo_final = max(v_dur + 2, a_dur + 2)

    print(f"  Video: {v_dur:.1f}s | Audio: {a_dur:.1f}s | Final: {tempo_final:.1f}s")

    # Fix audio pop
    fixed_audio = fix_audio_pop(audio_path, output_path)

    # Strip video (remove any metadata)
    stripped = SYNCED_DIR / (output_path.stem + "_stripped.mp4")
    subprocess.run([
        "ffmpeg", "-y", "-i", str(video_path),
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-an",
        str(stripped)
    ], capture_output=True)

    # Extend video if needed
    if tempo_final > v_dur:
        extend = tempo_final - v_dur
        extended = SYNCED_DIR / (output_path.stem + "_extended.mp4")
        subprocess.run([
            "ffmpeg", "-y", "-i", str(stripped),
            "-vf", f"tpad=stop_mode=clone:stop_duration={extend:.3f}",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-t", str(tempo_final),
            str(extended)
        ], capture_output=True)
        video_source = extended
    else:
        video_source = stripped

    # Combine video + audio
    subprocess.run([
        "ffmpeg", "-y",
        "-i", str(video_source),
        "-i", str(fixed_audio),
        "-map", "0:v", "-map", "1:a",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "128k",
        "-shortest",
        str(output_path)
    ], capture_output=True)

    # Cleanup temp files
    for f in [stripped, fixed_audio]:
        if f.exists() and f != output_path:
            f.unlink()
    extended = SYNCED_DIR / (output_path.stem + "_extended.mp4")
    if extended.exists():
        extended.unlink()

    dur = get_duration(output_path)
    print(f"  OK: {output_name} ({dur:.1f}s)")
    return output_path

def main():
    print("=== Sincronizando Aula 01 ===\n")
    synced_files = []

    for video_name, audio_name, output_name in SCENES:
        result = sync_scene(video_name, audio_name, output_name)
        if result:
            synced_files.append(result)

    if len(synced_files) < len(SCENES):
        print(f"\n⚠️  {len(SCENES) - len(synced_files)} cenas faltando!")
        return

    # Create concat list
    concat_file = SYNCED_DIR / "concat.txt"
    with open(concat_file, 'w') as f:
        for path in synced_files:
            f.write(f"file '{path.name}'\n")

    # Final concatenation
    final = SYNCED_DIR.parent.parent / "aula01_nomenclaturas.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(concat_file),
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-c:a", "aac", "-b:a", "128k",
        str(final)
    ], capture_output=True)

    if final.exists():
        dur = get_duration(final)
        size_mb = final.stat().st_size / 1024 / 1024
        print(f"\n✅ Vídeo final: {final}")
        print(f"   Duração: {dur:.1f}s ({dur/60:.1f} min)")
        print(f"   Tamanho: {size_mb:.1f} MB")
    else:
        print("\n❌ Falha na concatenação final")

if __name__ == "__main__":
    main()