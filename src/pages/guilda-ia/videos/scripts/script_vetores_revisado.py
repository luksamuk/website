#!/usr/bin/env python3
"""
Roteiro Revisado: Vetores e Similaridade de Cosseno
Estrutura coesa com progressão lógica: conceito → visual → matemática → resumo

8 cenas, ~99 segundos de áudio total
"""

from manim import *
import math
import numpy as np

# Cores - Paleta educacional
BG = "#0D1117"        # Fundo escuro
PRIMARY = "#58A6FF"   # Azul suave
SECONDARY = "#7EE787" # Verde
ACCENT = "#F0883E"    # Laranja âmbar
PURPLE = "#BC8CFF"    # Roxo suave
PINK = "#FF9CCE"      # Rosa suave
WHITE = "#E6EDF3"     # Branco suave
GRAY = "#8B949E"      # Cinza para textos secundários
MONO = "JetBrains Mono"


class Scene1_Introducao(Scene):
    """O que são embeddings?"""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        title = Text("O que são embeddings?", font_size=52, color=WHITE, font=MONO)
        title.move_to(UP * 2)
        
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        
        # Animação: palavra → vetor
        palavra = Text("\"gato\"", font_size=36, color=PRIMARY, font=MONO)
        palavra.shift(LEFT * 3)
        
        # HEURÍSTICA: Seta aponta PARA o texto, não para posição arbitrária
        vector_text = Text("[0.23, -0.45, 0.87, ...]", font_size=28, color=SECONDARY, font=MONO)
        vector_text.shift(RIGHT * 2.5)
        
        seta_start = palavra.get_right() + RIGHT * 0.2
        seta_end = vector_text.get_left() + LEFT * 0.15
        seta = Arrow(seta_start, seta_end, color=GRAY, buff=0.1)
        
        self.play(FadeIn(palavra), run_time=1)
        self.play(Create(seta), run_time=0.8)
        self.play(FadeIn(vector_text), run_time=1)
        self.wait(1.5)
        
        # Texto explicativo
        explicacao = Text("Palavras, imagens, sons → vetores", 
                         font_size=28, color=GRAY, font=MONO)
        explicacao.shift(DOWN * 1.5)
        
        self.play(FadeIn(explicacao), run_time=1)
        self.wait(2)


class Scene2_Visualizacao2D(Scene):
    """Visualização em 2 dimensões"""
    
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("Visualizando em 2D", font_size=48, color=WHITE, font=MONO)
        title.to_edge(UP, buff=0.3)
        
        self.play(FadeIn(title), run_time=1)
        
        # Sistema de coordenadas
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5,
            y_length=5,
            axis_config={"color": GRAY, "stroke_width": 1}
        )
        axes.shift(DOWN * 0.5)
        
        # Círculo unitário (referência)
        circle = Circle(radius=1, color=GRAY, stroke_opacity=0.3)
        circle.move_to(axes.get_origin())
        
        # Vetor exemplo
        v1 = [0.7, 0.5]
        v1_arrow = Arrow(
            axes.c2p(0, 0),
            axes.c2p(v1[0], v1[1]),
            color=PRIMARY, buff=0, stroke_width=4
        )
        
        # Ponto no vetor
        dot = Dot(point=axes.c2p(v1[0], v1[1]), color=ACCENT, radius=0.08)
        
        # Labels
        v1_label = Text("vetor", font_size=20, color=PRIMARY, font=MONO)
        v1_label.next_to(dot, UR, buff=0.15)
        
        truncate_text = Text("Truncado de 768 para 2 dimensões",
                            font_size=22, color=GRAY, font=MONO)
        truncate_text.shift(DOWN * 2.5)
        
        # Animações
        self.play(Create(axes), run_time=1)
        self.play(Create(circle), run_time=0.8)
        self.play(Create(v1_arrow), run_time=1)
        self.play(FadeIn(dot), FadeIn(v1_label), run_time=0.5)
        self.play(FadeIn(truncate_text), run_time=1)
        self.wait(2)


