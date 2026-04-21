#!/usr/bin/env python3
"""
Gera áudios TTS para Aula 01 — Nomenclaturas de IA
Usa edge-tts com voz pt-BR-AntonioNeural

Correções de pronúncia:
- "IA" → "I.A." (para não ler como verbo "ia")
- "Gemini" → "djeminái" (fonética portuguesa)
- Pontuação extra para separar "IA. RAG" (evitar "iarraguza")
"""

import asyncio
import subprocess
from pathlib import Path

VOICE = "pt-BR-AntonioNeural"
AUDIO_DIR = Path(__git_dir__() if False else Path.home() / "git/website/src/pages/guilda-ia/videos/aula01/audio")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

# Textos corrigidos para pronúncia
TEXTS = {
    "cena1_hook": (
        "Se você já ouviu alguém falar I. A. pra descrever um chatbot, "
        "ou RAG como se fosse um modelo... "
        "você não tá sozinho. "
        "Esses quatro termos — I. A., LLM, RAG e Agente — "
        "vivem sendo usados como se fossem a mesma coisa. "
        "E não são. Entender a diferença é o primeiro passo "
        "pra conseguir construir qualquer coisa com essa tecnologia."
    ),

    "cena2_ia": (
        "Inteligência Artificial é o nome do campo. "
        "Qualquer sistema que faz algo inteligente é I. A. "
        "O filtro de spam do seu email? I. A. "
        "Um motor de xadrez? I. A. "
        "O ChatGPT? Também I. A. "
        "É o guarda-chuva que cobre tudo — "
        "desde regras simples dos anos 50 "
        "até os modelos de bilhões de parâmetros de hoje."
    ),

    "cena3_llm": (
        "LLM é um tipo de I. A. — "
        "um modelo treinado pra prever a próxima palavra. "
        "É o que está por trás do ChatGPT, do Claude, do djeminái. "
        "Pra quem constrói, o que importa são quatro capacidades: "
        "tool calling, que é o modelo chamar ferramentas externas. "
        "Raciocínio, que é pensar passo a passo. "
        "Contexto longo, com janelas de mais de cem mil tokens. "
        "E multimodalidade, que é processar imagem, áudio e vídeo."
    ),

    "cena4_limites": (
        "Mas o LLM tem limites. "
        "Ele não calcula — se você perguntar 234 vezes 987, ele chuta. "
        "Ele não sabe fatos específicos — "
        "suas notas, seus documentos, nada disso tá no treinamento dele. "
        "E ele não tem memória de longo prazo — "
        "cada conversa começa do zero."
    ),

    "cena5_rag": (
        "RAG é a técnica que resolve esse problema de o LLM não saber. "
        "Funciona assim: o usuário faz uma pergunta, "
        "o sistema busca documentos relevantes, "
        "junta esses documentos com a pergunta, "
        "e passa tudo pro LLM gerar uma resposta fundamentada. "
        "Sem RAG, o modelo inventa. "
        "Com RAG, ele responde com base nos seus documentos."
    ),

    "cena6_agente": (
        "Agente vai além. "
        "É um sistema que junta LLM com ferramentas e memória. "
        "O modelo de linguagem faz inferência, decide o que fazer, "
        "e usa ferramentas reais — "
        "uma calculadora, uma busca na web, acesso a arquivos. "
        "Um LLM puro só fala. "
        "Um agente fala e faz. "
        "É a diferença entre um consultor e um assistente que executa."
    ),

    "cena7_resumo": (
        "Pra fixar: I. A. é o campo geral. "
        "LLM é um tipo de I. A. "
        "Já o RAG, usa o LLM junto com documentos. "
        "E o Agente usa LLM mais ferramentas mais memória. "
        "Quanto mais específico o termo, mais componentes estão envolvidos."
    ),

    "cena8_cta": (
        "Ao longo da Guilda, vamos cobrir tudo isso na prática. "
        "Da semana 1 com os conceitos, "
        "até a semana 10 com um agente completo. "
        "O material tá no site, gratuito. Comece pelo começo."
    ),
}


async def generate_audio(text: str, output_path: Path):
    """Generate audio using edge-tts"""
    import edge_tts

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(str(output_path))
    print(f"  OK: {output_path.name}")


async def main():
    print("=== Gerando áudios Aula 01 (corrigidos) ===\n")

    # Backup originals
    for name in TEXTS:
        old = AUDIO_DIR / f"{name}.mp3"
        if old.exists():
            backup = AUDIO_DIR / "backup"
            backup.mkdir(exist_ok=True)
            bak = backup / f"{name}.mp3.bak1"
            if not bak.exists():
                import shutil
                shutil.copy2(old, bak)
                print(f"  Backup: {old.name} → {bak.name}")

    # Generate new audio
    for name, text in TEXTS.items():
        output = AUDIO_DIR / f"{name}.mp3"
        await generate_audio(text, output)

    print("\n=== Concluído! ===")
    print("Áudios gerados em:", AUDIO_DIR)

    # Print durations
    print("\nDurações:")
    for name in TEXTS:
        output = AUDIO_DIR / f"{name}.mp3"
        if output.exists():
            result = subprocess.run(
                ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                 "-of", "default=noprint_wrappers=1:nokey=1", str(output)],
                capture_output=True, text=True
            )
            dur = float(result.stdout.strip())
            print(f"  {name}: {dur:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())