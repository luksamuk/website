#!/usr/bin/env python3
"""
Aula RAG - Vídeos Separados por Conceito

Estrutura:
1. Embeddings (já feito - 99s)
2. Chunking (~60s)
3. Vector Store (~60s)
4. Retrieval (~60s)
5. Pipeline RAG (~70s)

Workflow:
1. Gerar roteiros separados
2. Gerar áudios Edge TTS para cada vídeo
3. Renderizar cenas Manim
4. Sincronizar e concatenar
5. Montar vídeo final completo

Renderizar: manim -qh rag_lesson.py Scene*

==============================================
"""

from manim import *
import math
import random

# Paleta de cores
BG = "#0D1117"
PRIMARY = "#58A6FF"    # Azul
SECONDARY = "#7EE787"  # Verde
ACCENT = "#F0883E"     # Laranja
PURPLE = "#BC8CFF"     # Roxo
PINK = "#FF9CCE"       # Rosa
WHITE = "#E6EDF3"
GRAY = "#8B949E"
MONO = "JetBrains Mono"


# ============================================================================
# VÍDEO 2: CHUNKING
# ============================================================================

class Chunking_Scene1_Hook(Scene):
    """Hook: Como dividir um documento."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Documento grande
        doc = Rectangle(width=4, height=5, color=GRAY, stroke_width=2)
        doc.shift(LEFT * 2.5)
        
        lines = VGroup()
        for i in range(8):
            line = Line(LEFT * 4 + UP * (2 - i * 0.6), 
                       LEFT * 1 + UP * (2 - i * 0.6),
                       color=GRAY, stroke_width=1)
            lines.add(line)
        
        doc_content = VGroup(doc, lines)
        
        # Pergunta
        pergunta = Text("Como você divide isso\nem pedaços que fazem sentido?",
                       font_size=32, color=WHITE, font=MONO)
        pergunta.shift(RIGHT * 2.5)
        
        # Animações
        self.play(Create(doc), FadeIn(lines), run_time=1.5)
        self.play(FadeIn(pergunta), run_time=1)
        
        self.wait(2.5)


class Chunking_Scene2_Problema(Scene):
    """Problema: LLMs têm limite de contexto."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("O Problema do Contexto", font_size=36, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # Documento grande
        doc_grande = Rectangle(width=2, height=4, color=ACCENT, stroke_width=2)
        doc_grande.shift(LEFT * 3.5)
        label_grande = Text("100 páginas", font_size=18, color=ACCENT, font=MONO)
        label_grande.next_to(doc_grande, DOWN, buff=0.2)
        
        # Seta X
        x_mark = Text("✗", font_size=48, color=PINK)
        x_mark.shift(LEFT * 1.5)
        
        # LLM
        llm_box = Square(side_length=1.5, color=PRIMARY, stroke_width=2)
        llm_box.shift(RIGHT * 1)
        llm_label = Text("LLM", font_size=24, color=PRIMARY, font=MONO)
        llm_label.move_to(llm_box.get_center())
        
        # Limite
        limite = Text("limite:\n8k tokens", font_size=16, color=GRAY, font=MONO)
        limite.next_to(llm_box, DOWN, buff=0.3)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.8)
        self.play(Create(doc_grande), FadeIn(label_grande), run_time=1)
        self.play(FadeIn(x_mark), run_time=0.5)
        self.play(Create(llm_box), FadeIn(llm_label), FadeIn(limite), run_time=1)
        
        self.wait(2)


