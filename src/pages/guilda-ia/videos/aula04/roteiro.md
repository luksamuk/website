# Mini-Aula S04: Python + API de LLM — Roteiro (v2)

**Duração:** ~3:58
**Formato:** Manim + TTS Edge (pt-BR-AntonioNeural)
**YouTube:** https://youtu.be/2gRTEguprC8
**Thumbnail:** `guilda-thumb.py --type mini --number 04 --subtitle "Python + API de LLM" --tags "Variáveis/Listas/Dicts:SECONDARY:Funções/Loops:ACCENT:APIs de LLM:PURPLE" --equation "requests:SECONDARY >JSON→LLM:ACCENT >memória:PURPLE"`

---

## Pronúncia TTS (SOMENTE no texto de narração, NUNCA nos slides/Manim)

| Termo | Slide (visual) | Narração (TTS) |
|-------|---------------|----------------|
| API | API | A-P-I |
| LLM | LLM | L-L-M |
| JSON | JSON | Jêi-son |
| HTTP | HTTP | H-T-T-P |
| URL | URL | URL |
| requests | requests | requestes |
| OpenAI | OpenAI | Open ei-ái |
| LM Studio | LM Studio | L-M Studio |
| Ollama | Ollama | O Lhama |
| llama.cpp | llama.cpp | Lhama ponto cê-pê-pê |
| ik_llama.cpp | ik_llama.cpp | I-Cá Lhama ponto cê-pê-pê |
| llama-server | llama-server | Lhama sérver |
| Gemini | Gemini | Geminái |
| genai | genai | gen-ei-ái |
| generate_content | generate_content | generêite content |
| AI Studio | AI Studio | ei-ái Studio |
| VRAM | VRAM | vê-RAM |
| RAM | RAM | R-A-M |
| tokens | tokens | tokens |
| Qwen | Qwen | Quen |

---

## Cena 1 — Abertura (~10s)

**Visual:** Logo "GUILDA DE IA" grande no topo com glow azul. Badge laranja "AULA 04" abaixo. Subtítulo "Python + API de LLM" surge com typewriter. Três badges outline surgem embaixo: "Fundamentos" (verde), "Python / APIs" (laranja), "RAG / Agentes" (roxo).

**Narração (TTS):**
> Guil-da de I.A. Aula quatro. Python e A-P-I de L-L-M.

**Nota fonética TTS:**
> Guil-da de I-A. Aula quatro. Python e A-P-I de L-L-M.

---

## Cena 2 — Hook: Pra que Python? (~12s)

**Visual:** "Pra que Python?" em azul grande. Setas: "Python" (verde) → "API" (laranja) → "LLM" (roxo). Texto "controlar" pulsa em laranja.

**Narração (TTS):**
> Pra que Python, se o ChatGPT já responde tudo? Porque você quer controlar o modelo. E a ponte entre código e inteligência é a A-P-I.

**Nota fonética TTS:**
> Pra que Python, se o ChatGPT já responde tudo? Porque você quer controlar o modelo. E a ponte entre código e inteligência é a A-P-I.

---

## Cena 3 — API = Garçom (~12s)

**Visual:** Diagrama: Código (verde) → seta "JSON ▶" → API (laranja) → LLM (roxo). Badge embaixo: "Universal: Gemini, Ollama, OpenAI"

**Narração (TTS):**
> A A-P-I de L-L-M funciona como um garçom. Você manda um pedido em Jêi-son, a cozinha prepara, e volta como Jêi-son. Muda a URL, muda o formato, mas o conceito é universal. Entender H-T-T-P é entender todas as A-P-Is de L-L-M.

**Nota fonética TTS:**
> A A-P-I de L-L-M funciona como um garçom. Você manda um pedido em Jêi-son, a cozinha prepara, e volta como Jêi-son. Muda a URL, muda o formato, mas o conceito é universal. Entender H-T-T-P é entender todas as A-P-Is de L-L-M.

---

## Cena 4 — Código: requests.post() (~16s)

**Visual:** Bloco de código Python estilizado (syntax highlight):

```python
response = requests.post(
    url,
    json={
        "model": "gemma4:e2b",
        "messages": [
            {"role": "system", "content": "Responda em português."},
            {"role": "user", "content": "Qual a capital de MG?"},
        ],
    },
    timeout=120,
)
print(response.json()["choices"][0]["message"]["content"])
```

Badge no topo: "Um único padrão H-T-T-P" (laranja outline)

