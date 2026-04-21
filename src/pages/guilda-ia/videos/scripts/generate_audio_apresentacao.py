#!/usr/bin/env python3
"""Gera áudios Edge TTS para a apresentação da Guilda de IA."""

import subprocess
from pathlib import Path

# Narrações para cada cena
NARRATIONS = [
    # Cena 1 - Hook
    ("cena1_hook", "E se você pudesse criar seu próprio assistente de I A... do zero?"),
    
    # Cena 2 - Contexto
    ("cena2_contexto", "Essa é a proposta da Guilda de I A. Em doze semanas, você passa de curiosidade a prática construindo projetos reais."),
    
    # Cena 3 - Jornada
    ("cena3_jornada", "Começamos com fundamentos. O que é I A, como ela funciona, por que agora. Depois entramos no código: Python, A P Is, R A G, e muito mais."),
    
    # Cena 4 - Demonstração
    ("cena4_demo", "Na prática? Você conecta modelos a ferramentas reais. O agente planeja, executa, e aprende com os resultados."),
    
    # Cena 5 - Comunidade
    ("cena5_comunidade", "Não é um curso fechado. É um espaço de estudo onde você constrói junto com outras pessoas."),
    
    # Cena 6 - CTA
    ("cena6_cta", "Se você tem curiosidade, dá uma olhada. Todo o material está lá, gratuito. Comece pelo começo."),
]

def main():
    audio_dir = Path("/home/alchemist/guildia-ia-video/audio_apresentacao")
    audio_dir.mkdir(exist_ok=True)
    
    print("=== GERANDO ÁUDIOS EDGE TTS ===\n")
    
    durations = []
    
    for i, (name, text) in enumerate(NARRATIONS, 1):
        output = audio_dir / f"{name}.ogg"
        
        # Comando edge-tts
        cmd = [
            "edge-tts",
            "--voice", "pt-BR-AntonioNeural",
            "--text", text,
            "--write-media", str(output)
        ]
        
        subprocess.run(cmd, check=True)
        
        # Obter duração
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(output)],
            capture_output=True, text=True
        )
        dur = float(result.stdout.strip())
        durations.append(dur)
        
        print(f"[{i}] {name}: {dur:.2f}s")
        print(f"    Texto: {text[:60]}...")
    
    print(f"\n=== DURAÇÃO TOTAL: {sum(durations):.1f}s ({sum(durations)/60:.1f} min) ===")
    print(f"Áudios em: {audio_dir}")

if __name__ == "__main__":
    main()