# Roteiro Revisado: Vetores e Similaridade de Cosseno

## Estrutura Final (8 cenas, ~73s)

---

## Cena 1: O que são embeddings? (~10s)

**Animação:** Palavra "gato" → seta → vetor "[0.23, -0.45, 0.87, ...]"

**Narração:**
> "Um embedding é uma lista de números que representa o significado de algo. Palavras, imagens, sons — tudo pode virar um vetor de centenas de dimensões."

---

## Cena 2: Visualizando em 2D (~8s)

**Animação:** Plano cartesiano, vetor surgindo no círculo unitário

**Narração:**
> "Na prática, embeddings têm centenas de dimensões. Mas para visualizar, vamos truncar para apenas duas: um ponto no plano, uma seta saindo da origem."

---

## Cena 3: Círculo Unitário (~10s)

**Animação:** Círculo unitário, vetor rotacionando, cosseno aparecendo como projeção

**Narração:**
> "O círculo unitário é sua referência. Todo vetor normalizado fica aqui. O cosseno do ângulo é a projeção no eixo X: um número entre menos um e um."

---

## Cena 4: Vetor e Projeção (~10s)

**Animação:** Vetor único, linha tracejada vertical até o eixo X, valor "cos(θ)" aparecendo

**Narração:**
> "Quando o vetor aponta para cima, cosseno é positivo. Aponta para baixo, cosseno negativo. Quanto mais próximo da horizontal, maior a magnitude."

---

## Cena 5: Dois Vetores e o Ângulo (~10s)

**Animação:** Dois vetores saindo da origem, arco de ângulo entre eles

**Narração:**
> "Para similaridade, comparamos dois vetores. O ângulo entre eles revela tudo. Ângulo pequeno: semelhantes. Ângulo grande: diferentes."

---

## Cena 6: Vetores Opostos (~10s)

**Animação:** Dois vetores apontando direções opostas, ângulo de 180°

**Narração:**
> "Direções opostas: ângulo de cento e oitenta graus. Cosseno menos um. Significados opostos, como rei e rainha, sim e não. Quanto menor o ângulo, maior a similaridade."

---

## Cena 7: Fórmula Matemática (~15s)

**Animação:** Fórmula surgindo: cos(θ) = (A·B) / (|A||B|)

**Narração:**
> "Matematicamente: cosseno de teta igual ao produto escalar dividido pelo produto das magnitudes. Magnitudes normalizadas: sempre um. Então o cosseno captura apenas a direção, não o tamanho."

---

## Cena 8: Resumo Final (~10s)

**Animação:** Diagrama mostrando três vetores: semelhantes (ângulo pequeno), ortogonais (ângulo reto), opostos (ângulo raso)

**Narração:**
> "Então lembre: similaridade de cosseno captura relação semântica. Não importa o tamanho, importa a direção. Vetores próximos são semelhantes. Ortogonais são independentes. Opostos são opostos mesmo, como rei e rainha."

---

## TOTAL: ~83 segundos

**Mudanças em relação ao original:**
1. Removida repetição na cena 1 (intro duplicada)
2. Cenas didáticas integradas no fluxo (não no final)
3. Cada conceito aparece UMA vez
4. Progressão: conceito → visual → matemática → resumo
5. Removidas cenas redundantes (6 e 11 eram resumos duplicados)