class Chunking_Scene3_Solucao(Scene):
    """Solução: Dividir em chunks."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Chunking: Dividir para Conquistar", font_size=32, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # Estratégias
        estrategias = VGroup()
        
        # Fixed size
        e1_box = Rectangle(width=2.5, height=2, color=PRIMARY, stroke_width=2)
        e1_box.shift(UP * 0.5 + LEFT * 3.5)
        e1_title = Text("Fixed Size", font_size=20, color=PRIMARY, font=MONO)
        e1_title.move_to(e1_box.get_top() + DOWN * 0.3)
        e1_desc = Text("512 tokens\npor chunk", font_size=14, color=GRAY, font=MONO)
        e1_desc.move_to(e1_box.get_center() + DOWN * 0.2)
        
        # Semantic
        e2_box = Rectangle(width=2.5, height=2, color=SECONDARY, stroke_width=2)
        e2_box.shift(UP * 0.5)
        e2_title = Text("Semantic", font_size=20, color=SECONDARY, font=MONO)
        e2_title.move_to(e2_box.get_top() + DOWN * 0.3)
        e2_desc = Text("Por sentenças\nou parágrafos", font_size=14, color=GRAY, font=MONO)
        e2_desc.move_to(e2_box.get_center() + DOWN * 0.2)
        
        # Recursive
        e3_box = Rectangle(width=2.5, height=2, color=ACCENT, stroke_width=2)
        e3_box.shift(UP * 0.5 + RIGHT * 3.5)
        e3_title = Text("Recursive", font_size=20, color=ACCENT, font=MONO)
        e3_title.move_to(e3_box.get_top() + DOWN * 0.3)
        e3_desc = Text("Divide até\nencontrar tamanho", font_size=14, color=GRAY, font=MONO)
        e3_desc.move_to(e3_box.get_center() + DOWN * 0.2)
        
        # Chunks exemplo na parte de baixo
        chunks = VGroup()
        for i in range(5):
            chunk = Rectangle(width=1.2, height=0.6, color=PURPLE, stroke_width=1.5)
            chunk.shift(DOWN * 1.8 + LEFT * 2.4 + RIGHT * i * 1.3)
            chunks.add(chunk)
        
        chunks_label = Text("Chunks menores → fáceis de processar", 
                           font_size=18, color=PURPLE, font=MONO)
        chunks_label.shift(DOWN * 2.8)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.8)
        
        self.play(Create(e1_box), FadeIn(e1_title), FadeIn(e1_desc), run_time=1)
        self.play(Create(e2_box), FadeIn(e2_title), FadeIn(e2_desc), run_time=1)
        self.play(Create(e3_box), FadeIn(e3_title), FadeIn(e3_desc), run_time=1)
        
        self.play(*[FadeIn(c) for c in chunks], run_time=1)
        self.play(FadeIn(chunks_label), run_time=0.8)
        
        self.wait(2)


# ============================================================================
# VÍDEO 3: VECTOR STORE
# ============================================================================

class VectorStore_Scene1_Hook(Scene):
    """Hook: Onde guardar milhares de vetores?"""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Muitos vetores
        vetores = VGroup()
        for _ in range(30):
            v = Dot(radius=0.05, color=PRIMARY)
            v.shift(UP * random.uniform(-2, 2) + RIGHT * random.uniform(-3, 3))
            vetores.add(v)
        
        # Pergunta
        pergunta = Text("Onde guardar\nmilhares de vetores?",
                       font_size=40, color=WHITE, font=MONO)
        pergunta.to_edge(UP, buff=0.5)
        
        # Desafio
        desafio = Text("E achar o certo em\nmenos de 1 segundo?",
                      font_size=28, color=ACCENT, font=MONO)
        desafio.to_edge(DOWN, buff=0.8)
        
        # Animações
        self.play(*[FadeIn(v) for v in vetores], run_time=1.5)
        self.play(FadeIn(pergunta), run_time=1)
        self.play(FadeIn(desafio), run_time=1)
        
        self.wait(2.5)


class VectorStore_Scene2_Solucao(Scene):
    """Solução: Vector Database."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Vector Database", font_size=40, color=PRIMARY, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # Ferramentas
        ferramentas = VGroup()
        
        # FAISS
        f1 = Rectangle(width=2.2, height=1.2, color=SECONDARY, stroke_width=2)
        f1.shift(UP * 0.5 + LEFT * 3)
        f1_label = Text("FAISS", font_size=22, color=SECONDARY, font=MONO)
        f1_label.move_to(f1.get_center())
        
        # Chroma
        f2 = Rectangle(width=2.2, height=1.2, color=ACCENT, stroke_width=2)
        f2.shift(UP * 0.5)
        f2_label = Text("Chroma", font_size=22, color=ACCENT, font=MONO)
        f2_label.move_to(f2.get_center())
        
        # Pinecone
        f3 = Rectangle(width=2.2, height=1.2, color=PURPLE, stroke_width=2)
        f3.shift(UP * 0.5 + RIGHT * 3)
        f3_label = Text("Pinecone", font_size=22, color=PURPLE, font=MONO)
        f3_label.move_to(f3.get_center())
        
        # Características
        carac = Text("Indexação + Busca Rápida + Persistência",
                    font_size=20, color=GRAY, font=MONO)
        carac.shift(DOWN * 1.5)
        
        # Busca
        busca_demo = Text("query → embedding → busca → top-k resultados",
                         font_size=18, color=WHITE, font=MONO)
        busca_demo.shift(DOWN * 2.5)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.8)
        self.play(Create(f1), FadeIn(f1_label), run_time=0.8)
        self.play(Create(f2), FadeIn(f2_label), run_time=0.8)
        self.play(Create(f3), FadeIn(f3_label), run_time=0.8)
        self.play(FadeIn(carac), run_time=1)
        self.play(FadeIn(busca_demo), run_time=1)
        
        self.wait(2)


