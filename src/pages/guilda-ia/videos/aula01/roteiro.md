# Roteiro: Aula 01 — Nomenclaturas de IA

## Estrutura: 8 cenas, ~95s

| Cena | Conteúdo | Duração Est. |
|------|----------|-------------|
| 1 | Hook: Confusão de termos | ~12s |
| 2 | IA: o campo geral | ~13s |
| 3 | LLM: o modelo de linguagem | ~15s |
| 4 | O que LLM NÃO faz | ~10s |
| 5 | RAG: busca + geração | ~15s |
| 6 | Agente: LLM + ferramentas | ~15s |
| 7 | Resumo: hierarquia visual | ~10s |
| 8 | CTA: roadmap e próximo passo | ~12s |

---

## Cena 1 — Hook (~12s)

**Animação:** Quatro caixas (IA, LLM, RAG, Agente) surgem embaralhadas no centro, depois se organizam em coluna com cores distintas.

**Narração:**
> Se você já ouviu alguém falar "IA" pra descrever um chatbot, ou "RAG" como se fosse um modelo... você não tá sozinho. Esses quatro termos — IA, LLM, RAG e Agente — vivem sendo usados como se fossem a mesma coisa. E não são. Entender a diferença é o primeiro passo pra conseguir construir qualquer coisa com essa tecnologia.

---

## Cena 2 — IA: o campo geral (~13s)

**Animação:** Título "IA" grande surge. Abaixo, três ícones surgem sequencialmente: spam filter, xadrez, ChatGPT, cada um com label "IA". Destaque: contorno brilhante ao redor de tudo indicando que é o "guarda-chuva".

**Narração:**
> Inteligência Artificial é o nome do campo. Qualquer sistema que faz algo "inteligente" é IA. O filtro de spam do seu email? IA. Um motor de xadrez? IA. O ChatGPT? Também IA. É o guarda-chuva que cobre tudo — desde regras simples dos anos 50 até os modelos de bilhões de parâmetros de hoje.

---

## Cena 3 — LLM: o modelo de linguagem (~15s)

**Animação:** Dentro da caixa "IA", surge uma sub-caixa "LLM". Texto "prevê próxima palavra". Quatro capacidades aparecem como tags: Tool Calling, Raciocínio, Contexto Longo, Multimodalidade. Diagrama simplificado: input de texto → modelo → output de texto.

**Narração:**
> LLM é um tipo de IA — um modelo treinado pra prever a próxima palavra. É o que está por trás do ChatGPT, do Claude, do Gemini. Pra quem constrói, o que importa são quatro capacidades: tool calling, que é o modelo chamar ferramentas externas. Raciocínio, que é pensar passo a passo. Contexto longo, com janelas de mais de cem mil tokens. E multimodalidade, que é processar imagem, áudio e vídeo.

---

## Cena 4 — O que LLM NÃO faz (~10s)

**Animação:** Três "X" vermelhos surgem em vermelho: "Não calcula", "Não sabe seus dados", "Não tem memória". Exemplo visual: "234 x 987 = ?" → LLM responde "230.898" com sinal de alerta (pode estar errado).

**Narração:**
> Mas o LLM tem limites. Ele não calcula — se você perguntar 234 vezes 987, ele chuta. Ele não sabe fatos específicos — suas notas, seus documentos, nada disso tá no treinamento dele. E ele não tem memória de longo prazo — cada conversa começa do zero.

---

## Cena 5 — RAG: busca + geração (~15s)

**Animação:** Diagrama de fluxo em 4 passos: (1) Usuário pergunta → (2) Sistema busca em documentos → (3) Documentos + pergunta vão pro LLM → (4) LLM responde. Dois exemplos lado a lado: "Sem RAG" (LLM: "Não sei") e "Com RAG" (LLM: "2025").

**Narração:**
> RAG é a técnica que resolve esse problema de "o LLM não sabe". Funciona assim: o usuário faz uma pergunta, o sistema busca documentos relevantes, junta esses documentos com a pergunta, e passa tudo pro LLM gerar uma resposta fundamentada. Sem RAG, o modelo inventa. Com RAG, ele responde com base nos seus documentos.

---

## Cena 6 — Agente: LLM + ferramentas (~15s)

**Animação:** Diagrama central: caixa LLM no topo, três caixas de ferramentas abaixo (Calculadora, Busca Web, Arquivos), setas bidirecionais. Texto "Planeja → Executa → Responde". Comparação: LLM só fala vs Agente faz coisas.

**Narração:**
> Agente vai além. É um sistema que junta LLM com ferramentas e memória. O modelo de linguagem faz inferência, decide o que fazer, e usa ferramentas reais — uma calculadora, uma busca na web, acesso a arquivos. Um LLM puro só fala. Um agente fala e faz. É a diferença entre um consultor e um assistente que executa.

---

## Cena 7 — Resumo: hierarquia visual (~10s)

**Animação:** Diagrama de conjuntos (nested circles/boxes): IA (grande) ⊃ LLM (médio) → RAG usa LLM + documentos, Agente usa LLM + ferramentas + memória. Labels em cada camada.

**Narração:**
> Pra fixar: I. A. é o campo geral. LLM é um tipo de I. A. Já o RAG, usa o LLM junto com documentos. E o Agente usa LLM mais ferramentas mais memória. Quanto mais específico o termo, mais componentes estão envolvidos.

---

## Cena 8 — CTA: roadmap (~12s)

**Animação:** Timeline horizontal: Semana 1 (conceitos) → Semana 2-3 (prompting, Python) → Semana 4-5 (agente, ferramentas) → Semana 8 (RAG) → Semana 9-10 (agente completo). URL: luksamuk.codes/pages/guilda-ia com destaque.

**Narração:**
> Ao longo da Guilda, vamos cobrir tudo isso na prática. Da semana um aos conceitos, até a semana dez com um agente completo. O material tá no site, gratuito. Comece pelo começo.