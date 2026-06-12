#!/usr/bin/env python3
"""
Mini Aula 03: Python Mínimo — O essencial para começar com IA
VERSÃO 3: JetBrains Mono, pronúncias só no TTS, código com indentação visual

Renderizar:
    source ~/manim-env/bin/activate
    for s in Python_Scene1_Hook Python_Scene2_Variaveis Python_Scene3_ListasDicts Python_Scene4_Funcoes Python_Scene5_CondLoops Python_Scene6_Ponte Python_Scene7_CTA; do
        manim -qh python_minimo.py $s
    done
"""

from manim import *

# Paleta de cores Guilda de IA
BG = "#0D1117"
PRIMARY = "#58A6FF"
SECONDARY = "#7EE787"
ACCENT = "#F0883E"
PURPLE = "#BC8CFF"
WHITE = "#E6EDF3"
GRAY = "#8B949E"
DARK = "#161B22"

# FONTE MONO — JetBrains Mono (instalada no sistema)
MONO = "JetBrains Mono"
SANS = "DejaVu Sans"


# ============================================================================
# CENA 1: HOOK
# ============================================================================

class Python_Scene1_Hook(Scene):
    def construct(self):
        self.camera.background_color = BG

        titulo = Text("Python Mínimo", font_size=56, color=PRIMARY, font=MONO)
        titulo.shift(UP * 1.8)

        subtitulo = Text("O essencial para começar com IA", font_size=28, color=WHITE, font=MONO)
        subtitulo.next_to(titulo, DOWN, buff=0.4)

        ia = Text("IA", font_size=22, color=SECONDARY, font=MONO)
        llm = Text("LLM", font_size=22, color=ACCENT, font=MONO)
        agente = Text("Agente", font_size=22, color=PURPLE, font=MONO)
        caixas = VGroup(ia, llm, agente).arrange(DOWN, buff=0.3)
        caixas.shift(DOWN * 0.6 + LEFT * 3)

        seta = Arrow(LEFT, RIGHT, color=GRAY, stroke_width=2, max_tip_length_to_length_ratio=0.15)
        seta.shift(DOWN * 0.6)

        terminal = Rectangle(width=3.2, height=1.2, color=GRAY, stroke_width=1, fill_color=DARK, fill_opacity=0.9)
        terminal.shift(DOWN * 0.6 + RIGHT * 3)
        import_line = Text("import json", font_size=20, color=SECONDARY, font=MONO)
        import_line.move_to(terminal.get_center())

        self.play(FadeIn(titulo), run_time=1)
        self.play(FadeIn(subtitulo), run_time=0.8)
        for c in caixas:
            self.play(FadeIn(c), run_time=0.4)
        self.play(Create(terminal), FadeIn(import_line), Create(seta), run_time=1.2)
        self.wait(3)


# ============================================================================
# CENA 2: VARIÁVEIS (escrita normal, pronúncia só no áudio)
# ============================================================================

