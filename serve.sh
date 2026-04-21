#!/bin/bash
# serve.sh - Serve the site locally (run by user)
# Usage: ./serve.sh [port]

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
HTTP_PORT="${1:-8080}"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${BLUE}[SERVE]${NC} $1"; }
log_success() { echo -e "${GREEN}[OK]${NC} $1"; }

# Check if docs/ exists
if [ ! -d "$REPO_DIR/docs" ]; then
    echo "Erro: docs/ não existe. Rode ./build.sh primeiro."
    exit 1
fi

log_success "Servidor rodando em http://localhost:$HTTP_PORT"
log_info "Pressione Ctrl+C para parar"

cd "$REPO_DIR/docs"
python3 -m http.server "$HTTP_PORT"