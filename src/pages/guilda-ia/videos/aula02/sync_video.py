#!/usr/bin/env python3
"""Sync Manim videos with Edge TTS audio for Aula 02 - Prompting Básico."""
import subprocess
from pathlib import Path

BASE = Path("/home/alchemist/git/website/src/pages/guilda-ia/videos/aula02")
VIDEO_DIR = BASE / "media" / "videos" / "prompting_video" / "1080p60"
AUDIO_DIR = BASE
SYNCED_DIR = BASE / "synced"
SYNCED_DIR.mkdir(exist_ok=True)

SCENES = [
    ("Scene1Titulo.mp4", "cena1.mp3", "01_titulo.mp4"),
    ("Scene2Problema.mp4", "cena2.mp3", "02_problema.mp4"),
    ("Scene3OQueE.mp4", "cena3.mp3", "03_o_que_e.mp4"),
    ("Scene4ZeroFewShot.mp4", "cena4.mp3", "04_zero_few_shot.mp4"),
    ("Scene5RolePrompting.mp4", "cena5.mp3", "05_role_prompting.mp4"),
    ("Scene6CoT.mp4", "cena6.mp3", "06_cot.mp4"),
    ("Scene7RCEF.mp4", "cena7.mp3", "07_rcef.mp4"),
    ("Scene8RCEFPratica.mp4", "cena8.mp3", "08_rcef_pratica.mp4"),
    ("Scene9Alucinacao.mp4", "cena9.mp3", "09_alucinacao.mp4"),
    # NO fofoca — removed per user request
    ("Scene10Encerramento.mp4", "cena11.mp3", "10_encerramento.mp4"),
]

def get_duration(file_path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(file_path)],
        capture_output=True, text=True
    )
    return float(result.stdout.strip())

def remove_audio_pops(audio_path, output_path):
    """Remove Edge TTS pop/click at sample 0."""
    wav_in = str(output_path).replace(".mp4", "_in.wav")
    wav_out = str(output_path).replace(".mp4", "_fixed.wav")
    
    result = subprocess.run([
        "ffmpeg", "-y", "-i", str(audio_path),
        "-acodec", "pcm_s16le", "-ar", "48000", "-ac", "1", wav_in
    ], capture_output=True)
    if result.returncode != 0:
        return str(audio_path)
    
    wav_in_path = Path(wav_in)
    if not wav_in_path.exists() or wav_in_path.stat().st_size < 100:
        return str(audio_path)
    
    import wave, numpy as np
    try:
        with wave.open(wav_in, 'rb') as wav:
            framerate = wav.getframerate()
            raw = wav.readframes(wav.getnframes())
    except Exception:
        wav_in_path.unlink(missing_ok=True)
        return str(audio_path)
    
    samples = np.frombuffer(raw, dtype=np.int16)
    threshold = 500
    start_idx = 0
    for i, s in enumerate(samples):
        if abs(s) > threshold:
            start_idx = i
            break
    
    corrected = samples.copy()
    corrected[:start_idx] = 0
    fade_len = min(50, start_idx)
    for i in range(fade_len):
        idx = start_idx - fade_len + i
        if 0 <= idx < len(corrected):
            corrected[idx] = int(corrected[idx] * (i / fade_len))
    
    with wave.open(wav_out, 'wb') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(framerate)
        wav.writeframes(corrected.tobytes())
    
    wav_in_path.unlink(missing_ok=True)
    return wav_out

def sync_video_audio(video_path, audio_path, output_path):
    v_dur = get_duration(video_path)
    a_dur = get_duration(audio_path)
    
    tempo_final = max(v_dur + 2, a_dur + 2)
    
    # Strip video
    stripped = str(output_path).replace(".mp4", "_stripped.mp4")
    subprocess.run([
        "ffmpeg", "-y", "-i", str(video_path),
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-an", stripped
    ], capture_output=True)
    
    # Fix audio pops
    fixed_audio = remove_audio_pops(audio_path, output_path)
    
    # Extend video if needed
    if tempo_final > v_dur:
        extend = tempo_final - v_dur
        extended = str(output_path).replace(".mp4", "_extended.mp4")
        subprocess.run([
            "ffmpeg", "-y", "-i", stripped,
            "-vf", f"tpad=stop_mode=clone:stop_duration={extend:.3f}",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-t", str(tempo_final), extended
        ], capture_output=True)
        video_for_mux = extended
    else:
        video_for_mux = stripped
    
    # Mux
    subprocess.run([
        "ffmpeg", "-y", "-i", video_for_mux, "-i", fixed_audio,
        "-map", "0:v", "-map", "1:a",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "128k",
        "-shortest", str(output_path)
    ], capture_output=True)
    
    # Cleanup
    for f in [stripped, video_for_mux]:
        Path(f).unlink(missing_ok=True)
    if fixed_audio != str(audio_path):
        Path(fixed_audio).unlink(missing_ok=True)
    
    print(f"  ✓ {output_path.name} (V:{v_dur:.1f}s A:{a_dur:.1f}s → {tempo_final:.1f}s)")

def main():
    print("Syncing Aula 02 - Prompting Básico (v2 - no fofoca)...")
    
    missing = []
    synced_paths = []
    
    for video_name, audio_name, output_name in SCENES:
        video_path = VIDEO_DIR / video_name
        audio_path = AUDIO_DIR / audio_name
        output_path = SYNCED_DIR / output_name
        
        if not video_path.exists():
            missing.append(video_name)
            continue
        if not audio_path.exists():
            missing.append(audio_name)
            continue
        
        sync_video_audio(video_path, audio_path, output_path)
        synced_paths.append(output_path)
    
    if missing:
        print(f"\n⚠ Missing files: {missing}")
        return
    
    # Normalize + safe concat
    print("\nNormalizing for safe concat...")
    normalized_dir = SYNCED_DIR / "normalized"
    normalized_dir.mkdir(exist_ok=True)
    
    norm_paths = []
    for i, sp in enumerate(synced_paths, 1):
        norm = normalized_dir / f"norm{i:02d}.mp4"
        subprocess.run([
            "ffmpeg", "-y", "-i", str(sp),
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-r", "30", "-g", "30", "-keyint_min", "30",
            "-sc_threshold", "0",
            "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
            str(norm)
        ], capture_output=True)
        norm_paths.append(norm)
    
    inputs = " ".join([f"-i '{p}'" for p in norm_paths])
    cmd = f"""ffmpeg -y {inputs} \
        -filter_complex "concat=n={len(norm_paths)}:v=1:a=1[outv][outa]" \
        -map "[outv]" -map "[outa]" \
        -c:v libx264 -preset medium -crf 18 \
        -c:a aac \
        "{SYNCED_DIR / 'aula02_prompting.mp4'}" """
    
    result = subprocess.run(cmd, shell=True, capture_output=True)
    
    if result.returncode == 0:
        final = SYNCED_DIR / "aula02_prompting.mp4"
        dur = get_duration(final)
        size_mb = final.stat().st_size / (1024 * 1024)
        print(f"\n✅ Final: {final}")
        print(f"   Duration: {dur:.1f}s ({dur/60:.1f} min)")
        print(f"   Size: {size_mb:.1f} MB")
    else:
        print(f"\n❌ Concat failed: {result.stderr.decode()[-500:]}")
    
    # Cleanup normalized
    import shutil
    shutil.rmtree(normalized_dir, ignore_errors=True)

if __name__ == "__main__":
    main()