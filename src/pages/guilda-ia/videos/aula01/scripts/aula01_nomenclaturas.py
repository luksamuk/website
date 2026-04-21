#!/usr/bin/env python3
"""
Aula 01 — Nomenclaturas de IA (IA, LLM, RAG, Agente)
Vídeo didático de revisão da Aula 01 da Guilda de IA

TIMINGS BASEADOS NOS ÁUDIOS REAIS (v2 — pronúncia corrigida):
- Cena 1 (Hook): 23.6s áudio → 25.6s vídeo
- Cena 2 (IA): 25.8s áudio → 27.8s vídeo
- Cena 3 (LLM): 30.9s áudio → 32.9s vídeo
- Cena 4 (Limites): 21.7s áudio → 23.7s vídeo
- Cena 5 (RAG): 23.8s áudio → 25.8s vídeo
- Cena 6 (Agente): 25.7s áudio → 27.7s vídeo
- Cena 7 (Resumo): 19.6s áudio → 21.6s vídeo
- Cena 8 (CTA): 14.5s áudio → 16.5s vídeo

TOTAL: ~199s (~3min19s)

CORREÇÕES v2:
- Cena 2: exemplos na diagonal dentro do retângulo (Spam Filter canto sup. esq., ChatGPT canto inf. dir.)
- Cena 4: removido fadeout implícito, objetos ficam visíveis até o final
- Cena 5: removido fadeout implícito, objetos ficam visíveis até o final
- Cena 6: setas duplas → seta ponta dupla única; removido fadeout implícito

Renderizar com:
source ~/manim-env/bin/activate
manim -qh aula01_nomenclaturas.py Scene1Hook Scene2IA Scene3LLM Scene4Limites Scene5RAG Scene6Agente Scene7Resumo Scene8CTA
"""

from manim import *
import math

# Paleta de cores (GitHub dark + cores suaves)
BG = "#0D1117"
PRIMARY = "#58A6FF"    # Azul suave
SECONDARY = "#7EE787"  # Verde suave
ACCENT = "#F0883E"     # Laranja âmbar
PURPLE = "#BC8CFF"     # Roxo
PINK = "#FF9CCE"       # Rosa suave
RED = "#FF7B72"        # Vermelho suave
WHITE = "#E6EDF3"      # Branco suave
GRAY = "#8B949E"       # Cinza para textos secundários
MONO = "JetBrains Mono"


class Scene1Hook(Scene):
    """
    Hook: Confusão de termos.
    Áudio: 23.6s
    """
    def construct(self):
        self.camera.background_color = BG

        # Título provocativo
        titulo = Text("IA = LLM = RAG = Agente?",
                      font_size=40, color=RED, font=MONO)
        titulo.to_edge(UP, buff=0.5)

        # Quatro caixas embaralhadas
        termos = [
            ("IA", PRIMARY),
            ("LLM", SECONDARY),
            ("RAG", ACCENT),
            ("Agente", PURPLE),
        ]

        caixas = VGroup()
        labels = VGroup()
        for nome, cor in termos:
            box = Square(side_length=1.0, color=cor, stroke_width=2)
            box.set_fill(cor, opacity=0.15)
            label = Text(nome, font_size=24, color=cor, font=MONO)
            label.move_to(box.get_center())
            caixas.add(box)
            labels.add(label)

        # Posicionar embaralhado
        positions_shuffled = [
            LEFT * 2.5 + UP * 0.4,
            RIGHT * 1.8 + UP * 0.6,
            LEFT * 0.5 + DOWN * 0.8,
            RIGHT * 2.5 + DOWN * 0.3,
        ]
        for i, (box, label) in enumerate(zip(caixas, labels)):
            box.move_to(positions_shuffled[i])
            label.move_to(box.get_center())

        grupo_embaralhado = VGroup()
        for box, label in zip(caixas, labels):
            grupo_embaralhado.add(VGroup(box, label))

        # Posições organizadas (em linha)
        positions_sorted = [
            LEFT * 3 + DOWN * 0.5,
            LEFT * 1 + DOWN * 0.5,
            RIGHT * 1 + DOWN * 0.5,
            RIGHT * 3 + DOWN * 0.5,
        ]

        # Animações
        self.play(Write(titulo), run_time=1.5)

        for g in grupo_embaralhado:
            self.play(FadeIn(g), run_time=0.4)

        self.wait(2)

        # "=" entre elas
        equals = []
        for i in range(3):
            eq = Text("=", font_size=30, color=RED, font=MONO)
            eq.move_to((positions_shuffled[i] + positions_shuffled[i+1]) / 2)
            equals.append(eq)

        for eq in equals:
            self.play(FadeIn(eq), run_time=0.3)

        self.wait(2)

        # Remover = e reorganizar
        self.play(FadeOut(VGroup(*equals)), run_time=0.5)

        anims = []
        for i, (box, label) in enumerate(zip(caixas, labels)):
            target = positions_sorted[i]
            anims.append(box.animate.move_to(target))
            anims.append(label.animate.move_to(target))

        self.play(*anims, run_time=2)

        # "≠" entre elas
        not_equals = []
        for i in range(3):
            ne = Text("≠", font_size=30, color=SECONDARY, font=MONO)
            ne.move_to((positions_sorted[i] + positions_sorted[i+1]) / 2)
            not_equals.append(ne)

        for ne in not_equals:
            self.play(FadeIn(ne), run_time=0.3)

        self.wait(2)

        # Qual a diferença?
        pergunta = Text("Qual a diferença?", font_size=36, color=ACCENT, font=MONO)
        pergunta.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(pergunta), run_time=1)

        # Hold (áudio 23.6s total)
        self.wait(10)

        # SEM fade out — cena 1 não tinha e ficou OK


