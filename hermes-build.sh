#!/bin/bash
# hermes-build.sh - Build the site (run by Hermes agent)
# Usage: ./hermes-build.sh

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
DOCKER_IMAGE="luksamuk/emacs-export:hermes"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${BLUE}[BUILD]${NC} $1"; }
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

log_info "Construindo site..."

# Create docs directory structure
docker run --rm \
    -v "$REPO_DIR:/root/app" \
    -w /root/app \
    "$DOCKER_IMAGE" \
    sh -c "mkdir -p docs/posts docs/pages docs/talks docs/aulas docs/static docs/slides"

# Run build
docker run --rm \
    -v "$REPO_DIR:/root/app" \
    -w /root/app \
    "$DOCKER_IMAGE" \
    sh ./ci-run.sh

# Fix permissions
find "$REPO_DIR/docs" -type d -exec chmod 755 {} \; 2>/dev/null || true
find "$REPO_DIR/docs" -type f -exec chmod 644 {} \; 2>/dev/null || true
find "$REPO_DIR/docs" -exec chown $(id -u):$(id -g) {} 2>/dev/null || true

log_success "Build completo em docs/"
log_info "Rode ./serve.sh para servir localmente"