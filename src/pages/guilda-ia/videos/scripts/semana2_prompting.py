#!/usr/bin/env python3
"""
Aula 2: Prompting - Como falar com IA

Estrutura (~4 min):
1. Intro - O problema do prompt
2. Zero-shot vs Few-shot
3. Role Prompting
4. Chain-of-Thought
5. Framework RCEF
6. Resumo

Renderizar:
    source ~/manim-env/bin/activate
    manim -qh semana2_prompting.py Prompting_Scene1_Hook Prompting_Scene2_Problema
    manim -qh semana2_prompting.py Prompting_Scene3_ZeroShot Prompting_Scene4_FewShot
    manim -qh semana2_prompting.py Prompting_Scene5_Role Prompting_Scene6_CoT
    manim -qh semana2_prompting.py Prompting_Scene7_RCEF Prompting_Scene8_Resumo
"""

from manim import *

# Paleta de cores
BG = "#0D1117"
PRIMARY = "#58A6FF"
SECONDARY = "#7EE787"
ACCENT = "#F78166"
PURPLE = "#D2A8FF"
PINK = "#FF7B72"
GRAY = "#8B949E"

MONO = "IBM Plex Mono"

# ============================================================================
# CENA 1: HOOK
# ============================================================================

class Prompting_Scene1_Hook(Scene):
    """Hook: A mesma pergunta, respostas diferentes."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Prompting", font_size=64, color=PRIMARY, font=MONO)
        
        # Subtítulo
        subtitulo = Text("Como falar com IA", font_size=32, color=WHITE, font=MONO)
        subtitulo.next_to(titulo, DOWN, buff=0.5)
        
        # Exemplo
        exemplo = VGroup(
            Text('"Me fale sobre gatos"', font_size=20, color=GRAY, font=MONO),
            Text("→ resposta genérica", font_size=16, color=PINK, font=MONO),
        )
        exemplo.arrange(DOWN, buff=0.1)
        exemplo.shift(DOWN * 1.5)
        
        exemplo2 = VGroup(
            Text('"Quais as 3 raças mais populares no Brasil?"', font_size=20, color=GRAY, font=MONO),
            Text("→ resposta específica", font_size=16, color=SECONDARY, font=MONO),
        )
        exemplo2.arrange(DOWN, buff=0.1)
        exemplo2.shift(DOWN * 2.8)
        
        # Animações
        self.play(FadeIn(titulo), run_time=1)
        self.play(FadeIn(subtitulo), run_time=0.8)
        self.play(FadeIn(exemplo), run_time=1)
        self.play(FadeIn(exemplo2), run_time=1)
        
        self.wait(2)


class Prompting_Scene2_Problema(Scene):
    """O problema: mesma IA, resultados diferentes."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("O Problema", font_size=36, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # IA no centro
        ia_box = Square(side_length=2.5, color=PRIMARY, stroke_width=3)
        ia_label = Text("LLM", font_size=32, color=PRIMARY, font=MONO)
        ia_label.move_to(ia_box.get_center())
        
        # Prompt ruim
        ruim_box = Rectangle(width=3, height=1, color=PINK, stroke_width=2)
        ruim_box.shift(LEFT * 3.5 + UP * 1)
        ruim_label = Text('Prompt vago', font_size=18, color=PINK, font=MONO)
        ruim_label.move_to(ruim_box.get_center())
        
        # Resultado ruim
        bad_result = Text('Resposta\ninútil', font_size=16, color=PINK, font=MONO)
        bad_result.shift(RIGHT * 3.5 + UP * 1)
        
        # Prompt bom
        bom_box = Rectangle(width=3, height=1, color=SECONDARY, stroke_width=2)
        bom_box.shift(LEFT * 3.5 + DOWN * 1)
        bom_label = Text('Prompt claro', font_size=18, color=SECONDARY, font=MONO)
        bom_label.move_to(bom_box.get_center())
        
        # Resultado bom
        good_result = Text('Resposta\nexcelente', font_size=16, color=SECONDARY, font=MONO)
        good_result.shift(RIGHT * 3.5 + DOWN * 1)
        
        # Setas
        arrow1 = Arrow(ruim_box.get_right(), ia_box.get_left(), color=PINK, buff=0.2)
        arrow2 = Arrow(ia_box.get_right(), bad_result.get_left(), color=PINK, buff=0.2)
        arrow3 = Arrow(bom_box.get_right(), ia_box.get_left(), color=SECONDARY, buff=0.2)
        arrow4 = Arrow(ia_box.get_right(), good_result.get_left(), color=SECONDARY, buff=0.2)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.5)
        self.play(Create(ia_box), FadeIn(ia_label), run_time=1)
        
        self.play(FadeIn(ruim_box), FadeIn(ruim_label), run_time=0.8)
        self.play(Create(arrow1), run_time=0.5)
        self.play(FadeIn(bad_result), run_time=0.8)
        
        self.wait(0.5)
        
        self.play(FadeIn(bom_box), FadeIn(bom_label), run_time=0.8)
        self.play(Create(arrow3), run_time=0.5)
        self.play(FadeIn(good_result), run_time=0.8)
        
        self.wait(2)