class Scene2IA(Scene):
    """
    IA: o campo geral.
    Áudio: 25.8s (v2)
    """
    def construct(self):
        self.camera.background_color = BG

        # Título — IA grande no topo, com subtítulo ABAIXO dela
        titulo = Text("IA", font_size=72, color=PRIMARY, font=MONO)
        titulo.to_edge(UP, buff=0.4)

        subtitulo = Text("Inteligência Artificial", font_size=24, color=GRAY, font=MONO)
        subtitulo.next_to(titulo, DOWN, buff=0.3)

        # Label "o campo geral" abaixo do subtítulo, ANTES do retângulo
        campo_label = Text("O campo geral", font_size=22, color=PRIMARY, font=MONO)
        campo_label.next_to(subtitulo, DOWN, buff=0.5)

        # Retângulo do campo — ABAIXO do label, não o contendo
        campo_rect = Rectangle(
            width=10, height=3.5,
            color=PRIMARY, stroke_width=2,
            stroke_opacity=0.4,
            fill_color=PRIMARY, fill_opacity=0.03
        )
        campo_rect.next_to(campo_label, DOWN, buff=0.4)

        # Três exemplos DENTRO do retângulo, distribuídos na diagonal
        # Spam Filter no canto superior esquerdo, ChatGPT no canto inferior direito
        # Xadrez fica no centro
        exemplos = VGroup()
        items_data = [
            ("Spam Filter", GRAY),
            ("Xadrez", SECONDARY),
            ("ChatGPT", PRIMARY),
        ]

        labels_exemplos = VGroup()
        for nome, cor in items_data:
            label = Text(nome, font_size=22, color=cor, font=MONO)
            tag = Text("→ I.A.", font_size=16, color=PRIMARY, font=MONO)
            grupo = VGroup(label, tag)
            grupo.arrange(DOWN, buff=0.1)
            labels_exemplos.add(grupo)

        # Posições na diagonal dentro do retângulo
        # Spam Filter: canto sup. esq., Xadrez: centro, ChatGPT: canto inf. dir.
        diag_positions = [
            campo_rect.get_corner(UL) + DOWN * 0.7 + RIGHT * 1.2,
            campo_rect.get_center() + UP * 0.2,
            campo_rect.get_corner(DR) + UP * 0.7 + LEFT * 1.2,
        ]
        for i, grupo in enumerate(labels_exemplos):
            grupo.move_to(diag_positions[i])

        # Frase final ABAIXO do retângulo
        guarda = Text("O guarda-chuva que cobre tudo",
                      font_size=22, color=WHITE, font=MONO)
        guarda.next_to(campo_rect, DOWN, buff=0.5)

        # Animações
        self.play(Write(titulo), run_time=1)
        self.play(FadeIn(subtitulo), run_time=0.8)
        self.play(FadeIn(campo_label), run_time=0.6)
        self.play(FadeIn(campo_rect), run_time=1)

        for ex in labels_exemplos:
            self.play(FadeIn(ex), run_time=0.8)

        self.play(FadeIn(guarda), run_time=1)

        # Hold (áudio 25.8s)
        self.wait(16.8)


