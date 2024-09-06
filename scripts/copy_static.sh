#!/bin/bash
cp -r src/img docs/

cp -r src/posts/img \
   src/posts/win98 \
   docs/posts/

cp -r src/css src/files docs/

cp -r \
   src/pages/images \
   src/pages/img \
   docs/pages/

cp -r \
   src/talks/images \
   src/talks/img \
   src/talks/git_img \
   src/talks/techimera \
   src/talks/pragmatic \
   src/talks/psxprog \
   docs/talks/

cp -r static docs/

chmod -R +r docs/*
chmod -R +r docs/static/*
