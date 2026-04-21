#!/bin/bash
# local-serve.sh - Build and serve the blog locally for testing
# Usage: ./local-serve.sh [command]
#   Commands:
#     build    - Build HTML files only
#     serve    - Build and serve locally (default)
#     clean    - Remove docs/ directory
#     all      - Build, serve, then clean after Ctrl+C

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
DOCKER_IMAGE="luksamuk/emacs-export:hermes"
CONTAINER_NAME="luksamuk-blog-serve"
HTTP_PORT="${HTTP_PORT:-8080}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

check_docker() {
    if ! command -v docker &> /dev/null; then
        log_error "Docker não está instalado. Instale com: sudo pacman -S docker"
        exit 1
    fi
    if ! docker info &> /dev/null; then
        log_error "Docker não está rodando. Inicie com: sudo systemctl start docker"
        exit 1
    fi
}

pull_image() {
    log_info "Verificando imagem Docker..."
    if ! docker image inspect "$DOCKER_IMAGE" &> /dev/null; then
        log_info "Baixando imagem $DOCKER_IMAGE..."
        docker pull "$DOCKER_IMAGE"
    fi
    log_success "Imagem disponível"
}

build_site() {
    log_info "Construindo site..."
    cd "$REPO_DIR"
    
    # Create docs directory structure
    docker run --rm \
        -v "$REPO_DIR:/root/app" \
        -w /root/app \
        "$DOCKER_IMAGE" \
        sh -c "mkdir -p docs/posts docs/pages docs/talks docs/aulas docs/static docs/slides"
    
    # Run build scripts
    docker run --rm \
        -v "$REPO_DIR:/root/app" \
        -w /root/app \
        "$DOCKER_IMAGE" \
        sh ./ci-run.sh
    
    # Corrigir permissoes (arquivos criados pelo Docker sao root)
    find "$REPO_DIR/docs" -type d -exec chmod 755 {} \; 2>/dev/null
    find "$REPO_DIR/docs" -type f -exec chmod 644 {} \; 2>/dev/null
    find "$REPO_DIR/docs" -exec chown $(id -u):$(id -g) {} 2>/dev/null || true
    
    log_success "Build completo em docs/"
}

serve_site() {
    log_info "Iniciando servidor local na porta $HTTP_PORT..."
    log_info "Acesse: http://localhost:$HTTP_PORT"
    log_info "Pressione Ctrl+C para parar"
    
    cd "$REPO_DIR/docs"
    python3 -m http.server "$HTTP_PORT"
}

clean_docs() {
    log_info "Limpando docs/..."
    rm -rf "$REPO_DIR/docs"
    log_success "docs/ removido"
}

serve_background() {
    # Serve in background, return when user presses Ctrl+C
    trap 'log_info "Servidor parado"; exit 0' INT
    
    cd "$REPO_DIR/docs"
    python3 -m http.server "$HTTP_PORT" &
    SERVER_PID=$!
    
    log_success "Servidor rodando em http://localhost:$HTTP_PORT"
    log_info "Pressione Ctrl+C para parar"
    
    wait $SERVER_PID
}

case "${1:-serve}" in
    build)
        check_docker
        pull_image
        build_site
        ;;
    serve)
        check_docker
        pull_image
        build_site
        serve_site
        ;;
    clean)
        clean_docs
        ;;
    all)
        check_docker
        pull_image
        build_site
        
        # Set up cleanup on exit
        trap 'log_info "Limpando..."; clean_docs; exit 0' INT TERM
        
        log_info "Servidor iniciando... (Ctrl+C para parar e limpar)"
        serve_site
        ;;
    *)
        echo "Uso: $0 {build|serve|clean|all}"
        echo ""
        echo "  build  - Apenas constrói os arquivos HTML"
        echo "  serve   - Constrói e serve localmente (padrão)"
        echo "  clean   - Remove a pasta docs/"
        echo "  all     - Constrói, serve, e limpa ao sair (Ctrl+C)"
        exit 1
        ;;
esac