**Narração (TTS):**
> É isso. Um requestes.post, uma URL, um Jêi-son com modelo e mensagens. Qualquer A-P-I de L-L-M usa esse padrão. Na apostila tem mais detalhes, incluindo tratamento de erros como 401 e 429.

**Nota fonética TTS:**
> É isso. Um requestes.post, uma URL, um Jêi-son com modelo e mensagens. Qualquer A-P-I de L-L-M usa esse padrão. Na apostila tem mais detalhes, incluindo tratamento de erros como 401 e 429.

---

## Cena 5 — Cloud: Gemini + Ollama (~14s)

**Visual:** Split-screen com duas colunas. Esquerda ☁️ "Gemini" com badges "100+ tok/s", "Grátis com limites", "Precisa de internet", "API key necessária". Direita 🏠 "Ollama" com badges "80 tok/s", "100% grátis", "Privacidade total", "Sem internet*". Badge central: "Mesmo padrão HTTP".

**Narração (TTS):**
> Cloud com o Gemini: setup rápido, mais de 100 tokens por segundo, grátis com limites, precisa de A-P-I key. Local com o Ô-lhama: privacidade total, sem internet, 100 por cento grátis. Comece pelo Gemini, depois experimente o Ô-lhama.

**Nota fonética TTS:**
> Cloud com o Gemini: setup rápido, mais de 100 tokens por segundo, grátis com limites, precisa de A-P-I key. Local com o Ô-lhama: privacidade total, sem internet, 100 por cento grátis. Comece pelo Gemini, depois experimente o Ô-lhama.

---

## Cena 6 — Ollama no Colab (~14s)

**Visual:** Terminal estilizado com 3 linhas de destaque:
- `!nvidia-smi` → badge "GPU T4" (verde)
- `!ollama pull qwen3.5:4b` → badge "~2.7 GB" (laranja)
- `OLLAMA_KEEP_ALIVE = -1` → badge "não descarrega" (roxo)

Badge warning: "⚠️ Warm up: ~2-3 min na 1ª requisição"

**Narração (TTS):**
> No Google Colab com GPU T4, você também consegue rodar o Ô-lhama. Baixe o modelo, espere o warm-up de dois a três minutos, e pronto: L-L-M local e gratuito. Mas lembre-se de definir o parâmetro KEEP_ALIVE negativo um para o modelo não ser descarregado da memória de vídeo.

**Nota fonética TTS:**
> No Google Colab com GPU T4, você também consegue rodar o Ô-lhama. Baixe o modelo, espere o warm-up de dois a três minutos, e pronto: L-L-M local e gratuito. Mas lembre-se de definir o parâmetro KEEP_ALIVE menos um para o modelo não ser descarregado da memória de vídeo.

---

## Cena 7 — System Prompt + Chat com Memória (~14s)

**Visual:** Duas partes:
1. Topo: Pill laranja "Você é um tutor de Python" com label "system prompt"
2. Abaixo: Lista crescendo: {role: "system"} → .append() {role: "user"} → .append() {role: "assistant"} → .append() {role: "user"}
3. Insight em roxo: "O LLM não lembra. Você gerencia."

**Narração (TTS):**
> System prompt define a personalidade sem mandar mensagem. Bota "Você é um tutor de Python" e o modelo já responde diferente. Chat com memória é uma lista que cresce: system, user, assistente, user. Cada chamada manda o histórico inteiro. O L-L-M não lembra de nada. Quem gerencia a memória é você, no seu código.

**Nota fonética TTS:**
> System prompt define a personalidade sem mandar mensagem. Bota "Você é um tutor de Python" e o modelo já responde diferente. Chat com memória é uma lista que cresce: system, user, assistente, user. Cada chamada manda o histórico inteiro. O L-L-M não lembra de nada. Quem gerencia a memória é você, no seu código.

---

## Cena 8 — Alternativas: LM Studio, llama.cpp (~20s)

**Visual:** Três cards side-by-side simplificados:

Card 1 (verde): "LM Studio" — "Interface gráfica" — "Lhama ponto cê-pê-pê por baixo" — "Serve API Open-A-I compatible" — "Developer mode p/ configs"

Card 2 (laranja): "llama.cpp" — "Compilado do código-fonte" — "Melhor opção p/ hardware consumidor" — "Sempre atualizado"

Card 3 (roxo): "ik_llama.cpp" — "I-Cá Lhama ponto cê-pê-pê" — "Pouca VRAM + boa performance" — "Contexto até 200K tokens" — "Usa RAM comum"