# ============================================================================
# VÍDEO 4: RETRIEVAL
# ============================================================================

class Retrieval_Scene1_Hook(Scene):
    """Hook: Busca semântica vs keywords."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Query
        query = Text('"como fazer café"', font_size=32, color=PRIMARY, font=MONO)
        query.shift(UP * 1.5)
        
        # Duas abordagens
        # Keywords
        kw_box = Rectangle(width=3, height=2.5, color=PINK, stroke_width=2)
        kw_box.shift(LEFT * 2.5 + DOWN * 0.5)
        kw_title = Text("Keywords", font_size=24, color=PINK, font=MONO)
        kw_title.move_to(kw_box.get_top() + DOWN * 0.3)
        kw_result = Text('acha "café"\nmas perde\n"expresso"', 
                         font_size=16, color=GRAY, font=MONO)
        kw_result.move_to(kw_box.get_center() + DOWN * 0.2)
        
        # Semântica
        sem_box = Rectangle(width=3, height=2.5, color=SECONDARY, stroke_width=2)
        sem_box.shift(RIGHT * 2.5 + DOWN * 0.5)
        sem_title = Text("Semântica", font_size=24, color=SECONDARY, font=MONO)
        sem_title.move_to(sem_box.get_top() + DOWN * 0.3)
        sem_result = Text('acha "preparar\nbebida quente"\n✓', 
                         font_size=16, color=SECONDARY, font=MONO)
        sem_result.move_to(sem_box.get_center() + DOWN * 0.2)
        
        # Animações
        self.play(FadeIn(query), run_time=1)
        self.play(Create(kw_box), FadeIn(kw_title), FadeIn(kw_result), run_time=1.5)
        self.play(Create(sem_box), FadeIn(sem_title), FadeIn(sem_result), run_time=1.5)
        
        self.wait(2)


class Retrieval_Scene2_Processo(Scene):
    """Processo de retrieval."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Retrieval em RAG", font_size=36, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.3)
        
        # Pipeline horizontal
        passos = [
            ("Query", PRIMARY, "pergunta\ndo usuário"),
            ("Embed", SECONDARY, "converter\npara vetor"),
            ("Search", ACCENT, "buscar\nno vector DB"),
            ("Top-k", PURPLE, "k mais\nsimilares"),
        ]
        
        elementos = VGroup()
        x_pos = -4.5
        x_step = 2.8
        
        for nome, cor, desc in passos:
            box = Rectangle(width=2.2, height=1.8, color=cor, stroke_width=2)
            box.shift(RIGHT * (x_pos) + DOWN * 0.5)
            
            label = Text(nome, font_size=22, color=cor, font=MONO)
            label.move_to(box.get_top() + DOWN * 0.35)
            
            descricao = Text(desc, font_size=14, color=GRAY, font=MONO)
            descricao.move_to(box.get_center() + DOWN * 0.25)
            
            elementos.add(VGroup(box, label, descricao))
            x_pos += x_step
        
        # Setas de conexão
        setas = VGroup()
        for i in range(len(passos) - 1):
            start = elementos[i][0].get_right()
            end = elementos[i+1][0].get_left()
            seta = Arrow(start, end, color=GRAY, buff=0.15, stroke_width=2)
            setas.add(seta)
        
        # Top-k resultado
        resultado = Text("k=3: os 3 chunks mais relevantes",
                        font_size=18, color=WHITE, font=MONO)
        resultado.shift(DOWN * 2.5)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.6)
        
        for i, elem in enumerate(elementos):
            self.play(FadeIn(elem), run_time=0.6)
            if i < len(setas):
                self.play(Create(setas[i]), run_time=0.4)
        
        self.play(FadeIn(resultado), run_time=1)
        
        self.wait(2)