class Scene3LLM(Scene):
    """
    LLM: o modelo de linguagem.
    Áudio: 30.9s (v2)
    """
    def construct(self):
        self.camera.background_color = BG

        # Título — LLM grande no topo
        titulo = Text("LLM", font_size=64, color=SECONDARY, font=MONO)
        titulo.to_edge(UP, buff=0.4)

        subtitulo = Text("Large Language Model", font_size=22, color=GRAY, font=MONO)
        subtitulo.next_to(titulo, DOWN, buff=0.2)

        # Definição — "Prevê a próxima palavra" como texto destacado
        # NÃO como subtítulo flutuante — como elemento separado abaixo
        definicao = Text("Prevê a próxima palavra",
                        font_size=30, color=WHITE, font=MONO)
        definicao.next_to(subtitulo, DOWN, buff=0.6)

        # Indicador: "LLM é um tipo de IA" — antes do diagrama
        tipo = Text("Um tipo de IA", font_size=20, color=SECONDARY, font=MONO)
        tipo.next_to(definicao, DOWN, buff=0.5)

        # Quatro capacidades como tags — organizadas em 2x2 pra caber
        caps_group = VGroup()
        capacidades = [
            ("Tool Calling", ACCENT, "Chama ferramentas externas"),
            ("Raciocínio", PURPLE, "Pensa passo a passo"),
            ("Contexto Longo", PRIMARY, "100K+ tokens"),
            ("Multimodalidade", PINK, "Imagem, áudio, vídeo"),
        ]

        caps_row1 = VGroup()
        caps_row2 = VGroup()

        for i, (nome, cor, desc) in enumerate(capacidades):
            tag_bg = Rectangle(width=3.8, height=0.7, color=cor, stroke_width=2)
            tag_bg.set_fill(cor, opacity=0.15)
            tag_text = Text(f"{nome}", font_size=18, color=cor, font=MONO)
            tag_text.move_to(tag_bg.get_center())
            item = VGroup(tag_bg, tag_text)

            if i < 2:
                caps_row1.add(item)
            else:
                caps_row2.add(item)

        caps_row1.arrange(RIGHT, buff=0.5)
        caps_row2.arrange(RIGHT, buff=0.5)
        caps_group.add(caps_row1, caps_row2)
        caps_group.arrange(DOWN, buff=0.4)
        caps_group.next_to(tipo, DOWN, buff=0.5)

        # Descrições posicionadas abaixo das tags
        desc1a = Text("Chama ferramentas externas", font_size=14, color=ACCENT, font=MONO)
        desc1a.next_to(caps_row1[0], DOWN, buff=0.15)

        desc1b = Text("Pensa passo a passo", font_size=14, color=PURPLE, font=MONO)
        desc1b.next_to(caps_row1[1], DOWN, buff=0.15)

        desc2a = Text("100K+ tokens", font_size=14, color=PRIMARY, font=MONO)
        desc2a.next_to(caps_row2[0], DOWN, buff=0.15)

        desc2b = Text("Imagem, áudio, vídeo", font_size=14, color=PINK, font=MONO)
        desc2b.next_to(caps_row2[1], DOWN, buff=0.15)

        # Animações
        self.play(Write(titulo), run_time=1)
        self.play(FadeIn(subtitulo), FadeIn(definicao), run_time=1)
        self.play(FadeIn(tipo), run_time=0.6)

        # Revelar capacidades
        for cap in caps_row1:
            self.play(FadeIn(cap), run_time=0.7)

        # Descrições da row 1
        self.play(FadeIn(desc1a), FadeIn(desc1b), run_time=0.5)

        for cap in caps_row2:
            self.play(FadeIn(cap), run_time=0.7)

        # Descrições da row 2
        self.play(FadeIn(desc2a), FadeIn(desc2b), run_time=0.5)

        # Hold (áudio 30.9s)
        self.wait(20.8)


