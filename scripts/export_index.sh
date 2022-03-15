#!/bin/bash
for f in `find src/ -maxdepth 1 -name "*.org"`; do
    echo "$f";
    emacs --batch \
	  -l "/root/.emacs.d/init.el" \
	  --kill \
	  "$f" \
	  -f org-html-export-to-html;
    mv "${f%%.org}.html" docs/
done
