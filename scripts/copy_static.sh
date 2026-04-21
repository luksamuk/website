#!/bin/bash
cp -r src/img docs/

cp -r src/posts/img \
   src/posts/win98 \
   docs/posts/

cp -r src/css src/js src/files docs/

cp -r \
   src/pages/images \
   src/pages/img \
   docs/pages/

# Copy nested img directories for sub-pages
cp -r src/pages/guilda-ia/img docs/pages/guilda-ia/ 2>/dev/null || true

cp -r \
   src/talks/images \
   src/talks/img \
   src/talks/git_img \
   src/talks/techimera \
   src/talks/pragmatic \
   src/talks/psxprog \
   docs/talks/

# Copy slide assets (images, gifs)
mkdir -p docs/slides
cp src/slides/*.gif docs/slides/ 2>/dev/null || true
cp src/slides/*.png docs/slides/ 2>/dev/null || true
cp src/slides/*.jpg docs/slides/ 2>/dev/null || true

cp -r static docs/

# Copy root-level static files (CNAME, keybase.txt, etc.)
cp src/root/* docs/ 2>/dev/null || true

# Copy Atom feed
cp src/feed.xml docs/ 2>/dev/null || true

chmod -R +r docs/*
chmod -R +r docs/static/*