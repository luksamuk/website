"""
Mini-Aula S05: Estrutura de um Agente — 8 cenas (v3)
Paleta: BG=#0D1117 (GitHub Dark), Catppuccin Mocha Surface0=#313244 para code blocks
Code blocks: Manim Code() com formatter_style="monokai", background_config custom
ACENTOS: Você é, não, próxima, grátis, etc — sempre com acento nos slides.
SEM FADE-OUT — TTS sync facilitado.
Código grande: scale=0.55 mínimo nos slides de código.
DoubleArrow: tip_length=0.2 sempre.
FORMA SEGUE FUNÇÃO: cada elemento visual serve a um propósito explicativo.
Barras: align_to(LEFT baseline), nunca centralizadas.
Labels: alinhados em coluna vertical consistente, nunca flutuantes.
"""
from manim import *

# ── Colors & Constants ──────────────────────────────────────────────
BG = "#0D1117"
PRIMARY = "#58A6FF"
SECONDARY = "#7EE787"
ACCENT = "#F0883E"
PURPLE = "#BC8CFF"
PINK = "#FF6B9D"
WHITE = "#E6EDF3"
GRAY = "#8B949E"
DARK_CARD = "#161B22"
BORDER = "#30363D"
CODE_BG = "#313244"
CODE_BORDER = "#45475a"
CODE_FILL_OPACITY = 0.95

MONO = "JetBrains Mono"

CODE_CONFIG = {
    "fill_color": CODE_BG,
    "stroke_color": CODE_BORDER,
    "stroke_width": 1,
    "fill_opacity": CODE_FILL_OPACITY,
    "corner_radius": 0.15,
    "buff": 0.3,
}


# ── Helpers ──────────────────────────────────────────────────────────
def pill_badge(text, fill_color=ACCENT, text_color="#000000", font_size=28):
    txt = Text(text, font_size=font_size, color=text_color, weight=BOLD, font=MONO)
    bg = RoundedRectangle(
        corner_radius=0.3, fill_color=fill_color, fill_opacity=1.0,
        stroke_width=0, width=txt.width + 0.4, height=txt.height + 0.25,
    )
    bg.move_to(txt.get_center())
    return VGroup(bg, txt)


def neon_badge(text, border_color=SECONDARY, font_size=22):
    txt = Text(text, font_size=font_size, color=border_color, font=MONO)
    bg = RoundedRectangle(
        corner_radius=0.15, fill_color=BG, fill_opacity=0.9,
        stroke_color=border_color, stroke_width=2,
        width=txt.width + 0.35, height=txt.height + 0.2,
    )
    bg.move_to(txt.get_center())
    return VGroup(bg, txt)


def make_code(code_str, language="python", scale=0.55, add_line_numbers=False):
    cb = Code(
        code_string=code_str,
        language=language,
        formatter_style="monokai",
        background="rectangle",
        background_config=CODE_CONFIG,
        add_line_numbers=add_line_numbers,
    )
    cb.scale(scale)
    return cb


def bar_left_aligned(width, height, color, x_start, y_pos):
    """Rectangle whose LEFT edge is at x_start, centered vertically at y_pos."""
    bar = Rectangle(width=width, height=height, fill_color=color,
                    fill_opacity=0.8, stroke_width=0)
    bar.move_to(x_start * RIGHT + width * RIGHT / 2 + y_pos * UP)
    return bar


def scene_title(text, color=WHITE, font_size=36):
    """Create a centered title for scene transitions."""
    title = Text(text, font_size=font_size, color=color, weight=BOLD, font=MONO)
    title.move_to(ORIGIN)
    return title


# ════════════════════════════════════════════════════════════════════
# SCENE 1 — Abertura (~10s)
# ════════════════════════════════════════════════════════════════════
class S05_Scene1_Abertura(Scene):
    def construct(self):
        self.camera.background_color = BG

        logo = Text("GUILDA DE IA", font_size=56, color=PRIMARY, weight=BOLD, font=MONO)
        logo.move_to(UP * 2.0)

        badge = pill_badge("AULA 05", fill_color=ACCENT, text_color="#000000", font_size=32)
        badge.move_to(UP * 0.6)

        subtitle = Text("Estrutura de um Agente", font_size=30, color=WHITE, font=MONO)
        subtitle.move_to(DOWN * 0.6)

        tag1 = neon_badge("Fundamentos", border_color=SECONDARY, font_size=18)
        tag2 = neon_badge("Python / APIs", border_color=ACCENT, font_size=18)
        tag3 = neon_badge("Agentes", border_color=PURPLE, font_size=18)
        tags = VGroup(tag1, tag2, tag3).arrange(RIGHT, buff=0.4)
        tags.move_to(DOWN * 2.0)

        self.play(Write(logo), run_time=1.5)
        self.wait(0.3)
        self.play(FadeIn(badge), run_time=0.8)
        self.wait(0.3)
        self.play(Write(subtitle), run_time=0.8)
        self.play(FadeIn(tag3), run_time=0.5)
        self.play(FadeIn(tag1), FadeIn(tag2), run_time=0.5)
        self.wait(2.0)