class Scene4Limites(Scene):
    """
    O que LLM NÃO faz.
    Áudio: 21.7s (v2)
    """
    def construct(self):
        self.camera.background_color = BG

        # Título
        titulo = Text("O que LLM NÃO faz", font_size=36, color=RED, font=MONO)
        titulo.to_edge(UP, buff=0.4)

        # Três limites em coluna vertical (não horizontal — mais legível)
        limites = VGroup()
        limit_items = [
            ("✗  Não calcula", "234 × 987 = ?  →  ele chuta", RED),
            ("✗  Não sabe seus dados", "Suas notas, documentos?  →  não tá no treino", ACCENT),
            ("✗  Não tem memória", "Cada conversa  →  começa do zero", PURPLE),
        ]

        for titulo_item, desc_item, cor in limit_items:
            grupo = VGroup()
            t = Text(titulo_item, font_size=24, color=cor, font=MONO)
            d = Text(desc_item, font_size=16, color=GRAY, font=MONO)
            grupo.add(t, d)
            grupo.arrange(DOWN, buff=0.15)
            limites.add(grupo)

        limites.arrange(DOWN, buff=0.8)
        limites.shift(UP * 0.3)

        # Animações
        self.play(Write(titulo), run_time=1.2)

        for limite in limites:
            self.play(FadeIn(limite), run_time=1)

        # Hold (áudio 21.7s, animações ~4.2s, wait = ~17.5s)
        # NÃO usar fadeout — objetos ficam visíveis até o final
        self.wait(17.5)


class Scene5RAG(Scene):
    """
    RAG: busca + geração.
    Áudio: 23.8s (v2)
    """
    def construct(self):
        self.camera.background_color = BG

        # Título
        titulo = Text("RAG", font_size=56, color=ACCENT, font=MONO)
        titulo.to_edge(UP, buff=0.4)

        subtitulo = Text("Retrieval Augmented Generation",
                         font_size=20, color=GRAY, font=MONO)
        subtitulo.next_to(titulo, DOWN, buff=0.15)

        # Diagrama de fluxo (4 passos) — em linha horizontal
        # Usar apenas texto, sem emojis
        passos_labels = [
            ("1. Pergunta", WHITE),
            ("2. Busca\n   documentos", PRIMARY),
            ("3. Documentos\n   + pergunta", SECONDARY),
            ("4. Resposta\n   fundamentada", ACCENT),
        ]

        passos = VGroup()
        for nome, cor in passos_labels:
            label = Text(nome, font_size=20, color=cor, font=MONO)
            passos.add(label)

        passos.arrange(RIGHT, buff=1.0)
        passos.shift(UP * 0.5)

        # Setas entre passos
        setas = VGroup()
        for i in range(len(passos) - 1):
            start = passos[i].get_right() + RIGHT * 0.15
            end = passos[i+1].get_left() + LEFT * 0.15
            seta = Arrow(start, end, color=GRAY, buff=0.1, stroke_width=2)
            setas.add(seta)

        # Comparação: Sem RAG vs Com RAG — em colunas verticais
        sem_rag = VGroup()
        sem_label = Text("Sem RAG:", font_size=22, color=RED, font=MONO)
        sem_q = Text('"Quando foi fundada a Liga?"', font_size=16, color=GRAY, font=MONO)
        sem_a = Text('→ "Não sei" ou inventa', font_size=16, color=RED, font=MONO)
        sem_rag.add(sem_label, sem_q, sem_a)
        sem_rag.arrange(DOWN, buff=0.2)

        com_rag = VGroup()
        com_label = Text("Com RAG:", font_size=22, color=SECONDARY, font=MONO)
        com_q = Text('"Quando foi fundada a Liga?"', font_size=16, color=GRAY, font=MONO)
        com_a = Text('→ Busca documento\n→ "2025" (correto)', font_size=16, color=SECONDARY, font=MONO)
        com_rag.add(com_label, com_q, com_a)
        com_rag.arrange(DOWN, buff=0.2)

        comparacao = VGroup(sem_rag, com_rag)
        comparacao.arrange(RIGHT, buff=2.5)
        comparacao.shift(DOWN * 2.0)

        # Animações
        self.play(Write(titulo), FadeIn(subtitulo), run_time=1)

        # Revelar passos
        for i, passo in enumerate(passos):
            self.play(FadeIn(passo), run_time=0.7)
            if i < len(setas):
                self.play(Create(setas[i]), run_time=0.3)

        self.play(FadeIn(sem_rag), run_time=1)
        self.wait(1)
        self.play(FadeIn(com_rag), run_time=1)

        # Hold (áudio 23.8s, animações ~7s, wait = ~16.8s)
        # NÃO usar fadeout — objetos ficam visíveis até o final
        self.wait(16.8)