# ============================================================================
# CENA 2: ZERO-SHOT vs FEW-SHOT
# ============================================================================

class Prompting_Scene3_ZeroShot(Scene):
    """Zero-shot: pedir sem exemplos."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Zero-shot", font_size=36, color=PRIMARY, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # Definição
        def_text = Text("Pedir sem dar exemplos", font_size=22, color=GRAY, font=MONO)
        def_text.next_to(titulo, DOWN, buff=0.5)
        
        # Exemplo visual
        prompt_box = Rectangle(width=5.5, height=1.5, color=ACCENT, stroke_width=2)
        prompt_box.center()
        
        prompt_text = Text(
            'Traduza para inglês:\n"Bom dia"',
            font_size=20, color=WHITE, font=MONO
        )
        prompt_text.move_to(prompt_box.get_center())
        
        # Seta
        arrow = Arrow(ORIGIN, RIGHT, color=GRAY, buff=0.5)
        arrow.shift(DOWN * 2)
        
        # Resultado
        result_box = Rectangle(width=3, height=0.8, color=SECONDARY, stroke_width=2)
        result_box.shift(DOWN * 2 + RIGHT * 2.5)
        
        result_text = Text('"Good morning"', font_size=20, color=SECONDARY, font=MONO)
        result_text.move_to(result_box.get_center())
        
        # Quando usar
        quando = Text("Use para: tarefas simples", font_size=18, color=GRAY, font=MONO)
        quando.to_edge(DOWN, buff=0.5)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.5)
        self.play(FadeIn(def_text), run_time=0.6)
        self.play(Create(prompt_box), FadeIn(prompt_text), run_time=1)
        self.play(Create(arrow), run_time=0.5)
        self.play(Create(result_box), FadeIn(result_text), run_time=0.8)
        self.play(FadeIn(quando), run_time=0.5)
        
        self.wait(2)


class Prompting_Scene4_FewShot(Scene):
    """Few-shot: dar exemplos antes."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Few-shot", font_size=36, color=SECONDARY, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # Definição
        def_text = Text("Dar exemplos de input → output", font_size=22, color=GRAY, font=MONO)
        def_text.next_to(titulo, DOWN, buff=0.3)
        
        # Exemplos
        ex1 = Text('"Gato" → "Cat"', font_size=18, color=WHITE, font=MONO)
        ex2 = Text('"Cachorro" → "Dog"', font_size=18, color=WHITE, font=MONO)
        ex3 = Text('"Pássaro" → "Bird"', font_size=18, color=WHITE, font=MONO)
        
        exemplos = VGroup(ex1, ex2, ex3)
        exemplos.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        exemplos.shift(UP * 0.5 + LEFT * 1.5)
        
        # Query
        query = Text('"Peixe" → ?', font_size=20, color=ACCENT, font=MONO)
        query.next_to(exemplos, DOWN, buff=0.5)
        
        # Seta
        arrow = Arrow(query.get_right(), RIGHT, color=GRAY)
        
        # Resultado
        result = Text('"Fish"', font_size=20, color=SECONDARY, font=MONO)
        result.shift(RIGHT * 3)
        
        # Quando usar
        quando = Text("Use para: formato específico", font_size=18, color=GRAY, font=MONO)
        quando.to_edge(DOWN, buff=0.5)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.5)
        self.play(FadeIn(def_text), run_time=0.6)
        
        for ex in exemplos:
            self.play(FadeIn(ex), run_time=0.4)
        
        self.play(FadeIn(query), run_time=0.6)
        self.play(Create(arrow), run_time=0.5)
        self.play(FadeIn(result), run_time=0.8)
        self.play(FadeIn(quando), run_time=0.5)
        
        self.wait(2)


