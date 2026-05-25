"""
Mini-Aula S04: Python + API de LLM — v7 (11 cenas)
Paleta: BG=#0D1117 (GitHub Dark), Catppuccin Mocha Surface0=#313244 para code blocks
Code blocks: Manim Code() com formatter_style="monokai", background_config custom
ACENTOS: Você é, não, próxima, grátis, etc — sempre com acento nos slides.
URLs: Todas usam localhost (nunca 127.0.0.1).
Model: gemini-2.5-flash (nunca 2.0).
SEM FADE-OUT — TTS sync facilitado.
Código grande: scale=0.55 mínimo nos slides de código.
"""
from manim import *

# ── Colors & Constants ──────────────────────────────────────────────
BG = "#0D1117"
PRIMARY = "#58A6FF"
SECONDARY = "#7EE787"
ACCENT = "#F0883E"
PURPLE = "#BC8CFF"
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


# ════════════════════════════════════════════════════════════════════
# SCENE 1 — Abertura
# ════════════════════════════════════════════════════════════════════
class S04_Scene1_Abertura(Scene):
    def construct(self):
        self.camera.background_color = BG

        logo = Text("GUILDA DE IA", font_size=56, color=PRIMARY, weight=BOLD, font=MONO)
        logo.move_to(UP * 2.0)

        badge = pill_badge("AULA 04", fill_color=ACCENT, text_color="#000000", font_size=32)
        badge.move_to(UP * 0.6)

        subtitle = Text("Python + API de LLM", font_size=30, color=WHITE, font=MONO)
        subtitle.move_to(DOWN * 0.6)

        tag1 = neon_badge("Fundamentos", border_color=SECONDARY, font_size=18)
        tag2 = neon_badge("Python / APIs", border_color=ACCENT, font_size=18)
        tag3 = neon_badge("RAG / Agentes", border_color=PURPLE, font_size=18)
        tags = VGroup(tag1, tag2, tag3).arrange(RIGHT, buff=0.4)
        tags.move_to(DOWN * 2.0)

        self.play(Write(logo), run_time=1.5)
        self.wait(0.3)
        self.play(FadeIn(badge), run_time=0.8)
        self.play(Write(subtitle), run_time=0.8)
        self.play(FadeIn(tags), run_time=0.8)
        self.wait(1.2)


# ════════════════════════════════════════════════════════════════════
# SCENE 2 — Hook: Pra que Python?
# ════════════════════════════════════════════════════════════════════
class S04_Scene2_Hook(Scene):
    def construct(self):
        self.camera.background_color = BG

        q = Text("Pra que Python?", font_size=44, color=PRIMARY, weight=BOLD, font=MONO)
        q.move_to(UP * 1.2)
        self.play(Write(q), run_time=1.5)
        self.wait(0.5)

        arrow_style = {"color": GRAY, "stroke_width": 3, "max_tip_length_to_length_ratio": 0.15}
        python_label = Text("Python", font_size=28, color=SECONDARY, font=MONO)
        api_label = Text("API", font_size=28, color=ACCENT, weight=BOLD, font=MONO)
        llm_label = Text("LLM", font_size=28, color=PURPLE, font=MONO)

        python_label.move_to(LEFT * 4 + DOWN * 0.5)
        api_label.move_to(ORIGIN + DOWN * 0.5)
        llm_label.move_to(RIGHT * 4 + DOWN * 0.5)

        arrow1 = Arrow(python_label.get_right(), api_label.get_left(), **arrow_style)
        arrow2 = Arrow(api_label.get_right(), llm_label.get_left(), **arrow_style)

        self.play(FadeIn(python_label), run_time=0.6)
        self.wait(0.3)
        self.play(GrowArrow(arrow1), FadeIn(api_label), run_time=0.6)
        self.wait(0.3)
        self.play(GrowArrow(arrow2), FadeIn(llm_label), run_time=0.6)
        self.wait(0.5)

        control = Text("controlar", font_size=36, color=ACCENT, weight=BOLD, font=MONO)
        control.move_to(DOWN * 1.8)
        self.play(Write(control), run_time=0.8)
        self.play(control.animate.scale(1.15).set_color(YELLOW), run_time=0.3)
        self.play(control.animate.scale(1/1.15).set_color(ACCENT), run_time=0.3)
        self.wait(8.0)