class Scene6Agente(Scene):
    """
    Agente: LLM + ferramentas.
    Áudio: 25.7s (v2)
    """
    def construct(self):
        self.camera.background_color = BG

        # Título
        titulo = Text("Agente", font_size=56, color=PURPLE, font=MONO)
        titulo.to_edge(UP, buff=0.4)

        subtitulo = Text("LLM + Ferramentas + Memória",
                         font_size=20, color=GRAY, font=MONO)
        subtitulo.next_to(titulo, DOWN, buff=0.15)

        # Diagrama central: LLM no topo, ferramentas abaixo
        llm_box = Square(side_length=1.4, color=SECONDARY, stroke_width=2)
        llm_box.set_fill(SECONDARY, opacity=0.15)
        llm_label = Text("LLM", font_size=24, color=SECONDARY, font=MONO)
        llm_label.move_to(llm_box.get_center())
        llm_grupo = VGroup(llm_box, llm_label)
        llm_grupo.shift(UP * 0.8)

        # Ferramentas
        ferramentas = VGroup()
        ferramenta_data = [
            ("Calculadora", ACCENT),
            ("Busca Web", PRIMARY),
            ("Arquivos", PURPLE),
        ]

        for nome, cor in ferramenta_data:
            box = Square(side_length=1.1, color=cor, stroke_width=2)
            box.set_fill(cor, opacity=0.15)
            label = Text(nome, font_size=16, color=cor, font=MONO)
            label.move_to(box.get_center())
            ferramentas.add(VGroup(box, label))

        ferramentas.arrange(RIGHT, buff=0.8)
        ferramentas.shift(DOWN * 1.2)

        # Setas PONTA DUPLA proporcionais (tip_length uniforme)
        setas = VGroup()
        for f in ferramentas:
            s = DoubleArrow(
                llm_box.get_bottom() + DOWN * 0.05,
                f.get_top() + UP * 0.05,
                color=GRAY, buff=0.1, stroke_width=1.5,
                tip_length=0.2
            )
            setas.add(s)

        # Fluxo
        fluxo = Text("Decide → Executa → Responde",
                     font_size=20, color=WHITE, font=MONO)
        fluxo.next_to(ferramentas, DOWN, buff=0.4)

        # Comparação (mais compacta, mais pra cima)
        comp = VGroup()
        llm_side = VGroup(
            Text("LLM puro:", font_size=18, color=GRAY, font=MONO),
            Text("Só fala", font_size=20, color=SECONDARY, font=MONO)
        )
        llm_side.arrange(DOWN, buff=0.1)

        agente_side = VGroup(
            Text("Agente:", font_size=18, color=GRAY, font=MONO),
            Text("Fala E faz", font_size=20, color=PURPLE, font=MONO)
        )
        agente_side.arrange(DOWN, buff=0.1)

        comp.add(llm_side, agente_side)
        comp.arrange(RIGHT, buff=2.0)
        comp.next_to(fluxo, DOWN, buff=0.3)

        # Animações
        self.play(Write(titulo), FadeIn(subtitulo), run_time=1)
        self.play(FadeIn(llm_grupo), run_time=1)

        for i, (f, s) in enumerate(zip(ferramentas, setas)):
            self.play(Create(s), FadeIn(f), run_time=0.8)

        self.play(FadeIn(fluxo), run_time=0.8)
        self.play(FadeIn(comp), run_time=0.8)

        # Hold (áudio 25.7s, animações ~4.6s, wait = ~21.1s)
        # NÃO usar fadeout — objetos ficam visíveis até o final
        self.wait(21.1)


