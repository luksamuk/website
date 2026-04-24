from manim import *
import math

# ============================================
# Cores
# ============================================
BG = "#1A1A2E"
PRIMARY = "#58C4DD"
SECONDARY = "#83C167"
ACCENT = "#FFB033"
PURPLE = "#BB86FC"
PINK = "#FF6B9D"
WHITE_TEXT = "#E6EDF3"
GRAY = "#8B949E"
DARK_CARD = "#282A3A"
MONO = "JetBrains Mono"

# ============================================
# Cena 1: Título (~9s) — FIXED: pontuação clara
# ============================================
class Scene1Titulo(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        titulo = Text("Prompting Básico", font_size=52, color=WHITE_TEXT, font=MONO)
        subtitulo = Text("Como falar com IA.", font_size=32, color=PRIMARY, font=MONO)
        badge = Text("Semana 02 — Guilda de IA", font_size=22, color=ACCENT, font=MONO)
        
        titulo.move_to(UP * 0.5)
        subtitulo.next_to(titulo, DOWN, buff=0.3)
        badge.next_to(subtitulo, DOWN, buff=0.5)
        
        self.play(Write(titulo), run_time=2)
        self.play(FadeIn(subtitulo), run_time=1)
        self.play(FadeIn(badge), run_time=0.8)
        self.wait(2)

# ============================================
# Cena 2: O Problema — Vago vs Específico (~18s) — FIXED: pausa antes de "resposta específica"
# ============================================
class Scene2Problema(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        # Lado esquerdo: prompt vago
        vago_label = Text("Vago", font_size=28, color=PINK, font=MONO)
        vago_prompt = Text('"Me fale sobre gatos"', font_size=22, color=GRAY, font=MONO)
        vago_resp = Text("→ resposta genérica", font_size=20, color=GRAY, font=MONO)
        
        vago_group = VGroup(vago_label, vago_prompt, vago_resp)
        vago_group.arrange(DOWN, buff=0.3)
        vago_group.move_to(LEFT * 3.5 + UP * 0.3)
        
        # Lado direito: prompt específico
        esp_label = Text("Específico", font_size=28, color=SECONDARY, font=MONO)
        esp_prompt = Text('"3 raças mais populares\ndo Brasil e por quê"', font_size=20, color=PRIMARY, font=MONO)
        esp_resp = Text("→ resposta específica", font_size=20, color=SECONDARY, font=MONO)
        
        esp_group = VGroup(esp_label, esp_prompt, esp_resp)
        esp_group.arrange(DOWN, buff=0.3)
        esp_group.move_to(RIGHT * 3.5 + UP * 0.3)
        
        # Diferença
        dif_text = Text("A diferença?\nO prompt.", font_size=28, color=ACCENT, font=MONO)
        dif_text.move_to(DOWN * 1.5)
        
        # Box
        vago_box = SurroundingRectangle(vago_group, color=PINK, buff=0.2, corner_radius=0.1)
        esp_box = SurroundingRectangle(esp_group, color=SECONDARY, buff=0.2, corner_radius=0.1)
        
        self.play(FadeIn(vago_label), Create(vago_box), run_time=1.5)
        self.play(FadeIn(vago_prompt), FadeIn(vago_resp), run_time=1.5)
        
        self.play(FadeIn(esp_label), Create(esp_box), run_time=1.5)
        self.play(FadeIn(esp_prompt), run_time=1.5)
        self.wait(0.5)  # PAUSA
        self.play(FadeIn(esp_resp), run_time=1)
        
        self.play(Write(dif_text), run_time=2)
        self.wait(3)

# ============================================
# Cena 3: O que é prompt (~13s) — FIXED: mais espaço horizontal pras letras
# ============================================
class Scene3OQueE(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        # Prompt = R + C + E + F — mais espaço horizontal
        prompt_eq = Text("Prompt =", font_size=36, color=WHITE_TEXT, font=MONO)
        prompt_eq.move_to(LEFT * 5 + UP * 1.2)
        
        # Letras mais espaçadas à direita
        r = Text("R", font_size=44, color=SECONDARY, font=MONO, weight=BOLD)
        c = Text("C", font_size=44, color=PRIMARY, font=MONO, weight=BOLD)
        e = Text("E", font_size=44, color=ACCENT, font=MONO, weight=BOLD)
        f = Text("F", font_size=44, color=PINK, font=MONO, weight=BOLD)
        
        letters = VGroup(r, c, e, f)
        letters.arrange(RIGHT, buff=1.0)  # Mais espaço entre letras
        letters.move_to(RIGHT * 1 + UP * 1.2)
        
        # Legendas abaixo de cada letra
        r_label = Text("Role", font_size=20, color=SECONDARY, font=MONO)
        c_label = Text("Context", font_size=20, color=PRIMARY, font=MONO)
        e_label = Text("Examples", font_size=20, color=ACCENT, font=MONO)
        f_label = Text("Format", font_size=20, color=PINK, font=MONO)
        
        r_label.next_to(r, DOWN, buff=0.4)
        c_label.next_to(c, DOWN, buff=0.4)
        e_label.next_to(e, DOWN, buff=0.4)
        f_label.next_to(f, DOWN, buff=0.4)
        
        # Quote
        quote = Text("Ingredientes claros\n= prato previsível", font_size=24, color=WHITE_TEXT, font=MONO)
        quote.move_to(DOWN * 1.5)
        
        self.play(FadeIn(prompt_eq), run_time=0.8)
        for letter, label in [(r, r_label), (c, c_label), (e, e_label), (f, f_label)]:
            self.play(FadeIn(letter), FadeIn(label), run_time=0.8)
        
        self.play(Write(quote), run_time=2)
        self.wait(2)

# ============================================
# Cena 4: Zero-shot vs Few-shot (~22s) — sem mudanças
# ============================================
class Scene4ZeroFewShot(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        # Zero-shot
        zs_label = Text("Zero-shot", font_size=30, color=PINK, font=MONO)
        zs_prompt = Text('Traduza: "Bom dia"', font_size=24, color=GRAY, font=MONO)
        zs_result = Text("→ model tries, may fail", font_size=20, color=PINK, font=MONO)
        zs_ambig = Text('"Banco" → bank ou bench?', font_size=20, color=ACCENT, font=MONO)
        
        zs_group = VGroup(zs_label, zs_prompt, zs_result, zs_ambig)
        zs_group.arrange(DOWN, buff=0.25)
        zs_group.move_to(LEFT * 3.5)
        
        # Few-shot
        fs_label = Text("Few-shot", font_size=30, color=SECONDARY, font=MONO)
        fs_prompt = VGroup(
            Text('"Gato" → "Cat"', font_size=22, color=GRAY, font=MONO),
            Text('"Cachorro" → "Dog"', font_size=22, color=GRAY, font=MONO),
            Text('"Pássaro" → ?', font_size=22, color=PRIMARY, font=MONO),
        )
        fs_prompt.arrange(DOWN, buff=0.15)
        fs_result = Text("→ model learns the pattern", font_size=20, color=SECONDARY, font=MONO)
        
        fs_group = VGroup(fs_label, fs_prompt, fs_result)
        fs_group.arrange(DOWN, buff=0.25)
        fs_group.move_to(RIGHT * 3.5)
        
        # Divisor
        divider = Line(UP * 2.5, DOWN * 2.5, color=GRAY, stroke_width=1, stroke_opacity=0.4)
        
        self.play(FadeIn(zs_label), run_time=1)
        self.play(FadeIn(zs_prompt), run_time=1)
        self.play(FadeIn(zs_result), FadeIn(zs_ambig), run_time=1.5)
        
        self.play(Create(divider), run_time=0.5)
        self.play(FadeIn(fs_label), run_time=1)
        self.play(FadeIn(fs_prompt), run_time=2)
        self.play(FadeIn(fs_result), run_time=1)
        self.wait(3)

# ============================================
# Cena 5: Role Prompting (~21s) — sem mudanças
# ============================================
class Scene5RolePrompting(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        # Sem role
        sem_label = Text("Sem role:", font_size=24, color=PINK, font=MONO)
        sem_prompt = Text('"Explique derivadas"', font_size=22, color=GRAY, font=MONO)
        sem_resp = Text("→ texto genérico e seco", font_size=20, color=PINK, font=MONO)
        
        sem_group = VGroup(sem_label, sem_prompt, sem_resp)
        sem_group.arrange(DOWN, buff=0.3)
        sem_group.move_to(LEFT * 3.5 + UP * 0.5)
        
        # Com role
        com_label = Text("Com role:", font_size=24, color=SECONDARY, font=MONO)
        com_prompt = Text('"Você é uma professora\nde matemática do EM,\npaciente e didática.\nExplique derivadas."', 
                         font_size=18, color=PRIMARY, font=MONO)
        com_resp = Text("→ resposta acessível,\ncom exemplos", font_size=20, color=SECONDARY, font=MONO)
        
        com_group = VGroup(com_label, com_prompt, com_resp)
        com_group.arrange(DOWN, buff=0.25)
        com_group.move_to(RIGHT * 3.5 + UP * 0.3)
        
        # Divisor
        divider = Line(UP * 2.5, DOWN * 2.5, color=GRAY, stroke_width=1, stroke_opacity=0.4)
        
        # Quote
        note = Text("System prompt de agentes\n= role prompting", font_size=20, color=ACCENT, font=MONO)
        note.move_to(DOWN * 2.3)
        
        self.play(FadeIn(sem_label), FadeIn(sem_prompt), run_time=1.5)
        self.play(FadeIn(sem_resp), run_time=1)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(com_label), FadeIn(com_prompt), run_time=2)
        self.play(FadeIn(com_resp), run_time=1)
        self.play(Write(note), run_time=1.5)
        self.wait(3)

# ============================================
# Cena 6: Chain-of-Thought (~21s) — FIXED: título adicionado
# ============================================
class Scene6CoT(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        title = Text("Chain-of-Thought", font_size=32, color=PRIMARY, font=MONO)
        title.move_to(UP * 3)
        
        # Problema
        problem = Text("Roger tem 5 bolas.\nCompra 2 latas de 3.\nTotal?", font_size=22, color=WHITE_TEXT, font=MONO)
        problem.move_to(UP * 1.2)
        
        # Sem CoT
        sem_cot = Text("Sem CoT: 11?", font_size=26, color=PINK, font=MONO)
        sem_cot.move_to(LEFT * 3.5 + DOWN * 0.3)
        
        # Com CoT (passos)
        step1 = Text("5 bolas", font_size=22, color=GRAY, font=MONO)
        step2 = Text("2 × 3 = 6 bolas", font_size=22, color=PRIMARY, font=MONO)
        step3 = Text("5 + 6 = 11 ✓", font_size=22, color=SECONDARY, font=MONO)
        
        steps = VGroup(step1, step2, step3)
        steps.arrange(DOWN, buff=0.3)
        steps.move_to(RIGHT * 2.5 + DOWN * 0.5)
        
        com_label = Text("Com CoT:", font_size=26, color=SECONDARY, font=MONO)
        com_label.next_to(steps, UP, buff=0.3)
        
        # Quote
        note = Text("Ferramentas exigem\nraciocínio", font_size=20, color=ACCENT, font=MONO)
        note.move_to(DOWN * 2.5)
        
        self.play(Write(title), run_time=1.5)
        self.play(Write(problem), run_time=2)
        self.play(FadeIn(sem_cot), run_time=1.5)
        
        self.play(Write(com_label), run_time=1)
        for step in steps:
            self.play(FadeIn(step), run_time=0.7)
        
        self.play(Write(note), run_time=2)
        self.wait(2)

# ============================================
# Cena 7: RCEF-TC Framework (~30s) — FIXED: narração soletra cada letra
# ============================================
class Scene7RCEF(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        # Cards em sequência
        cards_data = [
            ("R", "Role", "Você é um tutor", SECONDARY),
            ("C", "Context", "Aluno no ensino médio", PRIMARY),
            ("E", "Examples", "2x+3=7 → x=2", ACCENT),
            ("F", "Format", "Responda em bullets", PINK),
            ("T", "Task", "Resolva esta equação", "#FF8C42"),
            ("C", "Constraints", "Máximo 3 passos", PURPLE),
        ]
        
        cards = []
        for letter, name, example, color in cards_data:
            card_letter = Text(letter, font_size=40, color=color, font=MONO, weight=BOLD)
            card_name = Text(name, font_size=20, color=color, font=MONO)
            card_ex = Text(example, font_size=16, color=GRAY, font=MONO)
            
            card = VGroup(card_letter, card_name, card_ex)
            card.arrange(DOWN, buff=0.1)
            cards.append(card)
        
        all_cards = VGroup(*cards)
        all_cards.arrange_in_grid(rows=2, cols=3, buff=0.5)
        all_cards.move_to(ORIGIN)
        
        # Animação sequencial
        for i, card in enumerate(cards):
            self.play(FadeIn(card), run_time=0.6)
        
        # Summary
        summary = Text("Zero-shot = sem E | Few-shot = com E | Role = R", 
                       font_size=20, color=ACCENT, font=MONO)
        summary.move_to(DOWN * 2.8)
        self.play(Write(summary), run_time=2)
        self.wait(3)

# ============================================
# Cena 8: RCEF-TC na prática (~20s) — FIXED: seta mais pra cima
# ============================================
class Scene8RCEFPratica(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        # Prompt ruim — mais pra cima
        ruim = Text('"Me ajuda com meu TCC"', font_size=26, color=PINK, font=MONO)
        ruim.move_to(UP * 2.5)
        
        # Seta de transformação — mais espaço entre seta e texto
        arrow = Arrow(UP * 2.0, UP * 0.2, color=ACCENT, buff=0.2, stroke_width=3)
        arrow_label = Text("RCEF-TC", font_size=22, color=ACCENT, font=MONO)
        arrow_label.next_to(arrow, RIGHT, buff=0.2)
        
        # Prompt bom — mais pra baixo
        bom_lines = VGroup(
            Text("R: Tutor de computação", font_size=20, color=SECONDARY, font=MONO),
            Text("C: 6º semestre, TCC em redes", font_size=20, color=PRIMARY, font=MONO),
            Text("T: Revisão de metodologia", font_size=20, color="#FF8C42", font=MONO),
            Text("F: Responda em tópicos", font_size=20, color=PINK, font=MONO),
            Text("C: Máximo 3 páginas", font_size=20, color=PURPLE, font=MONO),
        )
        bom_lines.arrange(DOWN, buff=0.2)
        bom_lines.move_to(DOWN * 0.8)
        
        self.play(Write(ruim), run_time=1.5)
        self.play(Create(arrow), FadeIn(arrow_label), run_time=1)
        
        for line in bom_lines:
            self.play(FadeIn(line), run_time=0.6)
        self.wait(4)

# ============================================
# Cena 9: Alucinações (~18s) — sem mudanças
# ============================================
class Scene9Alucinacao(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        # Prompt vago
        vago = Text('"Quem ganhou a copa de 2042?"', font_size=24, color=WHITE_TEXT, font=MONO)
        vago.move_to(UP * 1.8)
        
        # Alucinação
        aluc = Text("Modelo inventa resultado ✗", font_size=24, color=PINK, font=MONO)
        aluc.move_to(UP * 0.5)
        
        # Prompt com constraint
        constraint = Text('"Responda apenas se tiver certeza.\nSe não souber, diga que não sabe."', font_size=20, color=PRIMARY, font=MONO)
        constraint.move_to(DOWN * 0.5)
        
        # Resposta honesta
        honesto = Text('→ "Não sei" ✓', font_size=24, color=SECONDARY, font=MONO)
        honesto.move_to(DOWN * 1.8)
        
        # Diagnóstico
        diag = Text("Refaça o prompt. Melhorou?\n→ Era prompt ruim.\nAinda erra?\n→ Alucinação.", font_size=18, color=ACCENT, font=MONO)
        diag.move_to(DOWN * 3.2)
        
        self.play(Write(vago), run_time=1.5)
        self.play(Write(aluc), run_time=1.5)
        self.play(Write(constraint), run_time=2)
        self.play(Write(honesto), run_time=1.5)
        self.play(Write(diag), run_time=2.5)
        self.wait(1)

# ============================================
# Cena 10 (antiga 11): Encerramento (~12s) — agora é cena 10
# ============================================
class Scene10Encerramento(Scene):
    def construct(self):
        self.camera.background_color = BG
        
        quote1 = Text("O prompt é como uma receita.", font_size=32, color=WHITE_TEXT, font=MONO)
        quote2 = Text("Ingredientes claros = prato previsível.", font_size=28, color=PRIMARY, font=MONO)
        
        quote1.move_to(UP * 0.8)
        quote2.move_to(UP * -0.2)
        
        next_week = Text("Semana 03: Python + API", font_size=26, color=ACCENT, font=MONO)
        next_week.move_to(DOWN * 1.5)
        
        guilda = Text("Guilda de IA", font_size=30, color=SECONDARY, font=MONO)
        guilda.move_to(DOWN * 2.8)
        
        self.play(Write(quote1), run_time=2)
        self.play(FadeIn(quote2), run_time=2)
        self.play(FadeIn(next_week), run_time=1.5)
        self.play(FadeIn(guilda), run_time=1)
        self.wait(2)