#!/bin/bash
# hermes-build-slides.sh - Build only the Reveal.js slides (fast)
# Usage: ./hermes-build-slides.sh [slide-name]
#   slide-name: optional, e.g. "05-estrutura-agente" to build just one slide
#               without arg, builds all slides

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
DOCKER_IMAGE="luksamuk/emacs-export:hermes"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${BLUE}[SLIDES]${NC} $1"; }
log_success() { echo -e "${GREEN}[OK]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Check Docker
if ! command -v docker &> /dev/null; then
    log_error "Docker não está instalado"
    exit 1
fi
if ! docker info &> /dev/null 2>&1; then
    log_error "Docker não está rodando"
    exit 1
fi

# Pull image if needed
if ! docker image inspect "$DOCKER_IMAGE" &> /dev/null 2>&1; then
    log_info "Baixando imagem $DOCKER_IMAGE..."
    docker pull "$DOCKER_IMAGE"
fi

# Ensure output dir exists
mkdir -p "$REPO_DIR/docs/slides"

if [ -n "$1" ]; then
    # Build a single slide
    SLIDE_FILE="src/slides/${1}.org"
    if [ ! -f "$REPO_DIR/$SLIDE_FILE" ]; then
        log_error "Slide não encontrado: $SLIDE_FILE"
        exit 1
    fi

    log_info "Buildando slide: $1..."

    docker run --rm \
        -v "$REPO_DIR:/root/app" \
        -w /root/app \
        "$DOCKER_IMAGE" \
        sh -c "
            if [ -f 'src/slides/${1}-bindings.el' ]; then
                emacs --batch \
                    -l /root/.emacs.d/init.el \
                    -l 'src/slides/${1}-bindings.el' \
                    --kill \
                    'src/slides/${1}.org' \
                    -f org-reveal-export-to-html
            else
                emacs --batch \
                    -l /root/.emacs.d/init.el \
                    --kill \
                    'src/slides/${1}.org' \
                    -f org-reveal-export-to-html
            fi
            mv 'src/slides/${1}.html' docs/slides/
        "
else
    # Build all slides
    log_info "Buildando todos os slides..."

    docker run --rm \
        -v "$REPO_DIR:/root/app" \
        -w /root/app \
        "$DOCKER_IMAGE" \
        sh -c '
            for f in $(find src/slides -name "*.org"); do
                echo "$f"
                base="${f%.org}"
                if [ -f "${base}-bindings.el" ]; then
                    emacs --batch \
                        -l /root/.emacs.d/init.el \
                        -l "${base}-bindings.el" \
                        --kill \
                        "$f" \
                        -f org-reveal-export-to-html
                else
                    emacs --batch \
                        -l /root/.emacs.d/init.el \
                        --kill \
                        "$f" \
                        -f org-reveal-export-to-html
                fi
                mv "${base}.html" docs/slides/
            done
        '
fi

# Fix permissions
find "$REPO_DIR/docs/slides" -type f -exec chmod 644 {} \; 2>/dev/null || true
find "$REPO_DIR/docs/slides" -exec chown $(id -u):$(id -g) {} 2>/dev/null || true

log_success "Slides buildados em docs/slides/"