# ════════════════════════════════════════════════════════════════════
# SCENE 2 — Hook: LLM ≠ Agente (~15s)
# Lado esquerdo: LLM simples (cinza) com pergunta→resposta
# Lado direito: harness envolvendo LLM + 3 badges interconectados
# Seta pulsante LLM→Agente. Equação embaixo.
# ════════════════════════════════════════════════════════════════════
class S05_Scene2_Hook(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Title
        title = scene_title("LLM ≠ Agente", color=ACCENT, font_size=32)
        self.play(Write(title), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(title), run_time=0.5)

        # ─ Left side: LLM alone (gray, dull) ─
        llm_box = Rectangle(width=2.5, height=1.8, fill_color=DARK_CARD,
                           fill_opacity=0.8, stroke_color=GRAY, stroke_width=2)
        llm_box.move_to(LEFT * 4.5 + UP * 0.3)
        llm_label = Text("LLM", font_size=36, color=GRAY, weight=BOLD, font=MONO)
        llm_label.move_to(llm_box.get_center())

        # Arrow from left into box
        ask_arrow = Arrow(LEFT * 6.5 + UP * 0.3, llm_box.get_left(),
                          stroke_width=3, color=GRAY, tip_length=0.2)
        ask_text = Text("pergunta", font_size=14, color=GRAY, font=MONO)
        ask_text.next_to(ask_arrow, DOWN, buff=0.15)

        # Arrow from box to right
        resp_arrow = Arrow(llm_box.get_right(), LEFT * 2.2 + UP * 0.3,
                           stroke_width=3, color=GRAY, tip_length=0.2)
        resp_text = Text("resposta", font_size=14, color=GRAY, font=MONO)
        resp_text.next_to(resp_arrow, DOWN, buff=0.15)

        # ─ Right side: LLM + harness ─
        # Outer harness box (solid, blue border)
        harness_box = Rectangle(width=4.5, height=3.8, fill_color=DARK_CARD,
                                fill_opacity=0.6, stroke_color=PRIMARY, stroke_width=2)
        harness_box.move_to(RIGHT * 2.0 + UP * 0.3)

        # LLM box inside harness (top center)
        llm_inner = Rectangle(width=2.0, height=0.85, fill_color=CODE_BG,
                               fill_opacity=0.9, stroke_color=PRIMARY, stroke_width=2)
        llm_inner.move_to(RIGHT * 2.0 + UP * 1.4)
        llm_inner_label = Text("LLM", font_size=22, color=PRIMARY, weight=BOLD, font=MONO)
        llm_inner_label.move_to(llm_inner.get_center())

        # Three component badges inside harness (below LLM, in a row)
        mem = neon_badge("memória", border_color=SECONDARY, font_size=17)
        inst = neon_badge("instruções", border_color=ACCENT, font_size=17)
        ferr = neon_badge("ferramentas", border_color=PURPLE, font_size=17)
        inner_tags = VGroup(mem, inst, ferr).arrange(RIGHT, buff=0.25)
        inner_tags.move_to(RIGHT * 2.0 + DOWN * 0.3)

        # Connecting lines from LLM box down to each badge
        line_mem = Line(llm_inner.get_bottom() + LEFT * 0.4, mem.get_top(),
                        stroke_width=1.5, color=GRAY)
        line_inst = Line(llm_inner.get_bottom(), inst.get_top(),
                         stroke_width=1.5, color=GRAY)
        line_ferr = Line(llm_inner.get_bottom() + RIGHT * 0.4, ferr.get_top(),
                         stroke_width=1.5, color=GRAY)

        # Harness label
        harness_label = Text("harness", font_size=16, color=PRIMARY, font=MONO, weight=BOLD)
        harness_label.move_to(RIGHT * 2.0 + DOWN * 1.4)

        # Arrow between sides — closer to center
        big_arrow = Arrow(LEFT * 1.5 + UP * 0.3, LEFT * 0.0 + UP * 0.3,
                          stroke_width=4, color=ACCENT, tip_length=0.3)

        # Equation badge at bottom
        eq_badge = pill_badge("Agente = LLM + harness", fill_color=DARK_CARD,
                              text_color=PRIMARY, font_size=22)
        eq_badge.move_to(DOWN * 3.0)

        # ─ Animate left side (dull) ─
        self.play(Create(llm_box), Write(llm_label), run_time=1.0)
        self.play(GrowArrow(ask_arrow), Write(ask_text), run_time=0.5)
        self.play(GrowArrow(resp_arrow), Write(resp_text), run_time=0.5)
        self.wait(0.5)

        # ─ Animate right side (colorful) ─
        self.play(Create(harness_box), run_time=0.8)
        self.play(Create(llm_inner), Write(llm_inner_label), run_time=0.6)
        self.play(FadeIn(mem, inst, ferr), run_time=0.6)
        self.play(Create(line_mem), Create(line_inst), Create(line_ferr), run_time=0.5)
        self.play(Write(harness_label), run_time=0.4)
        self.wait(0.3)

        self.play(GrowArrow(big_arrow), run_time=0.8)
        self.play(FadeIn(eq_badge), run_time=0.8)
        self.wait(8.5)  # extra time for audio


# ════════════════════════════════════════════════════════════════════
# SCENE 3 — 4 Componentes (~18s)
# Vertical stack: boxes aligned LEFT with descriptions right-aligned
# Loop arrow on far right showing Output → Memória
# ════════════════════════════════════════════════════════════════════
class S05_Scene3_Componentes(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Title
        title = scene_title("4 Componentes", color=SECONDARY, font_size=32)
        self.play(Write(title), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(title), run_time=0.5)

        # Common center for diagram — boxes centered, descriptions to the right
        box_center_x = -1.5
        desc_left_x = 1.2

        specs = [
            ("System Prompt", "Quem o agente é", PINK, UP * 2.0),
            ("Memória", "O que já foi dito", SECONDARY, UP * 0.5),
            ("Input", "A pergunta atual", PRIMARY, DOWN * 1.0),
            ("Output", "A resposta", ACCENT, DOWN * 2.5),
        ]

        boxes = []
        descs = []
        for label, desc, color, y_pos in specs:
            # Box: centered at box_center_x
            box = Rectangle(width=3.2, height=0.9, fill_color=DARK_CARD,
                             fill_opacity=0.8, stroke_color=color, stroke_width=2)
            box.move_to(box_center_x * RIGHT + y_pos)
            label_t = Text(label, font_size=20, color=color, weight=BOLD, font=MONO)
            label_t.move_to(box.get_center())

            # Description: left-aligned at desc column
            desc_anchor = Dot(radius=0.001).move_to(desc_left_x * RIGHT + y_pos)
            desc_t = Text(desc, font_size=17, color=WHITE, font=MONO)
            desc_t.move_to(y_pos)
            desc_t.align_to(desc_anchor, LEFT)

            boxes.append(VGroup(box, label_t))
            descs.append(desc_t)

        # Animate each box + description together
        for box_grp, desc_t in zip(boxes, descs):
            self.play(FadeIn(box_grp), Write(desc_t), run_time=0.7)
            self.wait(0.3)

        self.wait(0.5)

        # Loop arrow: Output → Memória — LEFT side of boxes
        # Arrow starts near Output (bottom-left) and curves outward to the left up to Memória (top-left)
        arrow_x = box_center_x - 3.2 / 2 - 0.6  # just left of box left edge
        loop_arrow = CurvedArrow(
            arrow_x * RIGHT + DOWN * 2.3,
            arrow_x * RIGHT + UP * 0.7,
            color=SECONDARY, stroke_width=3, tip_length=0.2,
            angle=-0.5  # negative angle = curve bulges LEFT (away from boxes)
        )
        # Label to the left of the arrow (outside the curve, further left)
        loop_label = Text("volta pra\nmemória", font_size=14, color=SECONDARY, font=MONO)
        loop_label.move_to((arrow_x - 1.5) * RIGHT + DOWN * 0.8)

        self.play(Create(loop_arrow), run_time=1.0)
        self.play(Write(loop_label), run_time=0.6)
        self.wait(8.5)  # extra time for audio


# ════════════════════════════════════════════════════════════════════
# SCENE 4 — Agente na mão (~20s)
# Pseudocode on left, bullets on right — split layout
# Transition to second function with same pattern
# ════════════════════════════════════════════════════════════════════
class S05_Scene4_AgenteNaMao(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Title
        title = scene_title("Agente na mão", color=ACCENT, font_size=32)
        self.play(Write(title), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(title), run_time=0.5)

        # ── Part 1: criar_agente ──
        pseudo_str1 = """def criar_agente(instrucoes, max=20):
    return {
        "instrucoes": instrucoes,
        "historico": [],
        "max_historico": max
    }"""
        code1 = make_code(pseudo_str1, scale=0.75)
        code1.move_to(LEFT * 3.2 + UP * 0.3)

        bullets1_left = UP * 1.2
        bullets1_right = DOWN * 2.2
        b1 = VGroup(
            Text("• instruções", font_size=18, color=PINK, font=MONO),
            Text("• histórico vazio", font_size=18, color=SECONDARY, font=MONO),
            Text("• limite de mensagens", font_size=18, color=SECONDARY, font=MONO),
            Text("• Sem classes. Sem objs.", font_size=16, color=GRAY, font=MONO),
            Text("• Só dicts e funções", font_size=16, color=GRAY, font=MONO),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        b1.move_to(RIGHT * 3.0 + DOWN * 0.3)

        badge1 = neon_badge("truncar histórico", border_color=SECONDARY, font_size=16)
        badge1.move_to(RIGHT * 3.0 + DOWN * 2.5)

        self.play(FadeIn(code1), run_time=1.5)
        self.wait(0.5)
        for b in b1:
            self.play(Write(b), run_time=0.35)
        self.play(FadeIn(badge1), run_time=0.5)
        self.wait(1.0)

        # ── Transition: slide left, fade out, show conversar ──
        self.play(VGroup(code1, b1, badge1).animate.shift(LEFT * 4.0), run_time=0.8)
        self.play(FadeOut(code1, b1, badge1), run_time=0.4)

        # ── Part 2: conversar ──
        pseudo_str2 = """conversar(agente, msg):
  msgs = system + historico
  msgs.append(pergunta)
  resposta = LLM(msgs)
  historico.append(pergunta)
  historico.append(resposta)"""
        code2 = make_code(pseudo_str2, scale=0.65)
        code2.move_to(LEFT * 3.2 + UP * 0.3)

        b2 = VGroup(
            Text("• system prompt no topo", font_size=18, color=PINK, font=MONO),
            Text("• histórico truncado", font_size=18, color=SECONDARY, font=MONO),
            Text("• pergunta no final", font_size=18, color=PRIMARY, font=MONO),
            Text("• resposta volta pro histórico", font_size=16, color=ACCENT, font=MONO),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        b2.move_to(RIGHT * 3.0 + DOWN * 0.3)

        self.play(FadeIn(code2), run_time=1.5)
        for b in b2:
            self.play(Write(b), run_time=0.35)
        self.wait(4.9)  # extra time for audio


# ════════════════════════════════════════════════════════════════════
# SCENE 5a — Limite de contexto (~10s)
# Bars growing → truncation
# ════════════════════════════════════════════════════════════════════
class S05_Scene5a_Contexto(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Title
        title = scene_title("Limite de contexto", color=ACCENT, font_size=32)
        self.play(Write(title), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(title), run_time=0.5)

        baseline_x = -5.5
        w1, w2, w3 = 2.0, 5.5, 9.5

        bar1 = Rectangle(width=w1, height=0.6, fill_color=SECONDARY,
                          fill_opacity=0.8, stroke_width=0)
        bar1.move_to(baseline_x * RIGHT + (w1 / 2) * RIGHT + UP * 1.5)
        label1 = Text("histórico pequeno", font_size=16, color=SECONDARY, font=MONO)
        label1.next_to(bar1, RIGHT, buff=0.3)

        bar2 = Rectangle(width=w2, height=0.6, fill_color=ACCENT,
                          fill_opacity=0.8, stroke_width=0)
        bar2.move_to(baseline_x * RIGHT + (w2 / 2) * RIGHT + UP * 0.3)
        label2 = Text("histórico médio", font_size=16, color=ACCENT, font=MONO)
        label2.next_to(bar2, RIGHT, buff=0.3)

        bar3 = Rectangle(width=w3, height=0.6, fill_color=PINK,
                          fill_opacity=0.8, stroke_width=0)
        bar3.move_to(baseline_x * RIGHT + (w3 / 2) * RIGHT + DOWN * 0.9)
        label3 = Text("histórico gigante", font_size=16, color=PINK, font=MONO)
        label3.next_to(bar3, RIGHT, buff=0.3)

        # Token count arrow
        tokens_arrow = DoubleArrow(LEFT * 5.5 + DOWN * 2.0, LEFT * 5.5 + (w3 / 2 - 1) * LEFT * (-1) + DOWN * 2.0,
                                    stroke_width=2, color=WHITE, tip_length=0.2)
        tokens_text = Text("tokens ↑↑↑", font_size=20, color=WHITE, weight=BOLD, font=MONO)
        tokens_text.next_to(tokens_arrow, DOWN, buff=0.2)

        # Limit line
        limit_line = DashedLine(LEFT * 0.5 + UP * 2.0, LEFT * 0.5 + DOWN * 2.5,
                                stroke_width=2, color=RED)
        limit_label = Text("limite", font_size=18, color=RED, font=MONO)
        limit_label.next_to(limit_line, UP, buff=0.15)

        # Truncation badge
        trunc_badge = neon_badge("truncar", border_color=SECONDARY, font_size=18)
        trunc_badge.move_to(DOWN * 3.5)

        # Animate
        self.play(FadeIn(bar1), Write(label1), run_time=0.8)
        self.play(FadeIn(bar2), Write(label2), run_time=0.8)
        self.play(FadeIn(bar3), Write(label3), run_time=0.8)
        self.play(Create(tokens_arrow), Write(tokens_text), run_time=0.6)
        self.play(Create(limit_line), Write(limit_label), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(trunc_badge), run_time=0.6)
        self.wait(1.5)


# ════════════════════════════════════════════════════════════════════
# SCENE 5b — Lost in the Middle (~8s)
# ✓ inicio  ✗ meio  ✓ fim
# ════════════════════════════════════════════════════════════════════
class S05_Scene5b_LiTM(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Title
        title = scene_title("Por que truncar?", color=ACCENT, font_size=32)
        self.play(Write(title), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(title), run_time=0.5)

        # All bars start at same LEFT x baseline
        baseline_x = -5.5

        # Bar 1: small (green)
        w1, w2, w3 = 2.0, 5.5, 9.5
        common_y_spacing = 1.2

        bar1 = Rectangle(width=w1, height=0.6, fill_color=SECONDARY,
                          fill_opacity=0.8, stroke_width=0)
        bar1.move_to(baseline_x * RIGHT + (w1 / 2) * RIGHT + UP * 2.0)
        label1 = Text("histórico pequeno", font_size=16, color=SECONDARY, font=MONO)
        label1.next_to(bar1, RIGHT, buff=0.3)

        bar2 = Rectangle(width=w2, height=0.6, fill_color=ACCENT,
                          fill_opacity=0.8, stroke_width=0)
        bar2.move_to(baseline_x * RIGHT + (w2 / 2) * RIGHT + UP * 0.8)
        label2 = Text("histórico médio", font_size=16, color=ACCENT, font=MONO)
        label2.next_to(bar2, RIGHT, buff=0.3)

        bar3 = Rectangle(width=w3, height=0.6, fill_color=PINK,
                          fill_opacity=0.8, stroke_width=0)
        bar3.move_to(baseline_x * RIGHT + (w3 / 2) * RIGHT + DOWN * 0.4)
        label3 = Text("histórico gigante", font_size=16, color=PINK, font=MONO)
        label3.next_to(bar3, RIGHT, buff=0.3)

        # Double arrow "tokens"
        tokens_arrow = DoubleArrow(LEFT * 5.5 + DOWN * 1.4, LEFT * 5.5 + (w3 / 2 - 1) * LEFT * (-1) + DOWN * 1.4,
                                    stroke_width=2, color=WHITE, tip_length=0.2)
        tokens_text = Text("tokens ↑↑↑", font_size=20, color=WHITE, weight=BOLD, font=MONO)
        tokens_text.next_to(tokens_arrow, DOWN, buff=0.2)

        # Title + citation together
        litm_title = Text("Lost in the Middle", font_size=34, color=WHITE,
                           weight=BOLD, font=MONO)
        litm_ref = Text("(Liu et al., 2023)", font_size=16, color=GRAY, font=MONO)
        litm_group = VGroup(litm_title, litm_ref).arrange(DOWN, buff=0.15)
        litm_group.move_to(DOWN * 2.5)

        # Diagram: ✓ início  ✗ meio  ✓ fim
        ok_start = Text("✓ início", font_size=18, color=SECONDARY, font=MONO)
        bad_mid = Text("✗ meio", font_size=18, color=PINK, font=MONO)
        ok_end = Text("✓ fim", font_size=18, color=SECONDARY, font=MONO)
        diag = VGroup(ok_start, bad_mid, ok_end).arrange(RIGHT, buff=1.5)
        diag.move_to(DOWN * 3.5)

        # Animate
        self.play(FadeIn(bar1), Write(label1), run_time=0.8)
        self.play(FadeIn(bar2), Write(label2), run_time=0.8)
        self.play(FadeIn(bar3), Write(label3), run_time=0.8)
        self.play(Create(tokens_arrow), Write(tokens_text), run_time=0.6)
        self.wait(0.5)

        self.play(Write(litm_group), run_time=1.0)
        self.play(Write(ok_start), Write(bad_mid), Write(ok_end), run_time=0.8)
        self.wait(2.5)


# ════════════════════════════════════════════════════════════════════
# SCENE 5c — Compactação (~10s)
# Show compaction: middle messages → hidden session → summary replaces middle
# ════════════════════════════════════════════════════════════════════
class S05_Scene5c_Compactacao(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Title
        title = scene_title("Compactação", color=SECONDARY, font_size=32)
        self.play(Write(title), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(title), run_time=0.5)

        # ── Left side: 5 message blocks centered at ORIGIN ──
        msg_colors = [SECONDARY, PINK, PINK, PINK, SECONDARY]
        msg_labels = ["msg 1 (início)", "msg 2", "msg 3", "msg 4", "msg 5 (fim)"]
        msgs = []
        y_spacing = 0.85
        left_x = -4.0

        # 5 boxes: center vertically so midpoint is at y=0
        # Positions: +2*spacing, +1*spacing, 0, -1*spacing, -2*spacing
        for i, (label, color) in enumerate(zip(msg_labels, msg_colors)):
            y_pos = (2 - i) * y_spacing  # +1.7, +0.85, 0, -0.85, -1.7
            box = Rectangle(width=3.4, height=0.65, fill_color=DARK_CARD,
                           fill_opacity=0.8, stroke_color=color, stroke_width=2)
            box.move_to(left_x * RIGHT + y_pos * UP)
            txt = Text(label, font_size=13, color=color, font=MONO)
            txt.move_to(box.get_center())
            msgs.append(VGroup(box, txt))

        for msg in msgs:
            self.play(FadeIn(msg), run_time=0.3)

        self.wait(0.5)

        # Highlight middle messages (indices 1,2,3) with a dashed box
        mid_group = VGroup(msgs[1], msgs[2], msgs[3])
        mid_box_rect = Rectangle(width=3.6, height=2.4, stroke_color=ACCENT, stroke_width=2)
        mid_box_rect.move_to(mid_group.get_center())
        mid_box = DashedVMobject(mid_box_rect)
        self.play(Create(mid_box), run_time=0.8)

        # Arrow pointing right with label
        arrow_start = mid_group.get_center() + RIGHT * 2.5
        arrow_end = mid_group.get_center() + RIGHT * 3.8
        arrow_right = Arrow(arrow_start, arrow_end,
                           stroke_width=3, color=ACCENT, tip_length=0.2)
        summarize_label = Text("sessão\noculta", font_size=14, color=ACCENT, font=MONO)
        summarize_label.next_to(arrow_right, UP, buff=0.15)
        self.play(GrowArrow(arrow_right), Write(summarize_label), run_time=0.8)

        self.wait(1.0)

        # ── Right side: compacted result — 3 messages centered at ORIGIN ──
        result_labels = ["msg 1 (início)", "resumo", "msg 5 (fim)"]
        result_colors = [SECONDARY, ACCENT, SECONDARY]
        result_msgs = []
        right_x = 4.0

        # 3 boxes: center at y=0, same spacing as left
        for i, (label, color) in enumerate(zip(result_labels, result_colors)):
            y_pos = (1 - i) * y_spacing  # +0.85, 0, -0.85
            box = Rectangle(width=3.4, height=0.65, fill_color=DARK_CARD,
                           fill_opacity=0.8, stroke_color=color, stroke_width=2)
            box.move_to(right_x * RIGHT + y_pos * UP)
            txt = Text(label, font_size=13, color=color, font=MONO)
            txt.move_to(box.get_center())
            result_msgs.append(VGroup(box, txt))

        for rmsg in result_msgs:
            self.play(FadeIn(rmsg), run_time=0.5)

        # Arrow from left column to right column, at y=0
        arrow_result = Arrow(
            left_x * RIGHT + RIGHT * 1.8,
            right_x * RIGHT + LEFT * 1.8,
            stroke_width=3, color=WHITE, tip_length=0.2
        )
        self.play(GrowArrow(arrow_result), run_time=0.6)

        self.wait(0.5)

        # Badge: "compactação"
        badge = neon_badge("compactação", border_color=SECONDARY, font_size=18)
        badge.move_to(DOWN * 2.6)
        self.play(FadeIn(badge), run_time=0.6)
        self.wait(2.0)  # time for explanation


# ════════════════════════════════════════════════════════════════════
# SCENE 6 — ReAct: Pensar e Agir (~18s)
# Cycle diagram on left, shifts right, example on left
# ════════════════════════════════════════════════════════════════════
class S05_Scene6_ReAct(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Title
        title = scene_title("ReAct: Pensar e Agir", color=PURPLE, font_size=32)
        self.play(Write(title), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(title), run_time=0.5)

        # Cycle nodes — arranged in a diamond/rhombus pattern, compact
        labels_colors = [
            ("Input", PRIMARY),
            ("Thought", PURPLE),
            ("Action", ACCENT),
            ("Observation", SECONDARY),
        ]

        # Compact positions in left half
        positions = [
            LEFT * 4.0 + UP * 1.5,   # Input (left-top)
            UP * 3.0,                   # Thought (top-center)
            RIGHT * 4.0 + UP * 1.5,    # Action (right-top) — will move later
            DOWN * 0.5,                 # Observation (center-bottom)
        ]

        nodes = []
        for (label, color), pos in zip(labels_colors, positions):
            circle = Circle(radius=0.65, fill_color=DARK_CARD, fill_opacity=0.9,
                           stroke_color=color, stroke_width=3)
            circle.move_to(pos)
            txt = Text(label, font_size=16, color=color, weight=BOLD, font=MONO)
            txt.move_to(pos)
            node = VGroup(circle, txt)
            nodes.append(node)

        # Arrows: Input→Thought→Action→Observation→Thought (loop)
        arrows = [
            Arrow(nodes[0].get_right() + UP * 0.15, nodes[1].get_left() + DOWN * 0.1,
                  stroke_width=3, color=PRIMARY, tip_length=0.2),
            Arrow(nodes[1].get_right() + DOWN * 0.1, nodes[2].get_left() + UP * 0.15,
                  stroke_width=3, color=PURPLE, tip_length=0.2),
            Arrow(nodes[2].get_bottom() + LEFT * 0.2, nodes[3].get_right() + UP * 0.1,
                  stroke_width=3, color=ACCENT, tip_length=0.2),
            CurvedArrow(nodes[3].get_top() + LEFT * 0.3, nodes[1].get_bottom() + LEFT * 0.3,
                        stroke_width=3, color=SECONDARY, tip_length=0.2, angle=-0.5),
        ]

        cycle_group = VGroup(*nodes, *arrows)

        for node in nodes:
            self.play(FadeIn(node), run_time=0.4)
        for arrow in arrows:
            self.play(Create(arrow), run_time=0.5)
        self.wait(0.8)

        # Transition: shift cycle right, show example on left
        self.play(cycle_group.animate.shift(RIGHT * 5.5), run_time=0.8)

        # Example text on left — moved up to avoid bottom cutoff
        example_lines = [
            ("? = 234 × 987 + 100", WHITE, UP * 1.5),
            ("💭 Preciso multiplicar", PURPLE, UP * 0.7),
            ("🔧 calculadora[234 × 987]", ACCENT, DOWN * 0.1),
            ("     → 230958", GRAY, DOWN * 0.7),
            ("💭 Agora somo 100", PURPLE, DOWN * 1.5),
            ("✅ 231058", SECONDARY, DOWN * 2.3),
        ]

        example_texts = []
        for text, color, pos in example_lines:
            t = Text(text, font_size=17, color=color, font=MONO)
            t.move_to(LEFT * 2.0 + pos)
            example_texts.append(t)
            self.play(Write(t), run_time=0.4)

        self.wait(0.5)

        # Badges — moved up to stay in frame
        badge1 = neon_badge("hoje: memória + instruções", border_color=PURPLE, font_size=16)
        badge1.move_to(DOWN * 2.9 + LEFT * 2.0)
        badge2 = neon_badge("S06: ferramentas!", border_color=ACCENT, font_size=16)
        badge2.next_to(badge1, RIGHT, buff=0.3)
        self.play(FadeIn(badge1, badge2), run_time=0.6)
        self.wait(6.8)  # extra time for audio


# ════════════════════════════════════════════════════════════════════
# SCENE 7 — De Requests para LangChain (~12s)
# Two-column comparison, items aligned by column with consistent margins
# ════════════════════════════════════════════════════════════════════
class S05_Scene7_LangChain(Scene):
    def construct(self):
        self.camera.background_color = BG

        # Title
        title = scene_title("De Requests pra LangChain", color=PRIMARY, font_size=28)
        self.play(Write(title), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(title), run_time=0.5)

        # Column LEFT EDGES (not centers) — text aligns LEFT from here
        # Screen width ~14 units (-7 to 7). Left col: -6.5 to -0.3, Right col: 0.3 to 6.5
        left_edge = -6.3
        right_edge = 0.4
        separator_x = 0

        # Header row — also LEFT-aligned to same edge
        h_left = Text("Na mão (requests)", font_size=20, color=PRIMARY, weight=BOLD, font=MONO)
        h_left.move_to(UP * 3.0)
        h_left.align_to(Dot(radius=0.001).move_to(left_edge * RIGHT), LEFT)
        h_right = Text("Com LangChain", font_size=20, color=SECONDARY, weight=BOLD, font=MONO)
        h_right.move_to(UP * 3.0)
        h_right.align_to(Dot(radius=0.001).move_to(right_edge * RIGHT), LEFT)

        sep = Line(UP * 2.5, DOWN * 1.5, stroke_width=1, color=BORDER)
        sep.move_to(separator_x * RIGHT)

        self.play(Write(h_left), Write(h_right), Create(sep), run_time=1.0)
        self.wait(0.3)

        # Data rows — left text aligned to common LEFT edge, right text too
        rows = [
            ("Montar dict manual", "ChatPromptTemplate"),
            ("Histórico manual", "InMemoryChatMessageHistory"),
            ("Chamar e parsear", "ChatOpenAI"),
            ("[-N:] manual", "Configurável"),
        ]

        # Anchors at the LEFT edge of each column
        left_anchor = Dot(radius=0.001).move_to(left_edge * RIGHT)
        right_anchor = Dot(radius=0.001).move_to(right_edge * RIGHT)

        for i, (left_text, right_text) in enumerate(rows):
            y_pos = UP * 1.8 - i * 1.2
            lt = Text(left_text, font_size=16, color=GRAY, font=MONO)
            lt.move_to(y_pos)
            lt.align_to(left_anchor, LEFT)
            rt = Text(right_text, font_size=16, color=SECONDARY, font=MONO)
            rt.move_to(y_pos)
            rt.align_to(right_anchor, LEFT)
            # Each row starts at the same y_pos for both sides
            self.play(Write(lt), Write(rt), run_time=0.8)
            self.wait(0.2)

        self.wait(0.5)

        # Pipe badge
        pipe_text = Text("prompt | llm", font_size=24, color=WHITE, weight=BOLD, font=MONO)
        pipe_text.move_to(DOWN * 3.0)
        pipe_badge = neon_badge("pipe = encadeia", border_color=PRIMARY, font_size=16)
        pipe_badge.next_to(pipe_text, RIGHT, buff=0.4)

        self.play(Write(pipe_text), run_time=0.8)
        self.play(FadeIn(pipe_badge), run_time=0.5)
        self.wait(5.7)  # extra time for audio


# ════════════════════════════════════════════════════════════════════
# SCENE 8 — CTA (~10s)
# ════════════════════════════════════════════════════════════════════
class S05_Scene8_CTA(Scene):
    def construct(self):
        self.camera.background_color = BG

        badge = pill_badge("AULA 05", fill_color=ACCENT, text_color="#000000", font_size=32)
        badge.move_to(UP * 1.5)

        link = Text("Apostila + Slides + Colab", font_size=24, color=WHITE, font=MONO)
        link.move_to(UP * 0.3)
        url = Text("luksamuk.codes/pages/guilda-ia", font_size=18, color=GRAY, font=MONO)
        url.move_to(DOWN * 0.3)

        logo = Text("GUILDA DE IA", font_size=40, color=PRIMARY, weight=BOLD, font=MONO)
        logo.move_to(DOWN * 1.8)

        self.play(FadeIn(badge), run_time=0.8)
        self.play(Write(link), run_time=0.6)
        self.play(Write(url), run_time=0.5)
        self.wait(0.5)
        self.play(Write(logo), run_time=1.0)
        self.wait(2.0)