# Mini-Aula S05: Estrutura de um Agente — Roteiro (v3 — FINAL)

**Duração:** ~75s (animação + waits extras)
**Formato:** Manim + TTS Edge (pt-BR-AntonioNeural, rate=+15%)
**YouTube:** (em breve)

---

## Pronúncia TTS (SOMENTE no texto de narração, NUNCA nos slides/Manim)

| Termo | Slide (visual) | Narração (TTS) |
|-------|---------------|----------------|
| LLM | LLM | L-L-M |
| ReAct | ReAct | Ri-ékt |
| harness | harness | hárnis |

---

## Falas TTS por cena (rate=+15%)

### Cena 1 — Abertura (~5.9s de animação)
> Guil-da de I-A. Aula cinco. Estrutura de um agente.

### Cena 2 — Hook (~9.3s)
> Um L-L-M responde e esquece. Um agente lembra e age. A diferença é o hárnis — a estrutura em volta do modelo.

### Cena 3 — 4 Componentes — Seta curva à ESQUERDA dos boxes (barbada pra esquerda), label à esquerda da seta (~7.5s)
> System prompt define quem o agente é. Memória guarda o que já foi dito. Input é a pergunta, output é a resposta. E toda resposta volta pra memória.

### Cena 4 — Agente na mão (~11.3s)
**Corte 1 (~5.5s):**
> Dicionários e funções. Instruções, histórico vazio, limite de mensagens.

**Corte 2 (~5.5s):**
> System prompt no topo, histórico truncado, pergunta no final. A resposta volta pro histórico.

### Cena 5 — Por que truncar? (~7.3s)
> Conversa cresce, modelo esquece o que tá no meio. É o lost in the middle. Truncar corta as mensagens mais velhas.

### Cena 6 — ReAct (~9.8s)
> Ri-ékt: pensar, agir, observar, voltar. Hoje a gente constrói memória e instruções. Na próxima aula, ferramentas.

### Cena 7 — LangChain (~8.5s)
> Na mão funciona, mas é repetitivo. LangChain abstrai com prompt template, memória, e chamada ao modelo. Tudo encadeado com pipe.

### Cena 8 — CTA (~5.4s)
> Apostila e notebook no link na descrição. Até a próxima.

---

## Notas de produção
- TTS: pt-BR-AntonioNeural, rate=+15%
- Cores: #58A6FF, #7EE787, #F0883E, #BC8CFF
- Fonte: JetBrains Mono
- Sem fade-out entre cenas
- Forma segue função: cada elemento visual serve a um propósito