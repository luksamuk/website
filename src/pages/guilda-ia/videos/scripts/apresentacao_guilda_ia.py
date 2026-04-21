#!/usr/bin/env python3
"""
Apresentação da Guilda de IA - Videoaula Introdutória

Estrutura validada pela skill narrated-video-lesson:
- Conceito → Visual → Didática → Aplicação → Resumo
- Cada conceito aparece UMA vez
- Resumo APENAS no final
- Duração total: ~90 segundos
- Regra de timing: tempo_final = max(vídeo + 2s, áudio + 2s)

ROTEIRO:

Cena 1 - Hook (12s): "E se você pudesse criar seu próprio assistente de IA... do zero?"
Cena 2 - Contexto (14s): "Essa é a proposta da Guilda. 12 semanas, do básico ao avançado."
Cena 3 - Jornada (16s): Timeline com as 12 semanas de conteúdo.
Cena 4 - Demonstração (14s): Exemplo prático - agentes autônomos.
Cena 5 - Comunidade (12s): "Não é um curso. É um espaço de estudo."
Cena 6 - CTA (10s): Convite simples para participar.

Renderizar com: manim -qh apresentacao_guilda_ia.py Scene1Hook Scene2Contexto ... Scene6CTA
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
WHITE = "#E6EDF3"      # Branco suave
GRAY = "#8B949E"       # Cinza para textos secundários
MONO = "JetBrains Mono"


class Scene1Hook(Scene):
    """
    Hook: Pergunta provocativa.
    Duração alvo: ~12s
    Narração: "E se você pudesse criar seu próprio assistente de IA... do zero?"
    """
    
    def construct(self):
        self.camera.background_color = BG
        
        # Pergunta central - surge gradualmente
        pergunta = Text("E se você pudesse criar...", 
                       font_size=42, color=WHITE, font=MONO)
        pergunta.shift(UP * 0.5)
        
        # Segunda linha - destaque
        destaque = Text("seu próprio assistente de IA", 
                        font_size=48, color=PRIMARY, font=MONO)
        destaque.next_to(pergunta, DOWN, buff=0.15)
        
        # Terceira linha - punchline
        punchline = Text("...do zero?", 
                        font_size=42, color=ACCENT, font=MONO)
        punchline.next_to(destaque, DOWN, buff=0.15)
        
        # Animações com timing adequado
        self.play(Write(pergunta), run_time=1.5)
        self.play(FadeIn(destaque), run_time=1)
        self.play(FadeIn(punchline), run_time=1)
        
        # Hold para leitura
        self.wait(2.5)
        
        # Fade out suave
        self.play(FadeOut(VGroup(pergunta, destaque, punchline)), run_time=0.5)


class Scene2Contexto(Scene):
    """
    Contexto: O que é a Guilda de IA.
    Duração alvo: ~14s
    Narração: "Essa é a proposta da Guilda de IA. Em doze semanas, vamos do básico ao avançado, explorando como IA funciona e construindo projetos na prática."
    """
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Guilda de IA", font_size=52, color=PRIMARY, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # Proposta
        proposta = Text("12 semanas • Do básico ao avançado • Projetos na prática",
                       font_size=26, color=WHITE, font=MONO)
        proposta.next_to(titulo, DOWN, buff=0.8)
        
        # Progressão visual (três estágios)
        estagios = VGroup()
        
        # Estágio 1: Fundamentos
        e1 = VGroup()
        e1_titulo = Text("Fundamentos", font_size=24, color=GRAY, font=MONO)
        e1_icone = Text("📚", font_size=36)
        e1.add(e1_icone, e1_titulo)
        e1.arrange(DOWN, buff=0.1)
        
        # Estágio 2: Exploração
        e2 = VGroup()
        e2_titulo = Text("Exploração", font_size=24, color=SECONDARY, font=MONO)
        e2_icone = Text("🔍", font_size=36)
        e2.add(e2_icone, e2_titulo)
        e2.arrange(DOWN, buff=0.1)
        
        # Estágio 3: Aplicação
        e3 = VGroup()
        e3_titulo = Text("Aplicação", font_size=24, color=ACCENT, font=MONO)
        e3_icone = Text("⚙", font_size=36)
        e3.add(e3_icone, e3_titulo)
        e3.arrange(DOWN, buff=0.1)
        
        estagios.add(e1, e2, e3)
        estagios.arrange(RIGHT, buff=2.0)
        estagios.shift(DOWN * 0.5)
        
        # Setas de progressão
        seta1 = Arrow(e1.get_right(), e2.get_left(), color=GRAY, buff=0.2, stroke_width=2)
        seta2 = Arrow(e2.get_right(), e3.get_left(), color=GRAY, buff=0.2, stroke_width=2)
        
        # Animações
        self.play(FadeIn(titulo), run_time=1)
        self.play(FadeIn(proposta), run_time=1)
        self.play(FadeIn(e1), run_time=0.8)
        self.play(Create(seta1), FadeIn(e2), run_time=1)
        self.play(Create(seta2), FadeIn(e3), run_time=1)
        
        # Hold
        self.wait(2)


class Scene3Jornada(Scene):
    """
    Jornada: Timeline das 12 semanas.
    Duração alvo: ~16s
    Narração: "Começamos com fundamentos. O que é IA? Como ela funciona? E por que tudo isso está acontecendo agora? Depois entramos no código, Python, A P Is, R A G e muito mais."
    """
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Jornada de 12 Semanas", font_size=40, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.3)
        
        # Timeline horizontal
        line = Line(LEFT * 5.5, RIGHT * 5.5, color=GRAY, stroke_width=2)
        line.shift(DOWN * 0.5)
        
        # Marcadores de semanas (mostrar apenas 4 blocos para simplicidade)
        blocos = [
            ("1-3", "Fundamentos", PRIMARY, "IA, ML, LLMs"),
            ("4-6", "Código", SECONDARY, "Python, APIs"),
            ("7-9", "Técnicas", ACCENT, "RAG, Agentes"),
            ("10-12", "Projetos", PURPLE, "Aplicação"),
        ]
        
        pontos = VGroup()
        labels = VGroup()
        subtitulos = VGroup()
        
        x_positions = [-4, -1.3, 1.3, 4]
        
        for i, (semana, nome, cor, desc) in enumerate(blocos):
            x = x_positions[i]
            
            # Ponto na linha
            ponto = Dot(point=[x, -0.5, 0], radius=0.12, color=cor)
            pontos.add(ponto)
            
            # Nome acima
            label = Text(nome, font_size=22, color=cor, font=MONO)
            label.move_to([x, 0.5, 0])
            labels.add(label)
            
            # Descrição abaixo
            sub = Text(desc, font_size=16, color=GRAY, font=MONO)
            sub.move_to([x, -1.5, 0])
            subtitulos.add(sub)
        
        # Número de semanas abaixo
        numeros = VGroup()
        for i, (semana, _, _, _) in enumerate(blocos):
            num = Text(semana, font_size=14, color=GRAY, font=MONO)
            num.move_to([x_positions[i], -2.0, 0])
            numeros.add(num)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.8)
        self.play(Create(line), run_time=1)
        
        # Revelar blocos sequencialmente
        for i in range(4):
            self.play(
                FadeIn(pontos[i]),
                FadeIn(labels[i]),
                FadeIn(subtitulos[i]),
                FadeIn(numeros[i]),
                run_time=0.6
            )
        
        self.wait(2)


class Scene4Demonstracao(Scene):
    """
    Demonstração: Exemplo prático de agentes autônomos.
    Duração alvo: ~14s
    Narração: "Na prática? Você conecta modelos a ferramentas reais. O agente planeja, executa, e aprende com os resultados."
    """
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Agente Autônomo", font_size=40, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.3)
        
        # Diagrama simplificado
        # Modelo no topo
        modelo_box = Square(side_length=1.2, color=PRIMARY, stroke_width=2)
        modelo_box.set_fill(PRIMARY, opacity=0.2)
        modelo_label = Text("LLM", font_size=20, color=PRIMARY, font=MONO)
        modelo_label.move_to(modelo_box.get_center())
        modelo = VGroup(modelo_box, modelo_label)
        modelo.shift(UP * 1.5)
        
        # Ferramentas abaixo
        ferramentas = VGroup()
        ferramenta_nomes = ["Código", "Busca", "Arquivos"]
        ferramenta_cores = [SECONDARY, ACCENT, PURPLE]
        
        for i, (nome, cor) in enumerate(zip(ferramenta_nomes, ferramenta_cores)):
            box = Square(side_length=1.0, color=cor, stroke_width=2)
            box.set_fill(cor, opacity=0.2)
            label = Text(nome, font_size=16, color=cor, font=MONO)
            label.move_to(box.get_center())
            ferramentas.add(VGroup(box, label))
        
        ferramentas.arrange(RIGHT, buff=0.8)
        ferramentas.shift(DOWN * 1.0)
        
        # Setas de conexão
        setas = VGroup()
        for f in ferramentas:
            seta = Arrow(modelo.get_bottom(), f.get_top(), color=GRAY, buff=0.1, stroke_width=1.5)
            setas.add(seta)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.8)
        self.play(FadeIn(modelo), run_time=1)
        
        # Revelar ferramentas com setas
        for i, (f, s) in enumerate(zip(ferramentas, setas)):
            self.play(Create(s), FadeIn(f), run_time=0.8)
        
        # Texto explicativo
        explicacao = Text("Planeja → Executa → Aprende", 
                         font_size=24, color=WHITE, font=MONO)
        explicacao.shift(DOWN * 2.5)
        
        self.play(FadeIn(explicacao), run_time=1)
        self.wait(2)


class Scene5Comunidade(Scene):
    """
    Comunidade: Espaço de estudo aberto.
    Duração alvo: ~12s
    Narração: "É um espaço de estudo aberto, onde você constrói junto com outras pessoas interessadas."
    """
    
    def construct(self):
        self.camera.background_color = BG
        
        # Mensagem principal - estrutura preservada
        msg1 = Text("Um espaço de estudo", font_size=36, color=WHITE, font=MONO)
        msg1.shift(UP * 0.8)
        
        msg2 = Text("aberto e colaborativo", font_size=42, color=PRIMARY, font=MONO)
        msg2.next_to(msg1, DOWN, buff=0.3)
        
        # Destaque
        destaque = Text("Você constrói junto.", font_size=48, color=SECONDARY, font=MONO)
        destaque.next_to(msg2, DOWN, buff=0.6)
        
        # Ícones de pessoas (simplificado)
        pessoas = VGroup()
        for i in range(5):
            pessoa = Text("◉", font_size=32, color=PINK if i % 2 == 0 else ACCENT)
            pessoas.add(pessoa)
        
        pessoas.arrange(RIGHT, buff=0.3)
        pessoas.next_to(destaque, DOWN, buff=0.8)
        
        # Animações
        self.play(FadeIn(msg1), run_time=1)
        self.play(FadeIn(msg2), run_time=1)
        self.play(FadeIn(destaque), run_time=1)
        self.play(FadeIn(pessoas), run_time=0.8)
        
        self.wait(2)


class Scene6CTA(Scene):
    """
    CTA: Convite simples.
    Duração alvo: ~10s
    Narração: "Se você tem curiosidade, dá uma olhada. Todo o material está lá, gratuito. Comece pelo começo."
    """
    
    def construct(self):
        self.camera.background_color = BG
        
        # Convite
        convite = Text("Se você tem curiosidade...", 
                      font_size=36, color=WHITE, font=MONO)
        convite.shift(UP * 1)
        
        # URL do site
        url = Text("luksamuk.codes/pages/guilda-ia", 
                  font_size=32, color=PRIMARY, font=MONO)
        url.next_to(convite, DOWN, buff=0.8)
        
        # Caixa ao redor da URL
        url_box = SurroundingRectangle(url, color=PRIMARY, buff=0.2, stroke_width=2)
        
        # Mensagem final
        final = Text("Todo o material está lá. Gratuito.", 
                    font_size=24, color=SECONDARY, font=MONO)
        final.next_to(url, DOWN, buff=1)
        
        # Animações
        self.play(FadeIn(convite), run_time=1)
        self.play(FadeIn(url), Create(url_box), run_time=1.5)
        self.play(FadeIn(final), run_time=1)
        
        # Hold maior para leitura final
        self.wait(3)


# ==============================================================================
# INSTRUÇÕES DE USO
# ==============================================================================
# 
# 1. Renderizar cenas em 2160p60:
#    source ~/manim-env/bin/activate
#    manim -qh apresentacao_guilda_ia.py Scene1Hook Scene2Contexto Scene3Jornada Scene4Demonstracao Scene5Comunidade Scene6CTA
#
# 2. Gerar narrações com Edge TTS:
#    edge-tts --voice pt-BR-AntonioNeural --text "E se você pudesse criar..." --write-media audio/cena1.ogg
#    edge-tts --voice pt-BR-AntonioNeural --text "Essa é a proposta da Guilda..." --write-media audio/cena2.ogg
#    # ... (repetir para cada cena)
#
# 3. Sincronizar vídeos com áudio:
#    python sync_revisado.py
#
# 4. Concatenar e enviar:
#    ffmpeg -f concat -i concat_list.txt -c copy video_final.mp4
#
# ==============================================================================