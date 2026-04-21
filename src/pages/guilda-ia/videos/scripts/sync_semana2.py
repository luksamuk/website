#!/usr/bin/env python3
"""
Sincroniza vídeo Semana 2: Prompting.
"""

import subprocess
from pathlib import Path

VIDEO_DIR = Path("/home/alchemist/guildia-ia-video/media/videos/semana2_prompting/1080p60")
AUDIO_DIR = Path("/home/alchemist/guildia-ia-video/audio_semana2")
OUTPUT_DIR = Path("/home/alchemist/guildia-ia-video/synced_semana2")
FINAL_DIR = Path("/home/alchemist/guildia-ia-video")

def get_duration(file_path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(file_path)],
        capture_output=True, text=True
    )
    return float(result.stdout.strip())

def sync_video_audio(video_path, audio_path, output_path):
    v_dur = get_duration(video_path)
    a_dur = get_duration(audio_path)
    
    tempo_final = max(v_dur + 2, a_dur + 2)
    
    print(f"  Vídeo: {v_dur:.2f}s | Áudio: {a_dur:.2f}s | Final: {tempo_final:.2f}s")
    
    if tempo_final > v_dur:
        extend = tempo_final - v_dur
        temp = output_path.with_suffix(".temp.mp4")
        subprocess.run([
            "ffmpeg", "-y", "-i", str(video_path),
            "-vf", f"tpad=stop_mode=clone:stop_duration={extend:.3f}",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-t", str(tempo_final),
            str(temp)
        ], capture_output=True)
        video_input = temp
    else:
        temp = None
        video_input = video_path
    
    subprocess.run([
        "ffmpeg", "-y",
        "-i", str(video_input),
        "-i", str(audio_path),
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-c:a", "aac", "-b:a", "128k",
        "-shortest",
        str(output_path)
    ], capture_output=True)
    
    if temp and temp.exists():
        temp.unlink()
    
    return tempo_final

SCENES = [
    (VIDEO_DIR / "Prompting_Scene1_Hook.mp4", AUDIO_DIR / "hook.ogg", "01_hook.mp4"),
    (VIDEO_DIR / "Prompting_Scene2_Problema.mp4", AUDIO_DIR / "problema.ogg", "02_problema.mp4"),
    (VIDEO_DIR / "Prompting_Scene3_ZeroShot.mp4", AUDIO_DIR / "zeroshot.ogg", "03_zeroshot.mp4"),
    (VIDEO_DIR / "Prompting_Scene4_FewShot.mp4", AUDIO_DIR / "fewshot.ogg", "04_fewshot.mp4"),
    (VIDEO_DIR / "Prompting_Scene5_Role.mp4", AUDIO_DIR / "role.ogg", "05_role.mp4"),
    (VIDEO_DIR / "Prompting_Scene6_CoT.mp4", AUDIO_DIR / "cot.ogg", "06_cot.mp4"),
    (VIDEO_DIR / "Prompting_Scene7_RCEF.mp4", AUDIO_DIR / "rcef.ogg", "07_rcef.mp4"),
    (VIDEO_DIR / "Prompting_Scene8_Resumo.mp4", AUDIO_DIR / "resumo.ogg", "08_resumo.mp4"),
]

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    print("=== SINCRONIZANDO SEMANA 2 ===\n")
    
    durations = []
    
    for video_path, audio_path, output_name in SCENES:
        print(f"[{output_name}]")
        
        if not video_path.exists():
            print(f"  ERRO: {video_path}")
            continue
        
        output_path = OUTPUT_DIR / output_name
        duration = sync_video_audio(video_path, audio_path, output_path)
        durations.append((output_name, duration))
    
    total = sum(d for _, d in durations)
    print(f"\n=== DURAÇÃO TOTAL: {total:.1f}s ({total/60:.2f} min) ===")
    
    # Concatenar
    concat_list = OUTPUT_DIR / "concat_list.txt"
    with open(concat_list, "w") as f:
        for name, _ in sorted(durations):
            f.write(f"file '{name}'\n")
    
    final_output = FINAL_DIR / "semana2_prompting.mp4"
    print("\n=== CONCATENANDO ===")
    
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(concat_list),
        "-c", "copy",
        str(final_output)
    ], capture_output=True)
    
    final_dur = get_duration(final_output)
    print(f"\nVídeo final: {final_output}")
    print(f"Duração: {final_dur:.1f}s ({final_dur/60:.2f} min)")
    
    concat_list.unlink()

if __name__ == "__main__":
    main()