# ============================================================================
# VÍDEO 0: INTRODUÇÃO GERAL
# ============================================================================

class Intro_Scene1_Titulo(Scene):
    """Título geral da aula de RAG."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título principal
        titulo = Text("RAG", font_size=72, color=PRIMARY, font=MONO)
        
        # Subtítulo
        subtitulo = Text("Retrieval-Augmented Generation", 
                        font_size=32, color=WHITE, font=MONO)
        subtitulo.next_to(titulo, DOWN, buff=0.4)
        
        # Explicação
        explicacao = Text("Como dar memória e contexto para LLMs",
                         font_size=24, color=GRAY, font=MONO)
        explicacao.next_to(subtitulo, DOWN, buff=0.8)
        
        # Animações
        self.play(FadeIn(titulo), run_time=1)
        self.play(FadeIn(subtitulo), run_time=1)
        self.play(FadeIn(explicacao), run_time=1)
        
        self.wait(2)


class Intro_Scene2_Problema(Scene):
    """Problema: LLMs não sabem dos seus dados."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("O Problema", font_size=36, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # LLM
        llm_box = Square(side_length=2, color=PRIMARY, stroke_width=2)
        llm_box.shift(LEFT * 2.5)
        llm_label = Text("LLM", font_size=28, color=PRIMARY, font=MONO)
        llm_label.move_to(llm_box.get_center())
        
        # Conhecimento
        know_box = Rectangle(width=2.5, height=1.5, color=SECONDARY, stroke_width=2)
        know_box.shift(UP * 1.5)
        know_label = Text("Treino", font_size=20, color=SECONDARY, font=MONO)
        know_label.move_to(know_box.get_center())
        know_desc = Text("Dados até 2023", font_size=14, color=GRAY, font=MONO)
        know_desc.next_to(know_box, DOWN, buff=0.1)
        
        # X - não conhece
        unknow_box = Rectangle(width=2.5, height=1.5, color=PINK, stroke_width=2)
        unknow_box.shift(DOWN * 1.5 + RIGHT * 2)
        unknow_label = Text("Seus Dados", font_size=20, color=PINK, font=MONO)
        unknow_label.move_to(unknow_box.get_center())
        unknow_desc = Text("✗ Não conhece", font_size=14, color=GRAY, font=MONO)
        unknow_desc.next_to(unknow_box, DOWN, buff=0.1)
        
        # Pergunta
        pergunta = Text('"Qual o status do\npedido #1234?"',
                       font_size=18, color=ACCENT, font=MONO)
        pergunta.shift(LEFT * 2.5 + DOWN * 2.5)
        
        # Resposta
        resposta = Text('"Não tenho acesso\naos seus pedidos"',
                       font_size=18, color=GRAY, font=MONO)
        resposta.shift(LEFT * 2.5 + DOWN * 3.5)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.6)
        self.play(Create(llm_box), FadeIn(llm_label), run_time=1)
        self.play(FadeIn(know_box), FadeIn(know_label), FadeIn(know_desc), run_time=1)
        self.play(FadeIn(unknow_box), FadeIn(unknow_label), FadeIn(unknow_desc), run_time=1)
        self.play(FadeIn(pergunta), run_time=0.8)
        self.play(FadeIn(resposta), run_time=0.8)
        
        self.wait(2)


