#!/usr/bin/env python3
"""Gera áudios Edge TTS para as aulas de RAG."""

import subprocess
from pathlib import Path
import random

# Roteiros por vídeo
VÍDEO0_INTRO = [
    ("intro_1", "R A G. Retrieval-Augmented Generation. Como dar memória e contexto para L L Ms."),
    ("intro_2", "O problema: LLMs são treinados com dados até certo momento. Eles não conhecem seus documentos, não conhecem seus pedidos, não conhecem sua empresa."),
    ("intro_3", "A solução se chama RAG. Você busca informações relevantes, passa para o LLM junto com a pergunta, e ele gera uma resposta fundamentada."),
]

VÍDEO1_EMBEDDINGS = [
    # Já temos esse vídeo - vídeo revisado dos vetores (99s)
]

VÍDEO2_CHUNKING = [
    ("chunking_1", "Como você divide um documento de cem páginas em pedaços que fazem sentido?"),
    ("chunking_2", "O problema é que LLMs têm limite de contexto. Você não pode passar cem páginas de uma vez. O modelo vai truncar ou dar erro."),
    ("chunking_3", "A solução se chama chunking. Você pode dividir por tamanho fixo, por semântica, ou recursivamente. O resultado são pedaços menores que o modelo consegue processar."),
]

VÍDEO3_VECTOR_STORE = [
    ("vectorstore_1", "Onde guardar milhares de vetores e encontrar o certo em menos de um segundo?"),
    ("vectorstore_2", "Vector Database. Ferramentas como FAISS, Chroma e Pinecone fazem indexação eficiente e busca rápida. O processo: query vira embedding, busca no banco, retorna os k mais similares."),
]

VÍDEO4_RETRIEVAL = [
    ("retrieval_1", "Busca semântica é diferente de busca por palavras-chave. Se você busca 'como fazer café', a busca semântica encontra também 'preparar expresso'."),
    ("retrieval_2", "Em RAG, retrieval funciona assim: query vira embedding, busca no vector store, retorna os top-k documentos mais similares. Normalmente k igual a três funciona bem."),
]

VÍDEO5_PIPELINE = [
    ("pipeline_1", "Pipeline RAG completo. Documentos viram chunks, chunks viram embeddings, embeddings vão para o vector store. Quando chega uma query, você faz retrieval, augmentation com os documentos, e generation com o LLM."),
    ("pipeline_2", "RAG em resumo: Retrieval busca contexto relevante, Augmentation combina query com documentos, Generation gera a resposta fundamentada. Fundamentos que você usa em qualquer sistema de RAG."),
]

VÍDEO6_CONCLUSAO = [
    ("conclusao_1", "O que você aprendeu hoje: Embeddings para converter texto em vetores, Chunking para dividir documentos, Vector Store para armazenar, Retrieval para buscar, e o Pipeline completo."),
    ("conclusao_2", "Onde usar RAG? Chatbots de suporte, assistentes jurídicos, FAQ inteligente, análise de contratos. Qualquer lugar onde você precisa de respostas baseadas em documentos específicos."),
    ("conclusao_3", "Próximos passos: pratique com dados reais, experimente diferentes tamanhos de chunk, compare vector stores, e meça a qualidade das respostas. Todo o material está em luksamuk.codes."),
]

def main():
    base_dir = Path("/home/alchemist/guildia-ia-video/audio_rag")
    
    videos = [
        ("intro", VÍDEO0_INTRO),
        ("chunking", VÍDEO2_CHUNKING),
        ("vectorstore", VÍDEO3_VECTOR_STORE),
        ("retrieval", VÍDEO4_RETRIEVAL),
        ("pipeline", VÍDEO5_PIPELINE),
        ("conclusao", VÍDEO6_CONCLUSAO),
    ]
    
    print("=== GERANDO ÁUDIOS RAG ===\n")
    
    total_dur = 0
    
    for video_name, roteiro in videos:
        video_dir = base_dir / video_name
        video_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"--- {video_name.upper()} ---")
        
        video_dur = 0
        
        for nome, texto in roteiro:
            output = video_dir / f"{nome}.ogg"
            
            cmd = [
                "edge-tts",
                "--voice", "pt-BR-AntonioNeural",
                "--text", texto,
                "--write-media", str(output)
            ]
            
            subprocess.run(cmd, check=True, capture_output=True)
            
            # Duração
            result = subprocess.run(
                ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                 "-of", "default=noprint_wrappers=1:nokey=1", str(output)],
                capture_output=True, text=True
            )
            dur = float(result.stdout.strip())
            video_dur += dur
            
            print(f"  {nome}: {dur:.2f}s")
        
        print(f"  Subtotal: {video_dur:.1f}s\n")
        total_dur += video_dur
    
    print(f"=== DURAÇÃO TOTAL: {total_dur:.1f}s ({total_dur/60:.1f} min) ===")

if __name__ == "__main__":
    main()