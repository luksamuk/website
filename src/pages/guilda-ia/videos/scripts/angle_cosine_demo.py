#!/usr/bin/env python3
"""
Cena didática: Ângulo e Cosseno entre Vetores
Demonstra visualmente três casos: semelhantes, ortogonais, opostos.

Renderizar:
    source ~/manim-env/bin/activate
    manim -qh angle_cosine_demo.py AngleCosineDemo
"""

from manim import *
import math

# Cores
BG = "#0D1117"
PRIMARY = "#58A6FF"
SECONDARY = "#7EE787"
ACCENT = "#F0883E"
PINK = "#FF7B72"
PURPLE = "#D2A8FF"

MONO = "IBM Plex Mono"


class AngleCosineDemo(Scene):
    """Demonstra os três casos de relacionamento entre vetores."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Ângulo e Cosseno", font_size=36, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.3)
        
        # Subtítulo
        subtitulo = Text("Similaridade de vetores no círculo unitário", font_size=18, color=GRAY, font=MONO)
        subtitulo.next_to(titulo, DOWN, buff=0.2)
        
        self.play(FadeIn(titulo), FadeIn(subtitulo), run_time=1)
        
        # ===== PARTE 1: CÍRCULO UNITÁRIO =====
        
        # Eixos
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5,
            y_length=5,
            axis_config={"color": GRAY, "stroke_width": 1.5},
            tips=False
        )
        axes.shift(LEFT * 2.5)
        
        # Labels dos eixos
        x_label = Text("x", font_size=16, color=GRAY, font=MONO)
        x_label.next_to(axes.x_axis, RIGHT, buff=0.1)
        
        y_label = Text("y", font_size=16, color=GRAY, font=MONO)
        y_label.next_to(axes.y_axis, UP, buff=0.1)
        
        # Círculo unitário
        circle = Circle(radius=2, color=GRAY, stroke_width=1, stroke_opacity=0.4)
        circle.move_to(axes.get_origin())
        
        # ===== CASO 1: SEMELHANTES =====
        
        # Vetores com ângulo pequeno
        angle1 = math.radians(15)  # 15° entre eles
        v1_end = axes.c2p(math.cos(math.radians(30)), math.sin(math.radians(30)))
        v2_end = axes.c2p(math.cos(math.radians(45)), math.sin(math.radians(45)))
        
        v1_arrow = Arrow(
            axes.c2p(0, 0), v1_end,
            color=PRIMARY, buff=0, stroke_width=3
        )
        v2_arrow = Arrow(
            axes.c2p(0, 0), v2_end,
            color=SECONDARY, buff=0, stroke_width=3
        )
        
        # Arco do ângulo
        angle_arc1 = Arc(
            radius=0.5,
            start_angle=math.radians(30),
            angle=math.radians(15),
            color=ACCENT,
            stroke_width=2
        )
        angle_arc1.move_to(axes.get_origin())
        
        # Label do caso 1
        label1_v1 = Text("v₁", font_size=14, color=PRIMARY, font=MONO)
        label1_v1.next_to(v1_end, UR, buff=0.1)
        
        label1_v2 = Text("v₂", font_size=14, color=SECONDARY, font=MONO)
        label1_v2.next_to(v2_end, UR, buff=0.1)
        
        desc1_title = Text("Semelhantes", font_size=22, color=PRIMARY, font=MONO)
        desc1_title.shift(RIGHT * 3 + UP * 1.5)
        
        desc1_text = VGroup(
            Text("θ = 15°", font_size=16, color=WHITE, font=MONO),
            Text("cos(θ) ≈ 0.97", font_size=16, color=SECONDARY, font=MONO),
            Text("Significados parecidos", font_size=14, color=GRAY, font=MONO),
        )
        desc1_text.arrange(DOWN, buff=0.1)
        desc1_text.next_to(desc1_title, DOWN, buff=0.3)
        
        self.play(Create(axes), Create(circle), run_time=1)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.5)
        
        self.play(Create(v1_arrow), Create(v2_arrow), run_time=1)
        self.play(Create(angle_arc1), run_time=0.5)
        self.play(FadeIn(label1_v1), FadeIn(label1_v2), run_time=0.3)
        
        self.play(FadeIn(desc1_title), FadeIn(desc1_text), run_time=0.8)
        self.wait(2)
        
        # ===== CASO 2: ORTOGONAIS =====
        
        # Limpar caso anterior
        self.play(
            FadeOut(v1_arrow), FadeOut(v2_arrow),
            FadeOut(angle_arc1), FadeOut(label1_v1), FadeOut(label1_v2),
            FadeOut(desc1_title), FadeOut(desc1_text),
            run_time=0.5
        )
        
        # Vetores ortogonais (90°)
        v3_end = axes.c2p(1, 0)  # Horizontal
        v4_end = axes.c2p(0, 1)  # Vertical
        
        v3_arrow = Arrow(
            axes.c2p(0, 0), v3_end,
            color=PRIMARY, buff=0, stroke_width=3
        )
        v4_arrow = Arrow(
            axes.c2p(0, 0), v4_end,
            color=SECONDARY, buff=0, stroke_width=3
        )
        
        # Arco de 90°
        angle_arc2 = Arc(
            radius=0.5,
            start_angle=math.radians(0),
            angle=math.radians(90),
            color=ACCENT,
            stroke_width=2
        )
        angle_arc2.move_to(axes.get_origin())
        
        label2_v3 = Text("v₁", font_size=14, color=PRIMARY, font=MONO)
        label2_v3.next_to(v3_end, DOWN, buff=0.1)
        
        label2_v4 = Text("v₂", font_size=14, color=SECONDARY, font=MONO)
        label2_v4.next_to(v4_end, RIGHT, buff=0.1)
        
        desc2_title = Text("Ortogonais", font_size=22, color=PINK, font=MONO)
        desc2_title.shift(RIGHT * 3 + UP * 1.5)
        
        desc2_text = VGroup(
            Text("θ = 90°", font_size=16, color=WHITE, font=MONO),
            Text("cos(θ) = 0", font_size=16, color=PINK, font=MONO),
            Text("Sem relação (independentes)", font_size=14, color=GRAY, font=MONO),
        )
        desc2_text.arrange(DOWN, buff=0.1)
        desc2_text.next_to(desc2_title, DOWN, buff=0.3)
        
        self.play(Create(v3_arrow), Create(v4_arrow), run_time=1)
        self.play(Create(angle_arc2), run_time=0.5)
        self.play(FadeIn(label2_v3), FadeIn(label2_v4), run_time=0.3)
        
        self.play(FadeIn(desc2_title), FadeIn(desc2_text), run_time=0.8)
        self.wait(2)
        
        # ===== CASO 3: OPOSTOS =====
        
        # Limpar caso anterior
        self.play(
            FadeOut(v3_arrow), FadeOut(v4_arrow),
            FadeOut(angle_arc2), FadeOut(label2_v3), FadeOut(label2_v4),
            FadeOut(desc2_title), FadeOut(desc2_text),
            run_time=0.5
        )
        
        # Vetores opostos (180°)
        v5_end = axes.c2p(1, 0)   # Direita
        v6_end = axes.c2p(-1, 0)  # Esquerda
        
        v5_arrow = Arrow(
            axes.c2p(0, 0), v5_end,
            color=PRIMARY, buff=0, stroke_width=3
        )
        v6_arrow = Arrow(
            axes.c2p(0, 0), v6_end,
            color=PINK, buff=0, stroke_width=3
        )
        
        # Arco de 180° (semi-círculo)
        angle_arc3 = Arc(
            radius=0.5,
            start_angle=math.radians(0),
            angle=math.radians(180),
            color=ACCENT,
            stroke_width=2
        )
        angle_arc3.move_to(axes.get_origin())
        
        label3_v5 = Text("v₁", font_size=14, color=PRIMARY, font=MONO)
        label3_v5.next_to(v5_end, DOWN, buff=0.1)
        
        label3_v6 = Text("v₂", font_size=14, color=PINK, font=MONO)
        label3_v6.next_to(v6_end, DOWN, buff=0.1)
        
        desc3_title = Text("Opostos", font_size=22, color=ACCENT, font=MONO)
        desc3_title.shift(RIGHT * 3 + UP * 1.5)
        
        desc3_text = VGroup(
            Text("θ = 180°", font_size=16, color=WHITE, font=MONO),
            Text("cos(θ) = -1", font_size=16, color=ACCENT, font=MONO),
            Text("Rei / Rainha, Sim / Não", font_size=14, color=GRAY, font=MONO),
        )
        desc3_text.arrange(DOWN, buff=0.1)
        desc3_text.next_to(desc3_title, DOWN, buff=0.3)
        
        self.play(Create(v5_arrow), Create(v6_arrow), run_time=1)
        self.play(Create(angle_arc3), run_time=0.5)
        self.play(FadeIn(label3_v5), FadeIn(label3_v6), run_time=0.3)
        
        self.play(FadeIn(desc3_title), FadeIn(desc3_text), run_time=0.8)
        self.wait(2)
        
        # ===== RESUMO =====
        
        # Limpar tudo
        self.play(
            FadeOut(axes), FadeOut(circle),
            FadeOut(v5_arrow), FadeOut(v6_arrow),
            FadeOut(angle_arc3), FadeOut(label3_v5), FadeOut(label3_v6),
            FadeOut(desc3_title), FadeOut(desc3_text),
            FadeOut(titulo), FadeOut(subtitulo),
            run_time=0.5
        )
        
        # Resumo final
        resumo_titulo = Text("Resumo", font_size=32, color=WHITE, font=MONO)
        resumo_titulo.to_edge(UP, buff=0.5)
        
        caso1 = VGroup(
            Text("Semelhantes", font_size=20, color=PRIMARY, font=MONO),
            Text("θ pequeno → cos ≈ +1", font_size=16, color=GRAY, font=MONO),
        )
        caso1.arrange(DOWN, buff=0.1)
        caso1.shift(LEFT * 3.5)
        
        caso2 = VGroup(
            Text("Ortogonais", font_size=20, color=PINK, font=MONO),
            Text("θ = 90°  → cos = 0", font_size=16, color=GRAY, font=MONO),
        )
        caso2.arrange(DOWN, buff=0.1)
        caso2.center()
        
        caso3 = VGroup(
            Text("Opostos", font_size=20, color=ACCENT, font=MONO),
            Text("θ = 180° → cos = -1", font_size=16, color=GRAY, font=MONO),
        )
        caso3.arrange(DOWN, buff=0.1)
        caso3.shift(RIGHT * 3.5)
        
        # Destaque final
        destaque = Text("Não importa o tamanho, importa a DIREÇÃO", font_size=18, color=SECONDARY, font=MONO)
        destaque.to_edge(DOWN, buff=0.5)
        
        self.play(FadeIn(resumo_titulo), run_time=0.5)
        self.play(FadeIn(caso1), FadeIn(caso2), FadeIn(caso3), run_time=1)
        self.play(FadeIn(destaque), run_time=0.5)
        
        self.wait(3)


if __name__ == "__main__":
    print("\nPara renderizar:")
    print("    source ~/manim-env/bin/activate")
    print("    manim -qh angle_cosine_demo.py AngleCosineDemo")
    print("\nSaída: media/videos/angle_cosine_demo/1080p60/AngleCosineDemo.mp4")