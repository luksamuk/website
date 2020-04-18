#!/bin/bash
# Soon: -l init.el
for f in `find src/pages -name "*.org"`; do
    echo "$f";
    emacs --kill "$f" -f org-html-export-to-html;
    mv "${f%%.org}.html" docs/pages/
done

