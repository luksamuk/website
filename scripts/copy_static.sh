#!/bin/bash
cp -r src/img docs/

cp -r src/posts/img docs/posts/

cp -r src/css src/files docs/

cp -r src/pages/images src/pages/img docs/pages/

cp -r src/talks/images src/talks/img docs/talks/

cp -r static docs/

chmod -R +r docs/*