**Narração (TTS):**
> Se você tem dificuldade com console, o L-M Studio é uma alternativa entry-level com interface gráfica e controles refinados. Ligue o developer mode para ver todas as configurações. Ele usa Lhama ponto cê-pê-pê por baixo dos panos e serve uma A-P-I compatível com a da Open-A-I. Para hardware de consumidor, compilar o Lhama ponto cê-pê-pê direto do código-fonte é sempre a melhor opção. E se você tem pouca VRAM mas quer boa performance, o I-Cá Lhama ponto cê-pê-pê permite rodar modelos com mais contexto usando RAM comum.

**Nota fonética TTS:**
> Se você tem dificuldade com console, o L-M Studio é uma alternativa entry-level com interface gráfica e controles refinados. Ligue o developer mode para ver todas as configurações. Ele usa Lhama ponto cê-pê-pê por baixo dos panos e serve uma A-P-I compatível com a da Open-A-I. Para hardware de consumidor, compilar o Lhama ponto cê-pê-pê direto do código-fonte é sempre a melhor opção. E se você tem pouca VRAM mas quer boa performance, o I-Cá Lhama ponto cê-pê-pê permite rodar modelos com mais contexto usando RAM comum.

---

## Cena 9 — Código: chat.py unificado (~14s)

**Visual:** Bloco de código simplificado (syntax highlight) com 3 blocos comentados:

```python
# Ollama (padrão)
URL = "http://localhost:11434/v1/chat/completions"

# LM Studio
# URL = "http://localhost:1234/v1/chat/completions"

# llama-swap
# URL = "http://127.0.0.1:12434/v1/chat/completions"

response = requests.post(URL, json={
    "model": "qwen3.5:4b",
    "messages": [...],
}, timeout=120)
```

Badge âmbar: "Só muda a URL"

**Narração (TTS):**
> Independente de qual dessas três opções você está usando — Ô-lhama, L-M Studio ou Lhama sérver — o código é o mesmo. Você faz uma requisição H-T-T-P normal com requestes.post. Só muda a URL. Todas exportam uma A-P-I compatível com a da Open-A-I.

**Nota fonética TTS:**
> Independente de qual dessas três opções você está usando, Ô-lhama, L-M Studio ou Lhama sérver, o código é o mesmo. Você faz uma requisição H-T-T-P normal com requestes.post. Só muda a URL. Todas exportam uma A-P-I compatível com a da Open-A-I.

---

## Cena 10 — CTA: Próxima aula (~10s)

**Visual:** Badge laranja "AULA 04". Texto "Apostila + Notebook" (branco). URL "luksamuk.codes/pages/guilda-ia" (azul). Texto "Próxima aula: Estrutura de um Agente" (laranja). Logo grande "GUILDA DE IA" (azul com glow) embaixo.

**Narração (TTS):**
> Apostila e notebook no link na tela. Semana que vem: estrutura de um agente. Guil-da de I.A.

**Nota fonética TTS:**
> Apostila e notebook no link na tela. Semana que vem: estrutura de um agente. Guil-da de I-A.

---

**TOTAL estimado:** ~136s (~2min16s)

---

## Resumo das mudanças da v1 pra v2

1. **Adicionada Cena 1 (Abertura)** com logo GUILDA DE IA, badge e subtítulo — seguindo padrão da Aula 03
2. **Adicionada Cena 4 com código Python real** (`requests.post()`) — mostra o snippet completo
3. **Adicionada Cena 6 (Ollama no Colab)** — GPU T4, warm-up, KEEP_ALIVE
4. **Adicionada Cena 8 (Alternativas)** — LM Studio, llama.cpp, ik_llama.cpp com pronúncias no TTS
5. **Adicionada Cena 9 (chat.py unificado)** — código real com 3 backends comentados
6. **Adicionada Cena 10 (CTA)** — link, próxima aula, logo GUILDA DE IA
7. **Corrigidos TODOS os foneticismos** — "API" (não "A.P.I."), "LLM" (não "L.L.M."), "JSON" (não "Jêi-son") nos slides. Versões fonéticas SOMENTE na narração TTS.
8. **Ollama** pronunciado como "Ô-lhama" no TTS
9. **llama.cpp** pronunciado como "Lhama ponto cê-pê-pê" no TTS
10. **ik_llama.cpp** pronunciado como "I-Cá Lhama ponto cê-pê-pê" no TTS
11. **Referência à apostila** para tratamento de erros (401, 429)