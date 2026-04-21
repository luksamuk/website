# AGENTS.md — Regras para agentes IA trabalhando neste repositório

## NÃO MEXER

### docs/ — Build output, NÃO commitar
- A pasta `docs/` contém o site gerado e **NÃO** deve ser commitada.
- O pipeline de deploy (`JamesIves/github-pages-deploy-action`) faz deploy de `docs/` para a branch `gh-pages`.
- `docs/` está no `.gitignore` — **NUNCA** remova do `.gitignore`.
- Após o build local (`./hermes-build.sh`), faça staging **seletivo** — only `src/`, scripts, etc.
- Use `git add src/` ou liste arquivos específicos. **NÃO** use `git add -A` ou `git add .`.

## Build

- **Hermes build:** `./hermes-build.sh` (usa Docker `luksamuk/emacs-export:hermes`)
- **NÃO** use `./build.sh` diretamente — erro de permissão em `docs/`.
- SVGs em `src/pages/guilda-ia/img/` podem ser owned by root (Docker). Se write falhar, crie com sufixo `-v2` e atualize referências.

## Vídeos da Guilda

- Scripts Manim + áudio ficam em `src/pages/guilda-ia/videos/`
- Cada aula tem sua subpasta (ex: `aula00/`, `aula01/`)
- Pastas geradas (videos/, audio/) estão no `.gitignore` — só scripts e roteiros são commitados.

## Navbar — Single Source of Truth

A navbar HTML está definida em **`src/navbar.el`** como `luksamuk-nav-wrapper`. Todos os `bindings.el` usam `(load "../navbar.el")` e `(concat luksamuk-nav-wrapper ...)`. 

Arquivos com `#+BIND:` inline (setupfiles .org, avltree, huffman, psx-homebrew, index.org) mantêm a navbar hardcoded — ao alterar a navbar, rode `python3 sync-navbar.py` para sincronizar, e atualize `index.org` manualmente (usa `#+HTML:` inline).

**Links atuais da navbar:** Home | Sobre | Games | Talks | Blog

## Theme Toggle

- JS: `src/js/theme-toggle.js` — carregado via `<script src="/js/theme-toggle.js">`
- Referenciado em: `src/index.org`, `src/pages/setupfile.org`,
  `src/pages/guilda-ia/setupfile.org`, `src/posts/setupfile.org`,
  `src/pages/psx-homebrew.org`
- Respeita `localStorage` e `prefers-color-scheme`

## Navbar Scroll Collapse

- JS: `src/js/nav-scroll.js` — colapsa `#nav-wrapper` ao rolar > 80px
- HTML: `<div id="nav-wrapper">` envolve `<nav id="site-nav">` + `<h1 class="site-title">`
- O nav-wrapper fecha ANTES do page title — títulos e datas ficam no fluxo normal
- CSS: `#nav-wrapper.collapsed` reduz padding, font-size, gap; esconde ícones dos links
- Script usa `DOMContentLoaded` — não roda antes do DOM estar pronto
- Navbar começa expandida (não chama onScroll no load)

## Paleta de Cores

- **Dark theme**: bg `#1e1e2e`, body `#12121e5e`, cards `#282a3a`, border `#33334a`
- **Light theme**: bg `#faf8f0`, cards `#fffdf7`, nav `#e8e6def8`, text `#1F1F1F`
- **Accent**: `#7dd89a` (dark) / `#2a8a4e` (light), hover: `#5abf7a` / `#1f7a3f`

## Links Sociais

- LinkedIn: **REATIVADO** (github.com/luksamuk → linkedin.com/in/luksamuk)
- Twitch: **ADICIONADO** (twitch.tv/luksamuk)
- Guilda de IA: **NAO** está na navbar (evento temporário do semestre)

## OSINT Hardening

### NÃO deve aparecer no site (nem neste arquivo):

