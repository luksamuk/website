#!/bin/bash
# Soon: -l init.el
for f in `find src/posts -name "*.org"`; do
    echo "$f";
    emacs --kill "$f" -f org-reveal-export-to-html;
    mv "${f%%.org}.html" docs/posts/
done
