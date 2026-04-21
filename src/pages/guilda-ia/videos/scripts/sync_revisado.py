#!/usr/bin/env python3
"""
Pipeline para sincronizar vídeos Manim com áudio TTS.
Aplica a regra: tempo_final = max(duração_vídeo + 2s, duração_áudio + 2s)
"""

import subprocess
from pathlib import Path

# Diretórios
VIDEO_DIR = Path("/home/alchemist/guildia-ia-video/media/videos/script_vetores_revisado/2160p60")
AUDIO_DIR = Path("/home/alchemist/guildia-ia-video/audio_revisado")
OUTPUT_DIR = Path("/home/alchemist/guildia-ia-video/synced_revisado")
FINAL_DIR = Path("/home/alchemist/guildia-ia-video")

def get_duration(file_path: Path) -> float:
    """Obtém duração de vídeo ou áudio em segundos."""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(file_path)],
        capture_output=True, text=True
    )
    return float(result.stdout.strip())

def sync_video_audio(video_path: Path, audio_path: Path, output_path: Path) -> float:
    """
    Sincroniza vídeo com áudio aplicando a regra de timing correta.
    
    Regra:
    - tempo_base = duração_vídeo + 2s (leitura)
    - tempo_audio = duração_áudio + 2s (leitura)
    - tempo_final = max(tempo_base, tempo_audio)
    
    Returns:
        Duração final do vídeo
    """
    v_dur = get_duration(video_path)
    a_dur = get_duration(audio_path)
    
    # REGRA CORRETA: sempre +2s para leitura
    tempo_base = v_dur + 2
    tempo_audio_dur = a_dur + 2
    tempo_final = max(tempo_base, tempo_audio_dur)
    
    print(f"  Vídeo: {v_dur:.2f}s | Áudio: {a_dur:.2f}s | Final: {tempo_final:.2f}s")
    
    # Estender vídeo se necessário
    if tempo_final > v_dur:
        extend_time = tempo_final - v_dur
        temp = output_path.with_suffix(".temp.mp4")
        subprocess.run([
            "ffmpeg", "-y", "-i", str(video_path),
            "-vf", f"tpad=stop_mode=clone:stop_duration={extend_time:.3f}",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-t", str(tempo_final),
            str(temp)
        ], capture_output=True)
        video_input = temp
    else:
        temp = None
        video_input = video_path
    
    # Combinar vídeo com áudio
    cmd = [
        "ffmpeg", "-y",
        "-i", str(video_input),
        "-i", str(audio_path),
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-c:a", "aac", "-b:a", "128k",
        "-shortest",
        str(output_path)
    ]
    subprocess.run(cmd, capture_output=True)
    
    if temp and temp.exists():
        temp.unlink()
    
    return tempo_final

# Mapeamento de cenas para áudios
SCENES = [
    (VIDEO_DIR / "Scene1_Introducao.mp4", AUDIO_DIR / "cena1_intro.ogg", "01_Introducao.mp4"),
    (VIDEO_DIR / "Scene2_Visualizacao2D.mp4", AUDIO_DIR / "cena2_visual.ogg", "02_Visualizacao2D.mp4"),
    (VIDEO_DIR / "Scene3_CirculoUnitario.mp4", AUDIO_DIR / "cena3_circulo.ogg", "03_CirculoUnitario.mp4"),
    (VIDEO_DIR / "Scene4_VetorEProjecao.mp4", AUDIO_DIR / "cena4_projecao.ogg", "04_VetorEProjecao.mp4"),
    (VIDEO_DIR / "Scene5_DoisVetores.mp4", AUDIO_DIR / "cena5_angulo.ogg", "05_DoisVetores.mp4"),
    (VIDEO_DIR / "Scene6_VetoresOpostos.mp4", AUDIO_DIR / "cena6_opostos.ogg", "06_VetoresOpostos.mp4"),
    (VIDEO_DIR / "Scene7_Formula.mp4", AUDIO_DIR / "cena7_formula.ogg", "07_Formula.mp4"),
    (VIDEO_DIR / "Scene8_Resumo.mp4", AUDIO_DIR / "cena8_resumo.ogg", "08_Resumo.mp4"),
]

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    print("=== SINCRONIZANDO CENAS ===\n")
    durations = []
    
    for i, (video_path, audio_path, output_name) in enumerate(SCENES, 1):
        print(f"[{i:02d}] {output_name}")
        
        if not video_path.exists():
            print(f"  ERRO: Vídeo não encontrado: {video_path}")
            continue
        
        output_path = OUTPUT_DIR / output_name
        duration = sync_video_audio(video_path, audio_path, output_path)
        durations.append(duration)
    
    print(f"\n=== DURAÇÃO TOTAL: {sum(durations):.1f}s ({sum(durations)/60:.1f} min) ===")
    
    # Criar lista de concatenação
    concat_list = OUTPUT_DIR / "concat_list.txt"
    with open(concat_list, "w") as f:
        for _, _, output_name in SCENES:
            f.write(f"file '{output_name}'\n")
    
    # Concatenar
    final_output = FINAL_DIR / "video_vetores_revisado.mp4"
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