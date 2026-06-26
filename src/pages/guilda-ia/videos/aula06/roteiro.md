# Mini-aula S05 — Primeira Ferramenta
# Roteiro v1 (sem narração por enquanto)

## Cena 1 — Abertura (3s)
- Título: "Primeira Ferramenta"
- Subtítulo: "O agente finalmente faz algo"

## Cena 2 — Hook: LLM não calcula (8s)
- Slide: "234 × 987 = ?"
- LLM prevê a resposta (cara de dúvida)
- Resposta errada aparece: "231.000?"
- Badge: "LLM prevê, não calcula"

## Cena 3 — A solução: ferramentas (8s)
- Diagrama do ciclo: Pensar → Agir (tool_call) → Observar (resultado) → Responder
- 4 quadrantes com ícones
- Badge: "Ferramenta = função Python"

## Cena 4 — @tool: Pydantic resolve (7s)
- Código: função calculate com decorator @tool
- Diagrama simples: LLM → JSON schema → Pydantic → invocação
- Badge: "Descrição clara = ferramenta útil"

## Cena 5 — Ciclo manual: bind_tools (8s)
- 3 passos numerados:
  1. invoke → LLM decide (tool_calls)
  2. Você executa a ferramenta
  3. invoke de novo com ToolMessage → resposta
- Código: trecho do bind_tools

## Cena 6 — Ciclo automático: create_agent (6s)
- Lado esquerdo: código manual (grande, complexo)
- Lado direito: create_agent (2 linhas)
- Setas convergindo pro mesmo resultado
- Badge: "Manual pra aprender, automático pra produzir"

## Cena 7 — Async: um gostinho (5s)
- invoke (síncrono) vs ainvoke (assíncrono)
- Diagrama: agente.ainvoke → "Processando..." → await → resultado
- Badge: "Próxima aula: MCP"

## Cena 8 — CTA (3s)
- "Ferramenta transforma conversa em ação"
- "LLM puro: só fala | Agente com ferramenta: fala E faz"
- Guilda de IA