class Intro_Scene3_Solucao(Scene):
    """Solução: RAG."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # RAG
        titulo = Text("RAG", font_size=48, color=PRIMARY, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # Expansão
        r_text = Text("R", font_size=36, color=SECONDARY, font=MONO)
        a_text = Text("A", font_size=36, color=ACCENT, font=MONO)
        g_text = Text("G", font_size=36, color=PURPLE, font=MONO)
        
        rag_full = VGroup(
            Text("Retrieval", font_size=20, color=SECONDARY, font=MONO),
            Text("Augmentation", font_size=20, color=ACCENT, font=MONO),
            Text("Generation", font_size=20, color=PURPLE, font=MONO),
        )
        rag_full.arrange(RIGHT, buff=1.5)
        rag_full.next_to(titulo, DOWN, buff=0.8)
        
        # Explicação simples
        explicacao = VGroup()
        
        e1 = Text("1. Buscar informações relevantes", font_size=22, color=WHITE, font=MONO)
        e2 = Text("2. Passar para o LLM junto com a pergunta", font_size=22, color=WHITE, font=MONO)
        e3 = Text("3. LLM gera resposta fundamentada", font_size=22, color=WHITE, font=MONO)
        
        explicacao.add(e1, e2, e3)
        explicacao.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        explicacao.shift(DOWN * 1.2)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.8)
        self.play(FadeIn(rag_full), run_time=1.2)
        self.play(FadeIn(e1), run_time=0.8)
        self.play(FadeIn(e2), run_time=0.8)
        self.play(FadeIn(e3), run_time=0.8)
        
        self.wait(2)


# ============================================================================
# VÍDEO 5: PIPELINE RAG COMPLETO
# ============================================================================

class RAGPipeline_Scene1_Juntando(Scene):
    """Juntando todos os conceitos."""
    
    def construct(self):
        self.camera.background_color = BG
        
        titulo = Text("Pipeline RAG Completo", font_size=36, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.3)
        
        # Pipeline vertical
        passos = [
            ("Documentos", PRIMARY, "Chunks"),
            ("Embeddings", SECONDARY, "Vetores"),
            ("Vector Store", ACCENT, "Indexação"),
            ("Query + Retrieval", PURPLE, "Busca"),
            ("Augmentation", PINK, "Query + Docs"),
            ("Generation", WHITE, "LLM responde"),
        ]
        
        elementos = VGroup()
        y_pos = 2.5
        y_step = -1.0
        
        for nome, cor, sub in passos:
            box = Rectangle(width=4, height=0.8, color=cor, stroke_width=2)
            box.shift(UP * y_pos)
            
            label = Text(nome, font_size=20, color=cor, font=MONO)
            label.move_to(box.get_center() + LEFT * 0.5)
            
            sublabel = Text(sub, font_size=14, color=GRAY, font=MONO)
            sublabel.move_to(box.get_center() + RIGHT * 1.2)
            
            elementos.add(VGroup(box, label, sublabel))
            y_pos += y_step
        
        # Setas de conexão
        setas = VGroup()
        for i in range(len(passos) - 1):
            start = elementos[i][0].get_bottom()
            end = elementos[i+1][0].get_top()
            seta = Arrow(start, end, color=GRAY, buff=0.1, stroke_width=1.5)
            setas.add(seta)
        
        # Animações - revelar sequencialmente
        self.play(FadeIn(titulo), run_time=0.6)
        
        for i, elem in enumerate(elementos):
            self.play(FadeIn(elem), run_time=0.5)
            if i < len(setas):
                self.play(Create(setas[i]), run_time=0.3)
        
        self.wait(2)


class RAGPipeline_Scene2_Resumo(Scene):
    """Resumo final."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("RAG em Resumo", font_size=36, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # Três pilares
        pilares = VGroup()
        
        # Retrieval
        r_box = Rectangle(width=3.5, height=2, color=PRIMARY, stroke_width=2)
        r_box.shift(LEFT * 3.5 + UP * 0.3)
        r_label = Text("Retrieval", font_size=24, color=PRIMARY, font=MONO)
        r_label.move_to(r_box.get_top() + DOWN * 0.35)
        r_desc = Text("Busca contexto\nrelevante", font_size=16, color=GRAY, font=MONO)
        r_desc.move_to(r_box.get_center() + DOWN * 0.2)
        
        # Augmentation
        a_box = Rectangle(width=3.5, height=2, color=SECONDARY, stroke_width=2)
        a_box.shift(UP * 0.3)
        a_label = Text("Augmentation", font_size=24, color=SECONDARY, font=MONO)
        a_label.move_to(a_box.get_top() + DOWN * 0.35)
        a_desc = Text("Combina query\n+ documentos", font_size=16, color=GRAY, font=MONO)
        a_desc.move_to(a_box.get_center() + DOWN * 0.2)
        
        # Generation
        g_box = Rectangle(width=3.5, height=2, color=ACCENT, stroke_width=2)
        g_box.shift(RIGHT * 3.5 + UP * 0.3)
        g_label = Text("Generation", font_size=24, color=ACCENT, font=MONO)
        g_label.move_to(g_box.get_top() + DOWN * 0.35)
        g_desc = Text("LLM gera\nresposta", font_size=16, color=GRAY, font=MONO)
        g_desc.move_to(g_box.get_center() + DOWN * 0.2)
        
        pilares.add(VGroup(r_box, r_label, r_desc))
        pilares.add(VGroup(a_box, a_label, a_desc))
        pilares.add(VGroup(g_box, g_label, g_desc))
        
        # Setas
        seta1 = Arrow(r_box.get_right(), a_box.get_left(), color=GRAY, buff=0.15)
        seta2 = Arrow(a_box.get_right(), g_box.get_left(), color=GRAY, buff=0.15)
        
        # Mensagem final
        mensagem = Text("Fundamentos = tudo que você aprendeu até aqui",
                       font_size=22, color=WHITE, font=MONO)
        mensagem.shift(DOWN * 2)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.6)
        self.play(FadeIn(r_box), FadeIn(r_label), FadeIn(r_desc), run_time=1)
        self.play(Create(seta1), FadeIn(a_box), FadeIn(a_label), FadeIn(a_desc), run_time=1)
        self.play(Create(seta2), FadeIn(g_box), FadeIn(g_label), FadeIn(g_desc), run_time=1)
        self.play(FadeIn(mensagem), run_time=1)
        
        self.wait(3)