# ============================================================================
# CENA 3: ROLE PROMPTING
# ============================================================================

class Prompting_Scene5_Role(Scene):
    """Role Prompting: definir quem a IA deve ser."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Role Prompting", font_size=36, color=PURPLE, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # Definição
        def_text = Text("Atribuir um papel à IA", font_size=22, color=GRAY, font=MONO)
        def_text.next_to(titulo, DOWN, buff=0.3)
        
        # Box de role
        role_box = Rectangle(width=6, height=2.5, color=PURPLE, stroke_width=2)
        role_box.center()
        
        role_text = VGroup(
            Text("Você é um professor de matemática", font_size=18, color=WHITE, font=MONO),
            Text("do ensino médio, especializado em", font_size=18, color=WHITE, font=MONO),
            Text("explicar conceitos complexos de", font_size=18, color=WHITE, font=MONO),
            Text("forma simples.", font_size=18, color=WHITE, font=MONO),
        )
        role_text.arrange(DOWN, buff=0.1)
        role_text.move_to(role_box.get_center())
        
        # Componentes
        comp_title = Text("Componentes de um bom role:", font_size=16, color=GRAY, font=MONO)
        comp_title.to_edge(DOWN, buff=1.2)
        
        componentes = VGroup(
            Text("1. Identidade", font_size=16, color=PURPLE, font=MONO),
            Text("2. Expertise", font_size=16, color=ACCENT, font=MONO),
            Text("3. Público", font_size=16, color=SECONDARY, font=MONO),
            Text("4. Tom", font_size=16, color=PRIMARY, font=MONO),
        )
        componentes.arrange(RIGHT, buff=0.8)
        componentes.next_to(comp_title, DOWN, buff=0.2)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.5)
        self.play(FadeIn(def_text), run_time=0.6)
        self.play(Create(role_box), FadeIn(role_text), run_time=1.2)
        self.play(FadeIn(comp_title), run_time=0.5)
        
        for comp in componentes:
            self.play(FadeIn(comp), run_time=0.3)
        
        self.wait(2)


# ============================================================================
# CENA 4: CHAIN-OF-THOUGHT
# ============================================================================

class Prompting_Scene6_CoT(Scene):
    """Chain-of-Thought: pensar passo a passo."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Chain-of-Thought", font_size=32, color=ACCENT, font=MONO)
        titulo.to_edge(UP, buff=0.3)
        
        # Subtítulo
        sub = Text('"Vamos pensar passo a passo"', font_size=20, color=WHITE, font=MONO)
        sub.next_to(titulo, DOWN, buff=0.3)
        
        # Problema
        problema = VGroup(
            Text("Roger tem 5 bolas.", font_size=16, color=GRAY, font=MONO),
            Text("Compra 2 latas de 3 bolas.", font_size=16, color=GRAY, font=MONO),
            Text("Quantas bolas?", font_size=16, color=ACCENT, font=MONO),
        )
        problema.arrange(DOWN, buff=0.1)
        problema.shift(UP * 0.5 + LEFT * 3)
        
        # Raaciocínio
        raciocinio = VGroup(
            Text("Passo 1: 5 bolas iniciais", font_size=14, color=WHITE, font=MONO),
            Text("Passo 2: 2 × 3 = 6 bolas", font_size=14, color=SECONDARY, font=MONO),
            Text("Passo 3: 5 + 6 = 11", font_size=14, color=ACCENT, font=MONO),
        )
        raciocinio.arrange(DOWN, buff=0.15)
        raciocinio.shift(UP * 0.5 + RIGHT * 3)
        
        # Resultado
        result_box = Rectangle(width=3, height=0.6, color=SECONDARY, stroke_width=2)
        result_box.shift(DOWN * 1.5)
        
        result = Text("Resposta: 11", font_size=20, color=SECONDARY, font=MONO)
        result.move_to(result_box.get_center())
        
        # Paper
        paper = Text("Wei et al. (2022)", font_size=14, color=GRAY, font=MONO)
        paper.to_edge(DOWN, buff=0.3)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.6)
        self.play(FadeIn(problema), run_time=1)
        
        for passo in raciocinio:
            self.play(FadeIn(passo), run_time=0.5)
        
        self.play(Create(result_box), FadeIn(result), run_time=0.8)
        self.play(FadeIn(paper), run_time=0.5)
        
        self.wait(2)


# ============================================================================
# CENA 5: FRAMEWORK RCEF
# ============================================================================