class Scene3_CirculoUnitario(Scene):
    """Círculo Unitário e Cosseno"""
    
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("Círculo Unitário", font_size=48, color=WHITE, font=MONO)
        title.to_edge(UP, buff=0.3)
        
        self.play(FadeIn(title), run_time=1)
        
        # Sistema de coordenadas
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5,
            y_length=5,
            axis_config={"color": GRAY, "stroke_width": 1}
        )
        axes.shift(DOWN * 0.3)
        
        # Círculo unitário
        circle = Circle(radius=1, color=PRIMARY, stroke_width=2)
        circle.move_to(axes.get_origin())
        
        # Ângulo exemplo (37°)
        angle_rad = math.radians(37)
        scale = 1.0
        
        # Vetor
        v_end = axes.c2p(scale * math.cos(angle_rad), scale * math.sin(angle_rad))
        v_arrow = Arrow(axes.c2p(0, 0), v_end, color=ACCENT, buff=0, stroke_width=3)
        
        # Projeção no eixo X (cosseno)
        proj_x = axes.c2p(scale * math.cos(angle_rad), 0)
        dashed_line = DashedLine(v_end, proj_x, color=SECONDARY, stroke_width=1.5)
        
        # Arco do ângulo
        arc = Arc(radius=0.3, start_angle=0, angle=angle_rad, color=PINK, stroke_width=2)
        arc.move_to(axes.get_origin())
        
        # Theta label
        theta_label = Text("θ", font_size=24, color=PINK, font=MONO)
        theta_label.move_to(axes.c2p(0.25, 0.12))
        
        # Cosseno label
        cos_label = Text(f"cos(θ) = {math.cos(angle_rad):.2f}", 
                        font_size=24, color=SECONDARY, font=MONO)
        cos_label.shift(DOWN * 2.3)
        
        # Animações
        self.play(Create(axes), Create(circle), run_time=1.5)
        self.play(Create(v_arrow), run_time=1)
        self.play(Create(arc), FadeIn(theta_label), run_time=0.8)
        self.play(Create(dashed_line), run_time=1)
        self.play(FadeIn(cos_label), run_time=1)
        self.wait(2)
        
        # Mostrar range
        range_text = Text("cosseno ∈ [-1, 1]", font_size=22, color=GRAY, font=MONO)
        range_text.shift(DOWN * 2.8)
        self.play(FadeIn(range_text), run_time=0.8)
        self.wait(1)


class Scene4_VetorEProjecao(Scene):
    """Vetor e projeção - cosseno positivo/negativo"""
    
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("Projeção e Direção", font_size=48, color=WHITE, font=MONO)
        title.to_edge(UP, buff=0.3)
        
        self.play(FadeIn(title), run_time=1)
        
        # Sistema de coordenadas
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5,
            y_length=5,
            axis_config={"color": GRAY, "stroke_width": 1}
        )
        axes.shift(DOWN * 0.3)
        
        circle = Circle(radius=1, color=GRAY, stroke_opacity=0.3)
        circle.move_to(axes.get_origin())
        
        self.play(Create(axes), Create(circle), run_time=1)
        
        # Vetor apontando para cima (cosseno positivo)
        angle1 = math.radians(30)
        v1 = Arrow(axes.c2p(0, 0), axes.c2p(math.cos(angle1), math.sin(angle1)),
                   color=PRIMARY, buff=0, stroke_width=3)
        
        label_pos = Text("cima → cos > 0", font_size=20, color=PRIMARY, font=MONO)
        label_pos.shift(UP * 1.5 + RIGHT * 2)
        
        self.play(Create(v1), FadeIn(label_pos), run_time=1.5)
        self.wait(0.8)
        
        # Vetor apontando para baixo (cosseno negativo)
        angle2 = math.radians(150)  # 150° = cosseno negativo
        v2 = Arrow(axes.c2p(0, 0), axes.c2p(math.cos(angle2), math.sin(angle2)),
                   color=ACCENT, buff=0, stroke_width=3)
        
        label_neg = Text("baixo → cos < 0", font_size=20, color=ACCENT, font=MONO)
        label_neg.shift(DOWN * 1.5 + LEFT * 2)
        
        self.play(Create(v2), FadeIn(label_neg), run_time=1.5)
        self.wait(2)


