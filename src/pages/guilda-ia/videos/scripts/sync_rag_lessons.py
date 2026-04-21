#!/usr/bin/env python3
"""
Sincroniza vídeos RAG com áudios e monta o vídeo final.

Estrutura:
1. Intro (3 cenas)
2. Embeddings (vídeo já existe - 99s) 
3. Chunking (3 cenas)
4. Vector Store (2 cenas)
5. Retrieval (2 cenas)
6. Pipeline (2 cenas)
7. Conclusão (3 cenas)

Regra de timing: tempo_final = max(vídeo + 2s, áudio + 2s)
"""

import subprocess
from pathlib import Path

VIDEO_DIR = Path("/home/alchemist/guildia-ia-video/media/videos/rag_lessons/1080p60")
AUDIO_DIR = Path("/home/alchemist/guildia-ia-video/audio_rag")
OUTPUT_DIR = Path("/home/alchemist/guildia-ia-video/synced_rag")
EMBEDDINGS_VIDEO = Path("/home/alchemist/guildia-ia-video/video_vetores_revisado.mp4")
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
    """Sincroniza vídeo com áudio aplicando a regra de timing."""
    v_dur = get_duration(video_path)
    a_dur = get_duration(audio_path)
    
    tempo_base = v_dur + 2
    tempo_audio = a_dur + 2
    tempo_final = max(tempo_base, tempo_audio)
    
    print(f"  Vídeo: {v_dur:.2f}s | Áudio: {a_dur:.2f}s | Final: {tempo_final:.2f}s")
    
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

# Mapeamento de vídeos para áudios
SCENES = [
    # Introdução
    (VIDEO_DIR / "Intro_Scene1_Titulo.mp4", AUDIO_DIR / "intro/intro_1.ogg", "01_intro_1.mp4"),
    (VIDEO_DIR / "Intro_Scene2_Problema.mp4", AUDIO_DIR / "intro/intro_2.ogg", "02_intro_2.mp4"),
    (VIDEO_DIR / "Intro_Scene3_Solucao.mp4", AUDIO_DIR / "intro/intro_3.ogg", "03_intro_3.mp4"),
    
    # Embeddings (vídeo já existe - incluir depois)
    
    # Chunking
    (VIDEO_DIR / "Chunking_Scene1_Hook.mp4", AUDIO_DIR / "chunking/chunking_1.ogg", "05_chunking_1.mp4"),
    (VIDEO_DIR / "Chunking_Scene2_Problema.mp4", AUDIO_DIR / "chunking/chunking_2.ogg", "06_chunking_2.mp4"),
    (VIDEO_DIR / "Chunking_Scene3_Solucao.mp4", AUDIO_DIR / "chunking/chunking_3.ogg", "07_chunking_3.mp4"),
    
    # Vector Store
    (VIDEO_DIR / "VectorStore_Scene1_Hook.mp4", AUDIO_DIR / "vectorstore/vectorstore_1.ogg", "08_vectorstore_1.mp4"),
    (VIDEO_DIR / "VectorStore_Scene2_Solucao.mp4", AUDIO_DIR / "vectorstore/vectorstore_2.ogg", "09_vectorstore_2.mp4"),
    
    # Retrieval
    (VIDEO_DIR / "Retrieval_Scene1_Hook.mp4", AUDIO_DIR / "retrieval/retrieval_1.ogg", "10_retrieval_1.mp4"),
    (VIDEO_DIR / "Retrieval_Scene2_Processo.mp4", AUDIO_DIR / "retrieval/retrieval_2.ogg", "11_retrieval_2.mp4"),
    
    # Pipeline
    (VIDEO_DIR / "RAGPipeline_Scene1_Juntando.mp4", AUDIO_DIR / "pipeline/pipeline_1.ogg", "12_pipeline_1.mp4"),
    (VIDEO_DIR / "RAGPipeline_Scene2_Resumo.mp4", AUDIO_DIR / "pipeline/pipeline_2.ogg", "13_pipeline_2.mp4"),
    
    # Conclusão
    (VIDEO_DIR / "Conclusao_Scene1_Resumo.mp4", AUDIO_DIR / "conclusao/conclusao_1.ogg", "14_conclusao_1.mp4"),
    (VIDEO_DIR / "Conclusao_Scene2_Aplicacao.mp4", AUDIO_DIR / "conclusao/conclusao_2.ogg", "15_conclusao_2.mp4"),
    (VIDEO_DIR / "Conclusao_Scene3_Proximos.mp4", AUDIO_DIR / "conclusao/conclusao_3.ogg", "16_conclusao_3.mp4"),
]

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    print("=== SINCRONIZANDO VÍDEOS RAG ===\n")
    
    durations = []
    
    # Sincronizar cenas individuais
    for i, (video_path, audio_path, output_name) in enumerate(SCENES, 1):
        print(f"[{i:02d}] {output_name}")
        
        if not video_path.exists():
            print(f"  ERRO: Vídeo não encontrado: {video_path}")
            continue
        
        output_path = OUTPUT_DIR / output_name
        duration = sync_video_audio(video_path, audio_path, output_path)
        durations.append((output_name, duration))
    
    # Adicionar vídeo de embeddings (já sincronizado)
    embeddings_name = "04_embeddings.mp4"
    embeddings_output = OUTPUT_DIR / embeddings_name
    
    # Copiar vídeo de embeddings para o diretório de saída
    if EMBEDDINGS_VIDEO.exists():
        import shutil
        shutil.copy(EMBEDDINGS_VIDEO, embeddings_output)
        emb_dur = get_duration(embeddings_output)
        durations.insert(3, (embeddings_name, emb_dur))
        print(f"\n[04] {embeddings_name}: {emb_dur:.2f}s (vídeo existente)")
    
    print(f"\n=== DURAÇÃO TOTAL: {sum(d for _, d in durations):.1f}s ({sum(d for _, d in durations)/60:.1f} min) ===")
    
    # Criar lista de concatenação ordenada
    concat_list = OUTPUT_DIR / "concat_list.txt"
    with open(concat_list, "w") as f:
        for name, _ in sorted(durations):
            f.write(f"file '{name}'\n")
    
    # Concatenar
    final_output = FINAL_DIR / "rag_completo.mp4"
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
    
    if final_dur > 180:
        print(f"\n⚠️  Vídeo maior que 3 minutos. WhatsApp limita a 180MB.")
        print(f"   Tamanho estimado: {final_dur * 1.5:.0f}MB (pode variar)")
    
    concat_list.unlink()

if __name__ == "__main__":
    main()