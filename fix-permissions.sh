#!/bin/bash
# fix-permissions.sh - Corrige permissoes e move arquivos da guilda para o local correto
# Execute: cd ~/git/website && ./fix-permissions.sh

set -e

echo "Corrigindo permissoes..."
sudo chown -R $USER:$USER docs/

echo "Organizando arquivos da guilda..."
mkdir -p docs/pages/guilda-ia

# Mover arquivos da guilda (numerados e index.html)
for f in 01-nomenclaturas 02-prompting 03-python-api 04-estrutura-agente 05-primeira-ferramenta 06-multiplas-ferramentas 07-projeto-integrador 08-rag 09-testes 10-agente-completo 11-projeto-final 12-apresentacoes index; do
    if [ -f "docs/pages/${f}.html" ]; then
        mv "docs/pages/${f}.html" docs/pages/guilda-ia/
        echo "Movido: ${f}.html"
    fi
done

echo "Verificando estrutura final..."
ls -la docs/pages/guilda-ia/

echo "Pronto! Agora voce pode servir localmente:"
echo "  cd ~/git/website/docs && python3 -m http.server 8080"