# ============================================================================
# VÍDEO 6: CONCLUSÃO GERAL
# ============================================================================

class Conclusao_Scene1_Resumo(Scene):
    """Resumo de tudo que foi aprendido."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("O que você aprendeu", font_size=36, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # Tópicos em coluna
        topicos = VGroup()
        
        t1 = VGroup(
            Text("Embeddings", font_size=24, color=PRIMARY, font=MONO),
            Text("→ Convertendo texto em vetores", font_size=16, color=GRAY, font=MONO)
        )
        
        t2 = VGroup(
            Text("Chunking", font_size=24, color=SECONDARY, font=MONO),
            Text("→ Dividindo documentos em pedaços", font_size=16, color=GRAY, font=MONO)
        )
        
        t3 = VGroup(
            Text("Vector Store", font_size=24, color=ACCENT, font=MONO),
            Text("→ Armazenando e indexando vetores", font_size=16, color=GRAY, font=MONO)
        )
        
        t4 = VGroup(
            Text("Retrieval", font_size=24, color=PURPLE, font=MONO),
            Text("→ Buscando contexto relevante", font_size=16, color=GRAY, font=MONO)
        )
        
        t5 = VGroup(
            Text("RAG Pipeline", font_size=24, color=PINK, font=MONO),
            Text("→ Juntando tudo", font_size=16, color=GRAY, font=MONO)
        )
        
        topicos.add(t1, t2, t3, t4, t5)
        topicos.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        topicos.shift(DOWN * 0.2)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.6)
        
        for t in topicos:
            self.play(FadeIn(t), run_time=0.6)
        
        self.wait(2)


class Conclusao_Scene2_Aplicacao(Scene):
    """Aplicações práticas."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Onde usar RAG?", font_size=36, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # Aplicações
        apps = VGroup()
        
        apps_data = [
            ("Chatbot de Suporte", "Documentação da empresa", PRIMARY),
            ("Assistente Jurídico", "Coleção de leis e jurisprudência", SECONDARY),
            ("FAQ Inteligente", "Base de conhecimento interna", ACCENT),
            ("Análise de Contratos", "Templates e cláusulas", PURPLE),
        ]
        
        for nome, desc, cor in apps_data:
            box = Rectangle(width=5.5, height=0.9, color=cor, stroke_width=2)
            
            label = Text(nome, font_size=20, color=cor, font=MONO)
            label.move_to(box.get_center() + LEFT * 1.2)
            
            descricao = Text(desc, font_size=14, color=GRAY, font=MONO)
            descricao.next_to(label, RIGHT, buff=1.5)
            
            apps.add(VGroup(box, label, descricao))
        
        apps.arrange(DOWN, buff=0.4)
        apps.center()
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.6)
        
        for app in apps:
            self.play(FadeIn(app), run_time=0.6)
        
        self.wait(3)