class Scene5_DoisVetores(Scene):
    """Dois vetores e o ângulo entre eles"""
    
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("Ângulo entre Vetores", font_size=48, color=WHITE, font=MONO)
        title.to_edge(UP, buff=0.3)
        
        self.play(FadeIn(title), run_time=1)
        
        # Sistema de coordenadas
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5,
            y_length=5,
            axis_config={"color": GRAY, "stroke_width": 1}
        )
        axes.shift(DOWN * 0.3)
        
        circle = Circle(radius=1, color=GRAY, stroke_opacity=0.3)
        circle.move_to(axes.get_origin())
        
        self.play(Create(axes), Create(circle), run_time=1)
        
        # Dois vetores
        v1_angle = math.radians(20)
        v2_angle = math.radians(60)
        
        v1 = Arrow(axes.c2p(0, 0), 
                   axes.c2p(math.cos(v1_angle), math.sin(v1_angle)),
                   color=PRIMARY, buff=0, stroke_width=3)
        
        v2 = Arrow(axes.c2p(0, 0),
                   axes.c2p(math.cos(v2_angle), math.sin(v2_angle)),
                   color=SECONDARY, buff=0, stroke_width=3)
        
        # Arc between them
        angle_diff = v2_angle - v1_angle
        arc = Arc(radius=0.4, start_angle=v1_angle, angle=angle_diff,
                  color=PINK, stroke_width=2.5)
        arc.move_to(axes.get_origin())
        
        # Labels
        v1_label = Text("v₁", font_size=20, color=PRIMARY, font=MONO)
        v1_label.next_to(v1.get_end(), UR, buff=0.1)
        
        v2_label = Text("v₂", font_size=20, color=SECONDARY, font=MONO)
        v2_label.next_to(v2.get_end(), UR, buff=0.1)
        
        theta = Text("θ", font_size=24, color=PINK, font=MONO)
        theta.move_to(axes.c2p(0.3, 0.25))
        
        similaridade = Text("ângulo pequeno → similaridade alta",
                           font_size=22, color=GRAY, font=MONO)
        similaridade.shift(DOWN * 2.3)
        
        # Animações
        self.play(Create(v1), FadeIn(v1_label), run_time=1)
        self.play(Create(v2), FadeIn(v2_label), run_time=1)
        self.play(Create(arc), FadeIn(theta), run_time=0.8)
        self.play(FadeIn(similaridade), run_time=1)
        self.wait(2)


class Scene6_VetoresOpostos(Scene):
    """Vetores com direções opostas"""
    
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("Vetores Opostos", font_size=48, color=WHITE, font=MONO)
        title.to_edge(UP, buff=0.3)
        
        self.play(FadeIn(title), run_time=1)
        
        # Sistema de coordenadas
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5,
            y_length=5,
            axis_config={"color": GRAY, "stroke_width": 1}
        )
        axes.shift(DOWN * 0.3)
        
        circle = Circle(radius=1, color=GRAY, stroke_opacity=0.3)
        circle.move_to(axes.get_origin())
        
        self.play(Create(axes), Create(circle), run_time=1)
        
        # Dois vetores opostos
        # Vetor 1: 45° (nordeste)
        v1_angle = math.radians(45)
        v1 = Arrow(axes.c2p(0, 0),
                   axes.c2p(math.cos(v1_angle), math.sin(v1_angle)),
                   color=PRIMARY, buff=0, stroke_width=3)
        
        # Vetor 2: 225° (sudoeste) - oposto
        v2_angle = math.radians(225)
        v2 = Arrow(axes.c2p(0, 0),
                   axes.c2p(math.cos(v2_angle), math.sin(v2_angle)),
                   color=ACCENT, buff=0, stroke_width=3)
        
        # Labels
        v1_label = Text("v₁", font_size=20, color=PRIMARY, font=MONO)
        v1_label.next_to(v1.get_end(), UR, buff=0.1)
        
        v2_label = Text("v₂", font_size=20, color=ACCENT, font=MONO)
        v2_label.next_to(v2.get_end(), DL, buff=0.1)
        
        # Ângulo de 180°
        angle_text = Text("θ = 180°", font_size=24, color=PINK, font=MONO)
        angle_text.move_to(DOWN * 1.5 + RIGHT * 1.5)
        
        # Similaridade
        sim_text = Text("similaridade = cos(180°) = -1",
                       font_size=24, color=WHITE, font=MONO)
        sim_text.shift(DOWN * 2.3)
        
        # Significado
        meaning = Text("Significados completamente diferentes!",
                       font_size=22, color=ACCENT, font=MONO)
        meaning.shift(DOWN * 2.8)
        
        # Animações
        self.play(Create(v1), FadeIn(v1_label), run_time=1)
        self.play(Create(v2), FadeIn(v2_label), run_time=1)
        self.play(FadeIn(angle_text), run_time=0.8)
        self.play(FadeIn(sim_text), run_time=1)
        self.play(FadeIn(meaning), run_time=1)
        self.wait(2)


