#!/bin/bash
for f in `find src/pages -name "*.org"`; do
    echo "$f";
    emacs --batch -l "~/.emacs.d/init.el" --kill "$f" -f org-html-export-to-html;
    mv "${f%%.org}.html" docs/pages/
done

