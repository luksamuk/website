# Roteiro — Mini Aula: Python Mínimo (Semana 03)

Duração alvo: ~90 segundos
Voz: pt-BR-AntonioNeural (Edge TTS)
Formato: 1080p60, dark theme

## Cena 1: Hook (~12s)

**Visual:** Logo "GUILDA DE IA" + badge "AULA 03". Texto "Python mínimo" surge com typewriter. Abaixo, três caixas colapsam num `>>>` de terminal: "IA", "LLM", "Agente" — e uma seta aponta pro `import` do Python.

**Narração:**
> Python mínimo. O essencial pra começar com IA. Se você vai usar uma API, montar um agente ou fazer RAG — tudo começa com Python. Sem Python, sem agente.

---

## Cena 2: Variáveis e Tipos (~14s)

**Visual:** Terminal animado. Quatro linhas surgem em sequência:
- `nome = "Maria"` → label "string" em verde
- `idade = 25` → label "int" em laranja
- `altura = 1.70` → label "float" em roxo
- `estudante = True` → label "bool" em ciano
F-string animada: `f"{nome} tem {idade} anos"` — valores substituem as chaves.

**Narração:**
> Variáveis guardam valores. Texto é string, inteiro é int, decimal é float, verdadeiro ou falso é bool. E f-strings são a forma mais prática de juntar texto com variáveis: coloque a variável dentro de chaves com um F na frente da string.

---

## Cena 3: Listas e Dicionários (~14s)

**Visual:** Esquerda: lista `["maçã", "banana", "laranja"]` com índices `[0]`, `[1]`, `[2]` aparecendo em laranja. `.append("uva")` adiciona elemento animado. Direita: dict `{"nome": "João", "idade": 30}` com chaves em verde e valores em branco.

**Narração:**
> Lista é uma sequência ordenada — acesse por índice, adicione com append. Dicionário é pares de chave e valor — acesse por nome, não por posição. Em APIs, quase tudo que você recebe é um dicionário gigante.

---

## Cena 4: Funções (~12s)

**Visual:** Diagrama caixa-preta: `def saudar(nome, saudacao="Olá")` no topo com setas de input. Duas setas de saída: `saudar("Maria")` → `"Olá, Maria!"` e `saudar("João", "Oi")` → `"Oi, João!"`. Parâmetro default `saudacao="Olá"` destacado em laranja.

**Narração:**
> Funções são blocos reutilizáveis. Defina uma vez, chame quantas vezes quiser. Parâmetros com valor padrão são opcionais. E em APIs, toda chamada é uma função: você passa parâmetros e recebe um resultado.

---

## Cena 5: Condicionais e Loops (~14s)

**Visual:** Esquerda: fluxograma `if/elif/else` com setas coloridas (verde pra "maior de idade", amarelo pra "adolescente", vermelho pra "criança"). Direita: `for fruta in frutas` com cada item surgindo. Abaixo: `while count < 3` com contador `0 → 1 → 2 → 3` (para).

**Narração:**
> If, elif, else: o programa toma decisões. For percorre uma lista item por item. While repete enquanto a condição for verdadeira. Com essas três estruturas, você já consegue qualquer lógica.

---

## Cena 6: Python + IA — a ponte (~16s)

**Visual:** Diagrama em 3 camadas verticais: (1) Python no topo, (2) API no meio com seta bidirecional rotulada "JSON", (3) LLM embaixo. JSON animado trafega pela seta: `{"role": "user", "content": "Oi"}` desce, `{"role": "assistant", "content": "Olá!"}` sobe. Badge "Próxima aula: APIs de LLM" surge no canto.

**Narração:**
> Agora a conexão. Python sozinho processa dados. Mas quando você usa uma API, o Python manda um JSON pro modelo e recebe uma resposta. O modelo é o cérebro, a API é a ponte, e Python é a ferramenta que você usa pra construir tudo. Na próxima aula, vamos fazer essa ponte funcionar de verdade.

---

## Cena 7: CTA (~10s)

**Visual:** Badge "AULA 03" surge. Badge "Apostila + Notebook → luksamuk.codes" aparece abaixo. URLs: `luksamuk.codes/pages/guilda-ia` e link do Colab. Logo GUILDA DE IA fecha.

**Narração:**
> Apostila, slides e notebook no link na descrição. Pra próxima aula, traz seu Python básico — porque vamos conectar tudo com APIs. Até lá!

---

## TOTAL: ~92 segundos

**Notas de produção:**
- Usar Manim Community para animações de código/terminal
- Cores seguir paleta Guilda de IA (#58A6FF, #7EE787, #F0883E, #BC8CFF)
- TTS: pt-BR-AntonioNeural
- Thumbnail: `thumbnail_aula03.png` (tipo mini, com equação)