class Scene7_Formula(Scene):
    """Fórmula matemática do cosseno"""
    
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("A Fórmula", font_size=48, color=WHITE, font=MONO)
        title.to_edge(UP, buff=0.3)
        
        self.play(FadeIn(title), run_time=1)
        
        # Fórmula: cos(θ) = (A · B) / (||A|| × ||B||)
        cos_theta = Text("cos(θ)", font_size=48, color=PRIMARY, font=MONO)
        equals = Text("=", font_size=48, color=WHITE, font=MONO)
        
        # Numerador
        numerator = Text("A · B", font_size=36, color=SECONDARY, font=MONO)
        
        # Linha de fração
        frac_line = Line(LEFT * 1.5, RIGHT * 1.5, color=WHITE, stroke_width=2)
        
        # Denominador
        denominator = Text("||A|| × ||B||", font_size=36, color=ACCENT, font=MONO)
        
        # Posicionar
        cos_theta.move_to(LEFT * 3 + UP * 0.5)
        equals.next_to(cos_theta, RIGHT, buff=0.3)
        
        # Numerador acima da linha
        numerator.move_to(RIGHT * 2 + UP * 0.5)
        frac_line.next_to(numerator, DOWN, buff=0.15)
        denominator.next_to(frac_line, DOWN, buff=0.15)
        
        # Animações
        self.play(Write(cos_theta), run_time=1)
        self.play(FadeIn(equals), run_time=0.5)
        self.play(FadeIn(numerator), FadeIn(frac_line), FadeIn(denominator), run_time=1.5)
        self.wait(1)
        
        # Explicação
        exp1 = Text("Produto escalar no numerador", 
                   font_size=24, color=GRAY, font=MONO)
        exp1.shift(DOWN * 1.5)
        
        exp2 = Text("Magnitudes normalizadas: ||A|| = ||B|| = 1",
                   font_size=24, color=GRAY, font=MONO)
        exp2.shift(DOWN * 2.1)
        
        exp3 = Text("→ Cosseno captura apenas a DIREÇÃO",
                   font_size=28, color=WHITE, font=MONO)
        exp3.shift(DOWN * 2.8)
        
        self.play(FadeIn(exp1), run_time=1)
        self.play(FadeIn(exp2), run_time=1)
        self.play(FadeIn(exp3), run_time=1.5)
        self.wait(2)


class Scene8_Resumo(Scene):
    """Resumo final"""
    
    def construct(self):
        self.camera.background_color = BG
        
        title = Text("Resumo", font_size=52, color=WHITE, font=MONO)
        title.to_edge(UP, buff=0.3)
        
        self.play(FadeIn(title), run_time=1)
        
        # Três casos: semelhantes, ortogonais, opostos
        # Usar posicionamento numérico claro
        
        y_center = 0
        
        # Semelhantes
        semelhantes_title = Text("Ângulo pequeno", font_size=28, color=GRAY, font=MONO)
        semelhantes_title.move_to(UP * 1.5 + LEFT * 3)
        
        semelhantes_valor = Text("→ similaridade alta (~1)", 
                                font_size=28, color=SECONDARY, font=MONO)
        semelhantes_valor.next_to(semelhantes_title, RIGHT, buff=0.2)
        
        # Ortogonais
        ortogonais_title = Text("Ângulo reto (90°)", font_size=28, color=GRAY, font=MONO)
        ortogonais_title.move_to(y_center + LEFT * 3)
        
        ortogonais_valor = Text("→ similaridade zero", 
                               font_size=28, color=GRAY, font=MONO)
        ortogonais_valor.next_to(ortogonais_title, RIGHT, buff=0.2)
        
        # Opostos
        opostos_title = Text("Ângulo 180°", font_size=28, color=GRAY, font=MONO)
        opostos_title.move_to(DOWN * 1.5 + LEFT * 3)
        
        opostos_valor = Text("→ similaridade negativa (-1)", 
                            font_size=28, color=ACCENT, font=MONO)
        opostos_valor.next_to(opostos_title, RIGHT, buff=0.2)
        
        # Animações
        self.play(FadeIn(semelhantes_title), FadeIn(semelhantes_valor), run_time=1)
        self.play(FadeIn(ortogonais_title), FadeIn(ortogonais_valor), run_time=1)
        self.play(FadeIn(opostos_title), FadeIn(opostos_valor), run_time=1)
        self.wait(1)
        
        # Conclusão
        conclusao = Text("Não importa o tamanho, importa a DIREÇÃO.",
                         font_size=32, color=WHITE, font=MONO)
        conclusao.shift(DOWN * 2.8)
        
        self.play(FadeIn(conclusao), run_time=1.5)
        self.wait(2)


# Renderizar todas as cenas:
# manim -qh script_vetores_revisado.py Scene1_Introducao Scene2_Visualizacao2D ...