# ════════════════════════════════════════════════════════════════════
# SCENE 3 — API = Garçom
# ════════════════════════════════════════════════════════════════════
class S04_Scene3_API_Garcom(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("API = Garçom", font_size=40, color=PRIMARY, weight=BOLD, font=MONO)
        title.move_to(UP * 2.5)
        self.play(Write(title), run_time=1.0)
        self.wait(0.3)

        client_box = Rectangle(width=2.2, height=1.0, fill_color=DARK_CARD, fill_opacity=0.9,
                               stroke_color=SECONDARY, stroke_width=2)
        client_txt = Text("Código", font_size=22, color=SECONDARY, font=MONO)
        client_label = VGroup(client_box, client_txt)
        client_label.move_to(LEFT * 4.5 + DOWN * 0.5)

        api_box = Rectangle(width=2.0, height=1.0, fill_color=DARK_CARD, fill_opacity=0.9,
                            stroke_color=ACCENT, stroke_width=2)
        api_txt = Text("API", font_size=24, color=ACCENT, weight=BOLD, font=MONO)
        api_label = VGroup(api_box, api_txt)
        api_label.move_to(ORIGIN + DOWN * 0.5)

        llm_box = Rectangle(width=2.2, height=1.0, fill_color=DARK_CARD, fill_opacity=0.9,
                            stroke_color=PURPLE, stroke_width=2)
        llm_txt = Text("LLM", font_size=22, color=PURPLE, weight=BOLD, font=MONO)
        llm_label = VGroup(llm_box, llm_txt)
        llm_label.move_to(RIGHT * 4.5 + DOWN * 0.5)

        self.play(FadeIn(client_label), run_time=0.6)
        self.play(FadeIn(api_label), run_time=0.6)
        self.play(FadeIn(llm_label), run_time=0.6)

        req_arrow = Arrow(client_label.get_right(), api_label.get_left(),
                          color=ACCENT, stroke_width=3, max_tip_length_to_length_ratio=0.15)
        req_txt = Text("JSON ▶", font_size=16, color=ACCENT, font=MONO)
        req_txt.next_to(req_arrow, UP, buff=0.15)

        mid_arrow = Arrow(api_label.get_right(), llm_label.get_left(),
                          color=PURPLE, stroke_width=3, max_tip_length_to_length_ratio=0.15)

        self.play(GrowArrow(req_arrow), Write(req_txt), run_time=0.8)
        self.play(GrowArrow(mid_arrow), run_time=0.8)

        quote = Text("Universal: Gemini, Ollama, OpenAI", font_size=20, color=GRAY, font=MONO)
        quote.move_to(DOWN * 2.2)
        self.play(Write(quote), run_time=0.8)
        self.wait(13.5)


# ════════════════════════════════════════════════════════════════════
# SCENE 4 — Cloud vs Local
# ════════════════════════════════════════════════════════════════════
class S04_Scene4_Cloud_vs_Local(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Cloud vs Local", font_size=40, color=PRIMARY, weight=BOLD, font=MONO)
        title.move_to(UP * 2.8)
        self.play(Write(title), run_time=1.0)
        self.wait(0.3)

        col_cloud = Rectangle(width=3.5, height=3.5, fill_color=DARK_CARD, fill_opacity=0.9,
                              stroke_color=PRIMARY, stroke_width=2)
        col_cloud.move_to(LEFT * 3.5 + DOWN * 0.3)

        cloud_title = Text("Gemini", font_size=26, color=PRIMARY, weight=BOLD, font=MONO)
        cloud_title.move_to(col_cloud.get_top() + DOWN * 0.35)

        cloud_items = VGroup(
            Text("100+ tok/s", font_size=18, color=SECONDARY, font=MONO),
            Text("Grátis com limites", font_size=18, color=WHITE, font=MONO),
            Text("Precisa de internet", font_size=18, color=GRAY, font=MONO),
            Text("API key necessária", font_size=18, color=GRAY, font=MONO),
        ).arrange(DOWN, buff=0.25)
        cloud_items.move_to(col_cloud.get_center() + DOWN * 0.3)

        col_local = Rectangle(width=3.5, height=3.5, fill_color=DARK_CARD, fill_opacity=0.9,
                              stroke_color=PURPLE, stroke_width=2)
        col_local.move_to(RIGHT * 3.5 + DOWN * 0.3)

        local_title = Text("Ollama", font_size=26, color=PURPLE, weight=BOLD, font=MONO)
        local_title.move_to(col_local.get_top() + DOWN * 0.35)

        local_items = VGroup(
            Text("80 tok/s", font_size=18, color=SECONDARY, font=MONO),
            Text("100% grátis", font_size=18, color=WHITE, font=MONO),
            Text("Privacidade total", font_size=18, color=GRAY, font=MONO),
            Text("Sem internet*", font_size=18, color=GRAY, font=MONO),
        ).arrange(DOWN, buff=0.25)
        local_items.move_to(col_local.get_center() + DOWN * 0.3)

        center_badge = neon_badge("Mesmo padrão HTTP", border_color=ACCENT, font_size=20)
        center_badge.move_to(DOWN * 2.5)

        footnote = Text("* exceto no Colab, que precisa de internet", font_size=16, color=GRAY, font=MONO)
        footnote.move_to(DOWN * 3.3)

        self.play(FadeIn(col_cloud), Write(cloud_title), run_time=0.8)
        self.play(FadeIn(col_local), Write(local_title), run_time=0.8)
        self.play(FadeIn(cloud_items), run_time=0.8)
        self.play(FadeIn(local_items), run_time=0.8)
        self.play(FadeIn(center_badge), run_time=0.5)
        self.play(FadeIn(footnote), run_time=0.4)
        self.wait(21.3)


# ════════════════════════════════════════════════════════════════════
# SCENE 5 — Código: SDK do Gemini (porção Cloud)
# ════════════════════════════════════════════════════════════════════
class S04_Scene5_Genai(Scene):
    def construct(self):
        self.camera.background_color = BG

        badge = neon_badge("SDK do Google: genai.Client", border_color=PRIMARY, font_size=20)
        badge.move_to(UP * 3.2)

        genai_code = """from google import genai
from google.genai import types
from google.colab import userdata

client = genai.Client(
    api_key=userdata.get('GEMINI_API_KEY')
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Olá! Qual a capital de MG?",
)"""

        code_block = make_code(genai_code, scale=1.0)
        code_block.move_to(UP * 0.0)

        self.play(FadeIn(badge), run_time=0.5)
        self.play(FadeIn(code_block), run_time=1.5)
        self.wait(15.9)


# ════════════════════════════════════════════════════════════════════
# SCENE 6 — Ollama no Colab
# ════════════════════════════════════════════════════════════════════
class S04_Scene6_Colab(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Ollama no Colab", font_size=36, color=PRIMARY, weight=BOLD, font=MONO)
        title.move_to(UP * 2.8)
        self.play(Write(title), run_time=1.0)

        lines_data = [
            ("!nvidia-smi", "GPU T4", SECONDARY),
            ("!ollama pull qwen3.5:4b", "~2.7 GB", ACCENT),
            ("OLLAMA_KEEP_ALIVE = -1", "não descarrega", PURPLE),
        ]

        line_group = VGroup()
        for code_text, badge_text, color in lines_data:
            code_line = Text(code_text, font_size=20, color=WHITE, font=MONO)
            badge_label = neon_badge(badge_text, border_color=color, font_size=14)
            row = VGroup(code_line, badge_label).arrange(RIGHT, buff=0.3)
            line_group.add(row)

        line_group.arrange(DOWN, buff=0.5)
        line_group.move_to(DOWN * 0.3)
        self.play(FadeIn(line_group), run_time=1.2)

        warn = neon_badge("Warm up: ~2-3 min (1ª requisição)", border_color=ACCENT, font_size=16)
        warn.move_to(DOWN * 2.8)
        self.play(FadeIn(warn), run_time=0.5)
        self.wait(17.3)


# ════════════════════════════════════════════════════════════════════
# SCENE 7 — Código: requests.post()
# ════════════════════════════════════════════════════════════════════
class S04_Scene7_Codigo(Scene):
    def construct(self):
        self.camera.background_color = BG

        top_badge = neon_badge("Um único padrão HTTP", border_color=ACCENT, font_size=20)
        top_badge.move_to(UP * 3.2)

        requests_code = """response = requests.post(
    "http://localhost:11434/v1/chat/completions",
    json={
        "model": "qwen3.5:4b",
        "messages": [
            {"role": "user",
             "content": "Capital de MG?"},
        ],
    },
    timeout=120,
)"""

        code_block = make_code(requests_code, scale=1.0)
        code_block.move_to(UP * 0.0)

        self.play(FadeIn(top_badge), run_time=0.5)
        self.play(FadeIn(code_block), run_time=1.5)
        self.wait(10.0)

        ref = Text("Erros (401, 429, 500) → ver apostila", font_size=18, color=GRAY, font=MONO)
        ref.move_to(DOWN * 3.0)
        self.play(Write(ref), run_time=0.6)
        self.wait(16.0)


# ════════════════════════════════════════════════════════════════════
# SCENE 8 — System Prompt + Chat com Memória
# ════════════════════════════════════════════════════════════════════
class S04_Scene8_System_Chat(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Gerenciamento de Mensagens em Código", font_size=28, color=PRIMARY, weight=BOLD, font=MONO)
        title.move_to(UP * 3.2)
        self.play(Write(title), run_time=0.8)

        sys_pill = pill_badge("Você é um tutor de Python", fill_color=ACCENT, text_color="#000000", font_size=22)
        sys_pill.move_to(UP * 2.0)
        label_sys = Text("system prompt", font_size=18, color=GRAY, font=MONO)
        label_sys.next_to(sys_pill, DOWN, buff=0.2)

        self.play(FadeIn(sys_pill), Write(label_sys), run_time=1.0)
        self.wait(0.5)

        msgs_data = [
            ('{ role: "system", ... }', ACCENT),
            ('{ role: "user", ... }', SECONDARY),
            ('{ role: "assistant", ... }', PRIMARY),
            ('{ role: "user", ... }', SECONDARY),
        ]

        msg_group = VGroup()
        start_y = UP * 0.5

        for i, (text_str, color) in enumerate(msgs_data):
            msg_text = Text(text_str, font_size=18, color=color, font=MONO)
            bg_rect = Rectangle(
                width=msg_text.width + 0.4, height=msg_text.height + 0.15,
                fill_color=DARK_CARD, fill_opacity=0.85,
                stroke_color=color, stroke_width=1.5,
            )
            bg_rect.move_to(msg_text.get_center())
            entry = VGroup(bg_rect, msg_text)
            entry.move_to(start_y + DOWN * i * 0.85)

            if i > 0:
                append_label = Text(".append()", font_size=16, color=ACCENT, font=MONO)
                append_label.next_to(entry, RIGHT, buff=0.2)
                anims = [FadeIn(entry), Write(append_label)]
            else:
                anims = [FadeIn(entry)]

            self.play(*anims, run_time=0.6)
            msg_group.add(entry)
            self.wait(0.3)

        insight = Text("O LLM não lembra. Você gerencia.", font_size=22, color=PURPLE, weight=BOLD, font=MONO)
        insight.move_to(DOWN * 2.8)
        self.play(Write(insight), run_time=0.8)
        self.wait(27.2)


# ════════════════════════════════════════════════════════════════════
# SCENE 9 — Alternativas Locais
# ════════════════════════════════════════════════════════════════════
class S04_Scene9_Alternativas(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Alternativas Locais", font_size=36, color=PRIMARY, weight=BOLD, font=MONO)
        title.move_to(UP * 3.0)
        self.play(Write(title), run_time=1.0)

        cards_data = [
            ("LM Studio", SECONDARY,
             ["Interface gráfica", "llama.cpp por baixo",
              "API OpenAI-compatible", "Developer mode"]),
            ("llama.cpp", ACCENT,
             ["Compilado do código", "Melhor p/ hardware", "Sempre atualizado", ""]),
            ("ik_llama.cpp", PURPLE,
             ["Pouca VRAM, boa perf", "Contexto até 200K", "RAM comum", ""]),
        ]

        card_group = VGroup()
        for name, color, items in cards_data:
            card_items = VGroup()
            for item in items:
                if item:
                    card_items.add(Text(item, font_size=14, color=WHITE if item == items[0] else GRAY, font=MONO))

            if len([i for i in items if i]) > 0:
                card_items.arrange(DOWN, buff=0.15)

            name_txt = Text(name, font_size=22, color=color, weight=BOLD, font=MONO)
            card_vgroup = VGroup(name_txt, card_items).arrange(DOWN, buff=0.2)
            card_group.add(card_vgroup)

        card_group.arrange(RIGHT, buff=1.0)
        card_group.move_to(DOWN * 0.5)

        self.play(FadeIn(card_group), run_time=1.5)
        self.wait(43.1)


# ════════════════════════════════════════════════════════════════════
# SCENE 10 — Código: chat.py unificado
# ════════════════════════════════════════════════════════════════════
class S04_Scene10_ChatPy(Scene):
    def construct(self):
        self.camera.background_color = BG

        badge = neon_badge("Só muda a URL", border_color=ACCENT, font_size=22)
        badge.move_to(UP * 3.2)

        chatpy_code = """# Ollama (padrão)
URL = "http://localhost:11434/v1/chat/completions"

# LM Studio
# URL = "http://localhost:1234/v1/chat/completions"

# llama.cpp (porta pode variar)
# URL = "http://localhost:8080/v1/chat/completions"

response = requests.post(
    URL,
    json={"model": "qwen3.5:4b",
          "messages": [...],
          "keep_alive": -1},
    timeout=120,
)"""

        code_block = make_code(chatpy_code, scale=0.65)
        code_block.move_to(UP * 0.0)

        self.play(FadeIn(badge), run_time=0.5)
        self.play(FadeIn(code_block), run_time=1.5)
        self.wait(17.8)


# ════════════════════════════════════════════════════════════════════
# SCENE 11 — CTA: Próxima aula
# ════════════════════════════════════════════════════════════════════
class S04_Scene11_CTA(Scene):
    def construct(self):
        self.camera.background_color = BG

        aula_badge = pill_badge("AULA 04", fill_color=ACCENT, text_color="#000000", font_size=32)
        aula_badge.move_to(UP * 2.2)
        self.play(FadeIn(aula_badge), run_time=0.8)

        link1 = Text("Apostila + Notebook", font_size=26, color=WHITE, font=MONO)
        link1.move_to(UP * 0.8)
        link2 = Text("luksamuk.codes/pages/guilda-ia", font_size=20, color=PRIMARY, font=MONO)
        link2.next_to(link1, DOWN, buff=0.3)

        prox = Text("Próxima aula: Estrutura de um Agente", font_size=22, color=ACCENT, font=MONO)
        prox.move_to(DOWN * 0.5)

        logo = Text("GUILDA DE IA", font_size=56, color=PRIMARY, weight=BOLD, font=MONO)
        logo.move_to(DOWN * 2.4)

        self.play(Write(link1), run_time=0.8)
        self.play(Write(link2), run_time=0.6)
        self.play(Write(prox), run_time=0.6)
        self.play(Write(logo), run_time=1.0)
        self.wait(7.3)