- **Nomes de empregadores** — usar descrições genéricas ("Empresa de EdTech", "Empresa de infra fiscal", etc)
- **Telefone** — nunca
- **Email em texto puro** — usar JS injection ou formato "user at domain dot com"
- **Nome completo** — usar "Lucas S. Vieira" (nunca o nome do meio)
- **Cidade específica** — usar "MG, Brasil" (nunca a cidade)
- **Nomes de instituições de ensino** — remover de slides e bio (exceto referências bibliográficas)

### Email — 3 camadas de proteção:

1. **`src/js/email-deobfuscate.js`** — monta email client-side e injeta em `<span id="email-contact">`. Fonte HTML mostra só "Lucas at ProtonMail"
2. **`macros.el`** — ofusca email com HTML entities (`&#NNN;`) nas OG/twitter meta tags. É a ÚNICA exceção que mantém o email real
3. **Posts/talks**: `%e` removido dos preâmbulos. Talks Reveal.js usam formato "at dot" no `#+EMAIL`

### Verificação pós-build:

```bash
grep -rl '<EMAIL>' docs/                      # deve retornar NONE
grep -rl '<DOMINIO-EMPREGADOR>' docs/          # deve retornar NONE
grep -rl '<NOME-COMPLETO>' docs/               # deve retornar NONE
```

**Nota:** O agente Hermes tem os valores reais dessas strings na memória de sessão. Use os patterns reais ao auditar, mas não os escreva em arquivos versionados.

### PII audit em mudanças de CV/experiência:

1. `src/pages/about.org`
2. `src/pages/talks-index.org`
3. `src/index.org`
4. `src/talks/*.org`
5. `src/pages/huffman.org`

### EXIF stripping

Imagens em `src/` devem ter EXIF removido. **NUNCA** rodar em `docs/` (regenerado pelo build):
```bash
find src/ -type f \( -name '*.png' -o -name '*.jpg' \) -exec exiftool -all= {} +
```

### Itens pendentes (não aplicados):

- Verificar WHOIS privacy do domínio
- Audit GitHub profile por exposição de empregador/localização
- Privacy policy (/privacy): **não necessária** para site estático sem analytics/cookies. Considerar se adicionar analytics (Plausible/Umami) no futuro

## Preamble — Email Removido

O token `%e` foi **removido** de todos os preâmbulos de posts e páginas. **NÃO re-adicione `%e`** nos formatos de preâmbulo — o email nunca deve aparecer direto no HTML de posts.

## Portfolio Thumbnails

Imagens de destaque no portfolio usam o script padronizado de overlay:

- **Script**: `~/.hermes/scripts/overlay-thumb.py`
- **Skill Hermes**: `overlay-thumb` (dogfood)
- **Tamanho**: 960×540 (16:9), sempre
- **Localização**: `src/pages/img/portfolio-<name>.png`
- **Estilo**: Overlay verde/azul diagonal, glow no título, scan lines, vinheta, accent #59c5ee
- **EXIF**: Sempre remover após gerar (`exiftool -all= <file>`)

### Uso

```bash
python3 ~/.hermes/scripts/overlay-thumb.py <input> <output> \
    --title "Project Name" --subtitle "Description" --tags "Tech • Stack"
```

Para screenshots de emulador com barras pretas 4:3, adicionar `--crop-4_3`.

## Fluxo: Publicar um Novo Post no Blog

Quando um novo post é criado, existem **4 arquivos** que precisam ser atualizados manualmente (não há automação):

### Checklist

1. **Criar o post** — `src/posts/<slug>.org`
   - Seguir o `setupfile.org` do diretório de posts
   - Definir `#+TITLE`, `#+DATE`, `#+LANGUAGE` (en/pt)
   - Adicionar imagens em `src/posts/img/` conforme necessário
   - Stripping EXIF: `exiftool -all= src/posts/img/*.png`

2. **Gerar thumbnail** — `src/posts/img/thumb-<slug>.png`
   - **Script**: `python3 ~/.hermes/scripts/blog-thumb.py <input> src/posts/img/thumb-<slug>.png`
   - **Tamanho**: 1200×628 (OG standard), fill/crop, **sem overlay/texto/gradientes**
   - Posts sem imagem no conteúdo usam `src/pages/img/blog-thumb-default.png` (não criar thumb personalizado)
   - Verificar que o thumb é referenciado em `macros.el` (convenção: `img/thumb-<slug>.png`)
   - EXIF strip após gerar: `exiftool -all= src/posts/img/thumb-<slug>.png`

