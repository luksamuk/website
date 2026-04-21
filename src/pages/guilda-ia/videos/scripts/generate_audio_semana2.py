#!/usr/bin/env python3
"""
Gera áudios Edge TTS para Aula 2: Prompting.
"""

import subprocess
from pathlib import Path

VOICE = "pt-BR-AntonioNeural"

ROTEIRO = [
    ("hook", "Prompting. Como falar com IA. A mesma pergunta pode gerar respostas completamente diferentes. Você já notou isso?"),
    ("problema", "O problema: a mesma LLM pode dar respostas inúteis ou excelentes, dependendo de como você pergunta. Um prompt vago gera resposta genérica. Um prompt claro gera resposta específica. A diferença está no prompt."),
    ("zeroshot", "Zero-shot: você pede sem dar exemplos. 'Traduza para inglês: Bom dia.' O modelo já sabe traduzir. Use zero-shot para tarefas simples e diretas."),
    ("fewshot", "Few-shot: você dá exemplos antes. 'Gato vira Cat, Cachorro vira Dog, Pássaro vira Bird.' Agora a IA entende o padrão. 'Peixe vira?' E ela responde 'Fish.' Use few-shot quando você precisa de um formato específico."),
    ("role", "Role prompting: você define quem a IA deve ser. 'Você é um professor de matemática do ensino médio, especializado em explicar conceitos complexos de forma simples.' Um bom role tem: identidade, expertise, público, e tom."),
    ("cot", "Chain-of-thought: você pede para pensar passo a passo. 'Roger tem 5 bolas, compra 2 latas de 3. Quantas?' Sem CoT, a IA pode chutar. Com CoT, ela pensa: '5 inicial, 2 vezes 3 é 6, total 11.' Wei e colegas mostraram isso em 2022."),
    ("rcef", "Framework R C E F: Role, quem você é; Context, a situação; Examples, exemplos de input-output; Format, formato da resposta. Um prompt estruturado tem essas quatro partes."),
    ("resumo", "Resumo: zero-shot para simples, few-shot para formato, role para contexto, chain-of-thought para raciocínio, e R C E F para estruturar. Material em luksamuk.codes."),
]

def main():
    base_dir = Path("/home/alchemist/guildia-ia-video/audio_semana2")
    base_dir.mkdir(exist_ok=True)
    
    print("=== GERANDO ÁUDIOS SEMANA 2 ===\n")
    
    total = 0
    
    for slug, texto in ROTEIRO:
        output = base_dir / f"{slug}.ogg"
        
        cmd = [
            "edge-tts", "--voice", VOICE,
            "--text", texto,
            "--write-media", str(output)
        ]
        
        subprocess.run(cmd, capture_output=True)
        
        # Obter duração
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(output)],
            capture_output=True, text=True
        )
        dur = float(result.stdout.strip())
        total += dur
        
        print(f"  {slug}: {dur:.2f}s")
    
    print(f"\n=== TOTAL: {total:.1f}s ({total/60:.1f} min) ===")

if __name__ == "__main__":
    main()