class Conclusao_Scene3_Proximos(Scene):
    """Próximos passos."""
    
    def construct(self):
        self.camera.background_color = BG
        
        # Título
        titulo = Text("Próximos Passos", font_size=36, color=WHITE, font=MONO)
        titulo.to_edge(UP, buff=0.4)
        
        # Passos
        passos = VGroup()
        
        p1 = Text("1. Pratique com dados reais", font_size=24, color=PRIMARY, font=MONO)
        p2 = Text("2. Experimente diferentes chunks", font_size=24, color=SECONDARY, font=MONO)
        p3 = Text("3. Compare vector stores", font_size=24, color=ACCENT, font=MONO)
        p4 = Text("4. Meça qualidade das respostas", font_size=24, color=PURPLE, font=MONO)
        
        passos.add(p1, p2, p3, p4)
        passos.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        passos.shift(DOWN * 0.3)
        
        # Call to action
        cta = Text("Material em: luksamuk.codes/pages/guilda-ia",
                  font_size=20, color=GRAY, font=MONO)
        cta.to_edge(DOWN, buff=0.6)
        
        # Animações
        self.play(FadeIn(titulo), run_time=0.6)
        
        for p in passos:
            self.play(FadeIn(p), run_time=0.6)
        
        self.play(FadeIn(cta), run_time=1)
        
        self.wait(3)


# ============================================================================
# INSTRUÇÕES
# ============================================================================
"""
RENDERIZAR TODAS AS CENAS:
    source ~/manim-env/bin/activate
    
    # Introdução
    manim -qh rag_lessons.py Intro_Scene1_Titulo Intro_Scene2_Problema Intro_Scene3_Solucao
    
    # Chunking
    manim -qh rag_lessons.py Chunking_Scene1_Hook Chunking_Scene2_Problema Chunking_Scene3_Solucao
    
    # Vector Store
    manim -qh rag_lessons.py VectorStore_Scene1_Hook VectorStore_Scene2_Solucao
    
    # Retrieval
    manim -qh rag_lessons.py Retrieval_Scene1_Hook Retrieval_Scene2_Processo
    
    # Pipeline
    manim -qh rag_lessons.py RAGPipeline_Scene1_Juntando RAGPipeline_Scene2_Resumo
    
    # Conclusão
    manim -qh rag_lessons.py Conclusao_Scene1_Resumo Conclusao_Scene2_Aplicacao Conclusao_Scene3_Proximos

SINCRONIZAR:
    python sync_rag_lessons.py
"""