3. **Adicionar ao `src/pages/blog.org`** — lista completa de posts
   - Adicionar `<article class="blog-item">` no **topo** da lista (posts mais recentes primeiro)
   - Template:
     ```html
     <article class="blog-item">
     <div class="blog-item-thumb"><a href="/posts/<slug>.html"><img src="/posts/img/thumb-<slug>.png" alt="<title>" loading="lazy"></a></div>
     <div class="blog-item-body">
     <div class="blog-item-header">
     <h2><a href="/posts/<slug>.html"><title></a></h2>
     <span class="blog-date"><Mon DD, YYYY></span>
     </div>
     <p><a href="/posts/<slug>.html" class="blog-link"><description EN></a></p>
     <div class="blog-tags"><span class="badge lang-<xx>"><XX></span> <span class="badge tag-<topic>"><Topic></span></div>
     </div>
     </article>
     ```
   - **CRITICAL**: Alinhar `href` do thumb com `href` do title no mesmo `<article>`. O preamble do Org causa offset!
   - Idiomas: `lang-en` → `EN`, `lang-pt` → `PT`
   - Tags: `tag-ai`, `tag-lisp`, `tag-plan9`, `tag-apl`, `tag-tools`

4. **Atualizar `src/index.org`** — seção "Latest Posts"
   - Adicionar o novo post no **topo** da `<ul class="latest-posts">`
   - Manter apenas os **3-4 posts mais recentes**
   - Template: `<li><a href="./posts/<slug>.html"><title></a><span class="latest-posts-date"><YYYY-MM-DD></span></li>`
   - Se a lista passar de 4 itens, remover o mais antigo

5. **Atualizar `src/feed.xml`** — Atom feed
   - Adicionar `<entry>` no **topo** da lista (logo após `<author>`)
   - Atualizar `<updated>` do feed com timestamp atual
   - Template de entry com thumbnail:
     ```xml
     <entry>
       <title><title></title>
       <link href="https://luksamuk.codes/posts/<slug>.html" rel="alternate"/>
       <link href="https://luksamuk.codes/posts/img/thumb-<slug>.png" rel="enclosure" type="image/png" length="<file-size-bytes>"/>
       <id>https://luksamuk.codes/posts/<slug>.html</id>
       <updated><YYYY-MM-DD>T00:00:00Z</updated>
       <published><YYYY-MM-DD>T00:00:00Z</published>
       <summary><description EN curta></summary>
     </entry>
     ```
   - **Thumbnail no feed**: usar `<link rel="enclosure">` com type `image/png` e o tamanho do arquivo em bytes
   - Posts sem thumb personalizado usam: `<link href="https://luksamuk.codes/pages/img/blog-thumb-default.png" rel="enclosure" type="image/png" length="<size>"/>`
   - Posts em PT mantêm título original em PT no feed; summaries sempre em EN

6. **Build e verificação**
   - `./hermes-build.sh`
   - Verificar localmente com `./serve.sh`
   - Checar que o post, blog list, homepage e feed renderizam corretamente
   - `git add src/` (NÃO `git add -A` — evitar incluir `docs/`)
   - Commit e push

### Post rascunho (NÃO publicar no feed)

- `majestic-post-mortem` — existe em `src/posts/` mas é rascunho (`#+DATE:` vazio, comentários de placeholder). Não adicionar ao feed nem ao blog.org até estar finalizado.

### Notas

- O feed é **100% manual** (`src/feed.xml`). Não é gerado pelo build.
- Summaries no feed são sempre em **inglês**, mesmo para posts em PT.
- A ordem no feed é cronológica decrescente (mais recentes primeiro).
- Thumbnails no feed usam `<link rel="enclosure">` (Atom standard) — leitores RSS que suportam irão exibir.