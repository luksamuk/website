# Roteiro — Mini Aula: Prompting Básico (Semana 02)

Duração alvo: ~5-6 minutos
voz: pt-BR-AntonioNeural (Edge TTS)
Formato: 1080p60, dark theme

## Cena 1: Título (~12s)

**Visual:** "Prompting Básico" surge com efeito typewriter. Subtítulo "Como falar com IA".fade in. Fundo: radial lines animadas.

**Narração:**
> Prompting básico. Como falar com I A. Semana dois da Guilda de I A.

## Cena 2: O Problema — Vago vs Específico (~18s)

**Visual:** Dois blocos lado a lado. Esquerda: "Me fale sobre gatos" com resposta genérica cinza. Direita: "Quais as 3 raças mais populares?" com resposta colorida. Seta de "Vago" → "Específico".

**Narração:**
> A mesma pergunta gera respostas completamente diferentes. "Me fale sobre gatos" vira um texto genérico. "Quais as três raças de gatos mais populares no Brasil e por quê" vira uma resposta específica. A diferença? O prompt.

## Cena 3: O que é prompt (~12s)

**Visual:** Diagrama: Prompt → (Role + Context + Examples + Format) → Resposta. Cada letra aparece com cor.

**Narração:**
> Um prompt é a instrução que você dá ao modelo. Inclui a pergunta, o contexto, exemplos, e o formato que você espera. Quanto mais claro o prompt, mais previsível a resposta.

## Cena 4: Zero-shot vs Few-shot (~20s)

**Visual:** Esquerda: bloco "Zero-shot" com "Traduza: Bom dia → ?". Direita: bloco "Few-shot" com "Gato → Cat, Cachorro → Dog, Pássaro → ?". Transição: exemplos aparecem e modelo "aprende" o padrão.

**Narração:**
> Zero-shot: você pede sem dar exemplos. O modelo tenta, mas pode errar por ambiguidade. "Banco" vira bank ou bench? Few-shot: você dá exemplos antes. O modelo aprende o padrão e responde com mais confiança. Mais exemplos, mais preciso, mas também mais tokens.

## Cena 5: Role Prompting (~16s)

**Visual:** Dois balloons de chat. Esquerda: "Explique derivadas" → resposta genérica. Direita: "Você é professora do ensino médio. Explique derivadas." → resposta didática com ícone de chapéu de professor.

**Narração:**
> Atribuir um papel muda a resposta. "Explique derivadas" sem contexto gera um texto seco. Com role prompting: "Você é uma professora de matemática do ensino médio, paciente e didática", a resposta sai acessível, com exemplos. Role prompting é a base do system prompt de agentes.

## Cena 6: Chain-of-Thought (~18s)

**Visual:** Problema: "Roger tem 5 bolas. Compra 2 latas de 3. Total?" Esquerda: resposta direta "11" (pode estar errada). Direita: raciocínio passo a passo com cores: 5 + (2×3) = 5+6 = 11. Animação de cada passo.

**Narração:**
> Chain of Thought: pedir ao modelo para pensar passo a passo. Sem isso, o modelo chuta a resposta. Com isso, ele explicita o raciocínio e erra menos. Funciona principalmente em modelos menores. Em agentes, ferramentas exigem raciocínio: qual usar e quando.

## Cena 7: Framework RCEF-TC (~20s)

**Visual:** Seis cards aparecem em sequência: R (Role, verde), C (Context, ciano), E (Examples, amarelo), F (Format, rosa), T (Task, laranja), C (Constraints, roxo). Cada um com exemplo curto.

**Narração:**
> RCEF-T C é um framework pra prompts completos. R de Role: quem é o modelo. C de Context: qual a situação. E de Examples: exemplos de entrada e saída. F de Format: como quer a resposta. T de Task: o que fazer. E C de Constraints: o que não fazer. Zero-shot é sem E. Few-shot é com E. Role é o R.

## Cena 8: RCEF-TC na prática (~16s)

**Visual:** Exemplo de prompt ruim "Me ajuda com meu TCC" sendo refatorado para RCEF-TC. Cada letra preenche um campo: R=tutor, C=Computação semestre 6, T=Revisão, F=Bullets, C=3 páginas.

**Narração:**
> Na prática: "Me ajuda com meu TCC" vira "R, você é um tutor de computação. C, sou do sexto semestre. T, preciso de revisão de metodologia. F, responda em tópicos. C, máximo três páginas." Toda a diferença.

## Cena 9: Alucinações (~14s)

**Visual:** "Quem ganhou a copa de 2042?" → modelo inventa resultado (alaranjado, falso). Depois "Responda apenas se tiver certeza" → "Não sei" (verde, honesto).

**Narração:**
> Às vezes o modelo erra. Se inventa algo que não existe, é alucinação. Se melhora quando você refaz o prompt, era prompt ruim. Sempre teste: reformule com mais contexto. Se ainda errar, é limitação do modelo.

## Cena 10: Fofoca da Semana (~16s)

**Visual:** Três cards de notícia aparecem: "Kimi K2.6: 1T params, open weights", "DeepSeek V4 Pro: 1.6T, 1M contexto, MIT", "Claude Code: removido do Pro, reposto em 12h". Badge "Abril 2026".

**Narração:**
> Fofoca da semana: Kimi K2.6 lançou com 1 trilhão de parâmetros e open weights. DeepSeek V4 Pro com 1.6 trilhões, 1 milhão de contexto, licença M I T. E o Claude Code? Removido do plano Pro da Anthropic em vinte e um de abril. Voltou doze horas depois. Open weights são a saída.

## Cena 11: Encerramento (~10s)

**Visual:** "O prompt é como uma receita. Ingredientes claros = prato previsível." + "Semana 03: Python + API". Logo Guilda de IA.

**Narração:**
> O prompt é como uma receita. Ingredientes claros, prato previsível. Na próxima semana: Python e chamadas de A P I. Até lá.