class Python_Scene2_Variaveis(Scene):
    def construct(self):
        self.camera.background_color = BG

        titulo = Text("Variáveis", font_size=36, color=PRIMARY, font=MONO)
        titulo.to_edge(UP, buff=0.4)

        lines = VGroup(
            VGroup(Text('nome = "Maria"', font_size=20, color=WHITE, font=MONO),
                   Text("string", font_size=14, color=SECONDARY, font=MONO)).arrange(RIGHT, buff=0.3),
            VGroup(Text("idade = 25", font_size=20, color=WHITE, font=MONO),
                   Text("int", font_size=14, color=ACCENT, font=MONO)).arrange(RIGHT, buff=0.3),
            VGroup(Text("altura = 1.70", font_size=20, color=WHITE, font=MONO),
                   Text("float", font_size=14, color=PURPLE, font=MONO)).arrange(RIGHT, buff=0.3),
            VGroup(Text("estudante = True", font_size=20, color=WHITE, font=MONO),
                   Text("bool", font_size=14, color=PRIMARY, font=MONO)).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        lines.shift(UP * 0.3)

        fstring_bg = Rectangle(width=7, height=0.7, color=ACCENT, stroke_width=2, fill_color=DARK, fill_opacity=0.8)
        fstring_bg.shift(DOWN * 1.8)
        fstring = Text('f"{nome} tem {idade} anos"', font_size=20, color=ACCENT, font=MONO)
        fstring.move_to(fstring_bg.get_center())

        result = Text('"Maria tem 25 anos"', font_size=16, color=SECONDARY, font=MONO)
        result.shift(DOWN * 2.8)

        self.play(FadeIn(titulo), run_time=0.5)
        for line in lines:
            self.play(FadeIn(line), run_time=0.5)
        self.play(Create(fstring_bg), FadeIn(fstring), run_time=1)
        self.play(FadeIn(result), run_time=0.6)
        self.wait(2)


# ============================================================================
# CENA 3: LISTAS E DICIONÁRIOS (append, APIs escritos normalmente)
# ============================================================================

class Python_Scene3_ListasDicts(Scene):
    def construct(self):
        self.camera.background_color = BG

        titulo = Text("Listas e Dicionários", font_size=32, color=PRIMARY, font=MONO)
        titulo.to_edge(UP, buff=0.3)

        lista_title = Text("Lista", font_size=22, color=SECONDARY, font=MONO)
        lista_title.shift(UP * 1 + LEFT * 3.5)
        lista_code = VGroup(
            Text('["maçã", "banana",', font_size=16, color=WHITE, font=MONO),
            Text(' "laranja"]', font_size=16, color=WHITE, font=MONO),
        ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
        lista_code.next_to(lista_title, DOWN, buff=0.2)

        indices = VGroup(
            Text("[0]", font_size=12, color=ACCENT, font=MONO),
            Text("[1]", font_size=12, color=ACCENT, font=MONO),
            Text("[2]", font_size=12, color=ACCENT, font=MONO),
        ).arrange(RIGHT, buff=0.8)
        indices.next_to(lista_code, DOWN, buff=0.15)

        append_line = Text('.append("uva")', font_size=16, color=SECONDARY, font=MONO)
        append_line.next_to(indices, DOWN, buff=0.2)

        dict_title = Text("Dicionário", font_size=22, color=PURPLE, font=MONO)
        dict_title.shift(UP * 1 + RIGHT * 3)
        dict_code = VGroup(
            Text('{"nome": "João",', font_size=16, color=WHITE, font=MONO),
            Text(' "idade": 30}', font_size=16, color=WHITE, font=MONO),
        ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
        dict_code.next_to(dict_title, DOWN, buff=0.2)

        kv = VGroup(
            Text('"nome" → "João"', font_size=14, color=PURPLE, font=MONO),
            Text('"idade" → 30', font_size=14, color=PURPLE, font=MONO),
        ).arrange(DOWN, buff=0.15)
        kv.next_to(dict_code, DOWN, buff=0.2)

        # Rodapé — texto normal, pronúncia no áudio
        rodape = Text("Em APIs, quase tudo é um dicionário.", font_size=16, color=ACCENT, font=MONO)
        rodape.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(titulo), run_time=0.5)
        self.play(FadeIn(lista_title), FadeIn(lista_code), run_time=0.8)
        self.play(FadeIn(indices), run_time=0.5)
        self.play(FadeIn(append_line), run_time=0.4)
        self.play(FadeIn(dict_title), FadeIn(dict_code), run_time=0.8)
        self.play(FadeIn(kv), run_time=0.5)
        self.play(FadeIn(rodape), run_time=0.6)
        self.wait(2)


# ============================================================================
# CENA 4: FUNÇÕES (layout centralizado, setas claras)
# ============================================================================

class Python_Scene4_Funcoes(Scene):
    def construct(self):
        self.camera.background_color = BG

        titulo = Text("Funções", font_size=36, color=PRIMARY, font=MONO)
        titulo.to_edge(UP, buff=0.4)

        # Caixa centralizada
        func_box = Rectangle(width=6.5, height=0.8, color=SECONDARY, stroke_width=2, fill_color=DARK, fill_opacity=0.8)
        func_box.move_to(UP * 1.5)
        func_text = Text('def saudar(nome, saudacao="Olá"):', font_size=16, color=SECONDARY, font=MONO)
        func_text.move_to(func_box.get_center())

        # Chamadas
        call1 = Text('saudar("Maria")', font_size=16, color=WHITE, font=MONO)
        call1.move_to(LEFT * 2.5 + DOWN * 0.3)
        call2 = Text('saudar("João", "Oi")', font_size=16, color=WHITE, font=MONO)
        call2.move_to(RIGHT * 2.5 + DOWN * 0.3)

        # Setas das chamadas pra caixa
        arrow1 = Arrow(call1.get_top(), func_box.get_bottom() + LEFT * 1.5, color=ACCENT, buff=0.1, stroke_width=2)
        arrow2 = Arrow(call2.get_top(), func_box.get_bottom() + RIGHT * 1.5, color=ACCENT, buff=0.1, stroke_width=2)

        # Resultados
        r1_box = Rectangle(width=2.8, height=0.6, color=SECONDARY, stroke_width=2, fill_color=DARK, fill_opacity=0.8)
        r1_box.move_to(LEFT * 2.5 + DOWN * 1.5)
        r1 = Text('"Olá, Maria!"', font_size=16, color=SECONDARY, font=MONO)
        r1.move_to(r1_box.get_center())

        r2_box = Rectangle(width=2.5, height=0.6, color=PURPLE, stroke_width=2, fill_color=DARK, fill_opacity=0.8)
        r2_box.move_to(RIGHT * 2.5 + DOWN * 1.5)
        r2 = Text('"Oi, João!"', font_size=16, color=PURPLE, font=MONO)
        r2.move_to(r2_box.get_center())

        # Setas chamada → resultado
        res_arrow1 = Arrow(call1.get_bottom(), r1_box.get_top(), color=SECONDARY, buff=0.1, stroke_width=2)
        res_arrow2 = Arrow(call2.get_bottom(), r2_box.get_top(), color=PURPLE, buff=0.1, stroke_width=2)

        # Rodapé — texto normal
        rodape = Text("Toda chamada de API é uma função.", font_size=16, color=ACCENT, font=MONO)
        rodape.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(titulo), run_time=0.5)
        self.play(Create(func_box), FadeIn(func_text), run_time=1)
        self.play(FadeIn(call1), FadeIn(call2), Create(arrow1), Create(arrow2), run_time=1)
        self.play(Create(r1_box), FadeIn(r1), Create(res_arrow1), Create(r2_box), FadeIn(r2), Create(res_arrow2), run_time=1.2)
        self.play(FadeIn(rodape), run_time=0.6)
        self.wait(2)


# ============================================================================
# CENA 5: CONDICIONAIS E LOOPS (Code mobject para indentação correta)
# ============================================================================

class Python_Scene5_CondLoops(Scene):
    """If/elif/else, for, while — Code mobject preserva indentação."""

    def construct(self):
        self.camera.background_color = BG

        titulo = Text("Condicionais e Loops", font_size=28, color=PRIMARY, font=MONO)
        titulo.to_edge(UP, buff=0.3)

        # === LADO ESQUERDO: if/elif/else usando Code ===
        if_title = Text("if / elif / else", font_size=18, color=SECONDARY, font=MONO)
        if_title.shift(UP * 2 + LEFT * 3.5)

        if_code = Code(
            code_string='if idade >= 18:\n    "Maior"\nelif idade >= 12:\n    "Adolescente"\nelse:\n    "Criança"',
            language="python",
            background="window",
            add_line_numbers=False,
        )
        if_code.scale(0.55)
        if_code.next_to(if_title, DOWN, buff=0.2)

        # === LADO DIREITO: for/while usando Code ===
        for_title = Text("for / while", font_size=18, color=ACCENT, font=MONO)
        for_title.shift(UP * 2 + RIGHT * 3)

        for_code = Code(
            code_string='for fruta in frutas:\n    print(fruta)\n\nwhile count < 3:\n    count += 1',
            language="python",
            background="window",
            add_line_numbers=False,
        )
        for_code.scale(0.55)
        for_code.next_to(for_title, DOWN, buff=0.2)

        # Rodapé — MONO
        rodape = Text("Com essas 3 estruturas, já dá pra fazer qualquer lógica.", font_size=14, color=GRAY, font=MONO)
        rodape.to_edge(DOWN, buff=0.5)

        # Animações
        self.play(FadeIn(titulo), run_time=0.5)
        self.play(FadeIn(if_title), run_time=0.4)
        self.play(FadeIn(if_code), run_time=1.5)

        self.play(FadeIn(for_title), run_time=0.4)
        self.play(FadeIn(for_code), run_time=1.5)

        self.play(FadeIn(rodape), run_time=0.5)

        self.wait(2)


# CENA 6: PYTHON + IA — A PONTE (setas maiores, JSON legível, resumo alinhado)
# ============================================================================

class Python_Scene6_Ponte(Scene):
    def construct(self):
        self.camera.background_color = BG

        titulo = Text("Python + IA: A Ponte", font_size=32, color=PRIMARY, font=MONO)
        titulo.to_edge(UP, buff=0.3)

        # 3 camadas centralizadas
        py_box = Rectangle(width=5, height=0.9, color=SECONDARY, stroke_width=3, fill_color=DARK, fill_opacity=0.9)
        py_box.shift(UP * 1.8)
        py_text = Text("Python", font_size=28, color=SECONDARY, font=MONO)
        py_text.move_to(py_box.get_center())

        api_box = Rectangle(width=5, height=0.9, color=ACCENT, stroke_width=3, fill_color=DARK, fill_opacity=0.9)
        api_box.shift(DOWN * 0.2)
        api_text = Text("API", font_size=28, color=ACCENT, font=MONO)
        api_text.move_to(api_box.get_center())

        llm_box = Rectangle(width=5, height=0.9, color=PURPLE, stroke_width=3, fill_color=DARK, fill_opacity=0.9)
        llm_box.shift(DOWN * 2.0)
        llm_text = Text("LLM", font_size=28, color=PURPLE, font=MONO)
        llm_text.move_to(llm_box.get_center())

        # Setas grandes
        arrow1 = Arrow(py_box.get_bottom(), api_box.get_top(), color=GRAY, buff=0.15, stroke_width=3, max_tip_length_to_length_ratio=0.15)
        arrow2 = Arrow(api_box.get_bottom(), llm_box.get_top(), color=GRAY, buff=0.15, stroke_width=3, max_tip_length_to_length_ratio=0.15)

        # Labels JSON
        json_down = Text('{"role":"user","content":"Oi"}', font_size=13, color=ACCENT, font=MONO)
        json_down.next_to(arrow1, RIGHT, buff=0.3)
        json_up = Text('{"role":"assistant","content":"Olá!"}', font_size=13, color=SECONDARY, font=MONO)
        json_up.next_to(arrow2, RIGHT, buff=0.3)

        # Resumo à esquerda — MONO alinhado
        resumo = VGroup(
            Text("Python  =  ferramenta", font_size=16, color=WHITE, font=MONO),
            Text("API        =  ponte", font_size=16, color=WHITE, font=MONO),
            Text("LLM        =  cérebro", font_size=16, color=WHITE, font=MONO),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        resumo.shift(DOWN * 3.2 + LEFT * 1)

        # Badge
        badge = Rectangle(width=3.5, height=0.5, color=ACCENT, stroke_width=2, fill_color=ACCENT, fill_opacity=0.15)
        badge.shift(DOWN * 3.2 + RIGHT * 3)
        badge_text = Text("Próx. aula: APIs de LLM", font_size=13, color=ACCENT, font=MONO)
        badge_text.move_to(badge.get_center())

        self.play(FadeIn(titulo), run_time=0.5)
        self.play(Create(py_box), FadeIn(py_text), run_time=0.8)
        self.play(Create(api_box), FadeIn(api_text), run_time=0.8)
        self.play(Create(llm_box), FadeIn(llm_text), run_time=0.8)
        self.play(Create(arrow1), run_time=0.6)
        self.play(FadeIn(json_down), run_time=0.6)
        self.play(Create(arrow2), run_time=0.6)
        self.play(FadeIn(json_up), run_time=0.6)
        self.play(FadeIn(resumo), run_time=0.5)
        self.play(Create(badge), FadeIn(badge_text), run_time=0.6)
        self.wait(2)


# ============================================================================
# CENA 7: CTA
# ============================================================================

class Python_Scene7_CTA(Scene):
    def construct(self):
        self.camera.background_color = BG

        badge = Rectangle(width=2.5, height=0.6, color=ACCENT, stroke_width=0, fill_color=ACCENT, fill_opacity=1)
        badge.shift(UP * 2.2)
        badge_text = Text("AULA 03", font_size=24, color="#000000", font=MONO)
        badge_text.move_to(badge.get_center())

        link1 = Text("Apostila + Notebook", font_size=24, color=WHITE, font=MONO)
        link1.shift(UP * 0.8)

        link2 = Text("luksamuk.codes/pages/guilda-ia", font_size=18, color=PRIMARY, font=MONO)
        link2.next_to(link1, DOWN, buff=0.3)

        prox = Text("Próxima aula: APIs de LLM", font_size=20, color=ACCENT, font=MONO)
        prox.shift(DOWN * 0.8)

        logo = Text("GUILDA DE IA", font_size=56, color=PRIMARY, font=MONO)
        logo.shift(DOWN * 2.2)

        self.play(FadeIn(badge), FadeIn(badge_text), run_time=0.8)
        self.play(FadeIn(link1), run_time=0.6)
        self.play(FadeIn(link2), run_time=0.6)
        self.play(FadeIn(prox), run_time=0.5)
        self.play(FadeIn(logo), run_time=1)
        self.wait(2)