class Scene7Resumo(Scene):
    """
    Resumo: hierarquia visual.
    Áudio: 19.6s (v3 — "Já o RAG" para separar pronúncia)
    """
    def construct(self):
        self.camera.background_color = BG

        # Título
        titulo = Text("Hierarquia", font_size=40, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.4)

        # Layout VERTICAL em vez de diagrama de conjuntos aninhados
        # Cada nível abaixo do anterior, indentado pra mostrar hierarquia

        # Nível 1: IA
        ia_label = Text("IA — o campo geral", font_size=28, color=PRIMARY, font=MONO)
        ia_label.shift(UP * 1.8)

        # Barra indicando "contém"
        ia_bar = Line(LEFT * 4, RIGHT * 4, color=PRIMARY, stroke_width=2, stroke_opacity=0.3)
        ia_bar.next_to(ia_label, DOWN, buff=0.3)

        # Nível 2: LLM (indentado)
        llm_label = Text("LLM — um tipo de IA", font_size=24, color=SECONDARY, font=MONO)
        llm_label.next_to(ia_bar, DOWN, buff=0.5)
        llm_label.shift(RIGHT * 0.5)  # indentado

        llm_bar = Line(LEFT * 3, RIGHT * 3, color=SECONDARY, stroke_width=2, stroke_opacity=0.3)
        llm_bar.next_to(llm_label, DOWN, buff=0.3)

        # Nível 3: RAG e Agente (lado a lado, indentados)
        rag_label = Text("RAG", font_size=24, color=ACCENT, font=MONO)
        rag_desc = Text("LLM + documentos", font_size=16, color=GRAY, font=MONO)
        rag_grupo = VGroup(rag_label, rag_desc)
        rag_grupo.arrange(DOWN, buff=0.1)
        rag_grupo.next_to(llm_bar, DOWN, buff=0.5)
        rag_grupo.shift(LEFT * 2.5 + RIGHT * 0.5)

        agente_label = Text("Agente", font_size=24, color=PURPLE, font=MONO)
        agente_desc = Text("LLM + ferramentas\n+ memória", font_size=16, color=GRAY, font=MONO)
        agente_grupo = VGroup(agente_label, agente_desc)
        agente_grupo.arrange(DOWN, buff=0.1)
        agente_grupo.next_to(llm_bar, DOWN, buff=0.5)
        agente_grupo.shift(RIGHT * 2.5 + RIGHT * 0.5)

        # Mensagem final
        msg = Text("Quanto mais específico, mais componentes",
                   font_size=22, color=ACCENT, font=MONO)
        msg.to_edge(DOWN, buff=0.6)

        # Animações — revelar de cima pra baixo
        self.play(FadeIn(titulo), run_time=0.8)
        self.play(FadeIn(ia_label), run_time=0.8)
        self.play(Create(ia_bar), run_time=0.5)
        self.play(FadeIn(llm_label), run_time=0.8)
        self.play(Create(llm_bar), run_time=0.5)
        self.play(FadeIn(rag_grupo), FadeIn(agente_grupo), run_time=1)
        self.play(FadeIn(msg), run_time=0.8)

        # Hold (áudio 19.6s)
        self.wait(11.5)


class Scene8CTA(Scene):
    """
    CTA: Roadmap e convite.
    Áudio: 14.5s (v2)
    """
    def construct(self):
        self.camera.background_color = BG

        # Título
        titulo = Text("Roadmap da Guilda", font_size=36, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.4)

        # Timeline horizontal
        blocos = [
            ("1", "Conceitos", PRIMARY),
            ("2-3", "Prompting\nPython", SECONDARY),
            ("4-5", "Agente\nFerramentas", ACCENT),
            ("8", "RAG", PURPLE),
            ("9-10", "Agente\nCompleto", PINK),
        ]

        # Linha da timeline
        line = Line(LEFT * 5, RIGHT * 5, color=GRAY, stroke_width=2)
        line.shift(DOWN * 0.3)

        pontos = VGroup()
        labels = VGroup()

        x_positions = [-4, -2, 0, 2, 4]

        for i, (semana, nome, cor) in enumerate(blocos):
            x = x_positions[i]
            ponto = Dot(point=[x, -0.3, 0], radius=0.12, color=cor)
            pontos.add(ponto)

            grupo_label = VGroup()
            label_semana = Text(semana, font_size=14, color=cor, font=MONO)
            label_nome = Text(nome, font_size=16, color=cor, font=MONO)
            grupo_label.add(label_semana, label_nome)
            grupo_label.arrange(DOWN, buff=0.1)
            grupo_label.move_to([x, 0.8, 0])
            labels.add(grupo_label)

        # URL
        url = Text("luksamuk.codes/pages/guilda-ia",
                   font_size=28, color=PRIMARY, font=MONO)
        url.shift(DOWN * 2.5)
        url_box = SurroundingRectangle(url, color=PRIMARY, buff=0.2, stroke_width=2)

        # Mensagem
        msg = Text("Gratuito. Comece pelo começo.",
                   font_size=22, color=SECONDARY, font=MONO)
        msg.next_to(url, DOWN, buff=0.5)

        # Animações
        self.play(FadeIn(titulo), run_time=0.8)
        self.play(Create(line), run_time=0.8)

        for i in range(len(blocos)):
            self.play(
                FadeIn(pontos[i]),
                FadeIn(labels[i]),
                run_time=0.5
            )

        self.play(FadeIn(url), Create(url_box), run_time=1.2)
        self.play(FadeIn(msg), run_time=0.8)

        # Hold (áudio 14.5s)
        self.wait(8.5)