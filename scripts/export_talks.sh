#!/bin/bash
for f in `find src/talks -name "*.org"`; do
    echo "$f";
    emacs --batch \
	  -l "/root/.emacs.d/init.el" \
	  --kill \
	  "$f" \
	  -f org-reveal-export-to-html;
    mv "${f%%.org}.html" docs/talks/
done