class Prompting_Scene7_RCEF(Scene):
    """Framework R-C-E-F para prompts estruturados."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Framework R-C-E-F", font_size=32, color=PRIMARY, font=MONO)
        titulo.to_edge(UP, buff=0.3)
        
        # Letras
        r = VGroup(
            Text("R", font_size=36, color=PRIMARY, font=MONO),
            Text("Role", font_size=16, color=GRAY, font=MONO),
        )
        r.arrange(DOWN, buff=0.1)
        
        c1 = VGroup(
            Text("C", font_size=36, color=SECONDARY, font=MONO),
            Text("Context", font_size=16, color=GRAY, font=MONO),
        )
        c1.arrange(DOWN, buff=0.1)
        
        e = VGroup(
            Text("E", font_size=36, color=ACCENT, font=MONO),
            Text("Examples", font_size=16, color=GRAY, font=MONO),
        )
        e.arrange(DOWN, buff=0.1)
        
        f = VGroup(
            Text("F", font_size=36, color=PURPLE, font=MONO),
            Text("Format", font_size=16, color=GRAY, font=MONO),
        )
        f.arrange(DOWN, buff=0.1)
        
        framework = VGroup(r, c1, e, f)
        framework.arrange(RIGHT, buff=1)
        framework.center()
        
        # Exemplo
        exemplo = VGroup(
            Text("# ROLE", font_size=14, color=PRIMARY, font=MONO),
            Text("Você é um revisor de código", font_size=12, color=GRAY, font=MONO),
            Text("# CONTEXT", font_size=14, color=SECONDARY, font=MONO),
            Text("Código de e-commerce", font_size=12, color=GRAY, font=MONO),
            Text("# FORMAT", font_size=14, color=PURPLE, font=MONO),
            Text("JSON: {issues, suggestions}", font_size=12, color=GRAY, font=MONO),
        )
        exemplo.arrange(DOWN, buff=0.15)
        exemplo.to_edge(DOWN, buff=0.5)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.5)
        
        for letra in framework:
            self.play(FadeIn(letra), run_time=0.5)
        
        self.play(FadeIn(exemplo), run_time=1)
        
        self.wait(2)


# ============================================================================
# CENA 6: RESUMO
# ============================================================================

class Prompting_Scene8_Resumo(Scene):
    """Resumo da aula."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Resumo", font_size=36, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # Tópicos
        topicos = VGroup()
        
        t1 = VGroup(
            Text("Zero-shot", font_size=24, color=PRIMARY, font=MONO),
            Text("→ Pedir sem exemplos", font_size=16, color=GRAY, font=MONO),
        )
        
        t2 = VGroup(
            Text("Few-shot", font_size=24, color=SECONDARY, font=MONO),
            Text("→ Dar exemplos antes", font_size=16, color=GRAY, font=MONO),
        )
        
        t3 = VGroup(
            Text("Role Prompting", font_size=24, color=PURPLE, font=MONO),
            Text("→ Definir quem a IA é", font_size=16, color=GRAY, font=MONO),
        )
        
        t4 = VGroup(
            Text("Chain-of-Thought", font_size=24, color=ACCENT, font=MONO),
            Text("→ Pensar passo a passo", font_size=16, color=GRAY, font=MONO),
        )
        
        t5 = VGroup(
            Text("R-C-E-F", font_size=24, color=PRIMARY, font=MONO),
            Text("→ Role, Context, Examples, Format", font_size=16, color=GRAY, font=MONO),
        )
        
        topicos.add(t1, t2, t3, t4, t5)
        topicos.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        topicos.center()
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.5)
        
        for t in topicos:
            self.play(FadeIn(t), run_time=0.5)
        
        self.wait(2)


# ============================================================================
# INSTRUÇÕES
# ============================================================================
"""
RENDERIZAR TUDO:
    source ~/manim-env/bin/activate
    manim -qh semana2_prompting.py Prompting_Scene1_Hook Prompting_Scene2_Problema
    manim -qh semana2_prompting.py Prompting_Scene3_ZeroShot Prompting_Scene4_FewShot
    manim -qh semana2_prompting.py Prompting_Scene5_Role Prompting_Scene6_CoT
    manim -qh semana2_prompting.py Prompting_Scene7_RCEF Prompting_Scene8_Resumo

GERAR ÁUDIOS:
    python generate_audio_semana2.py

SINCRONIZAR:
    python sync_semana2.py
"""