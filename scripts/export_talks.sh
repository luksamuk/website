#!/bin/bash
for f in `find src/talks -name "*.org"`; do
    echo "$f";
    if [ -f "${f%%.org}-bindings.el" ]; then
	emacs --batch \
	      -l "/root/.emacs.d/init.el" \
	      -l "${f%%.org}-bindings.el" \
	      --kill \
	      "$f" \
	      -f org-reveal-export-to-html;
    else
	emacs --batch \
	      -l "/root/.emacs.d/init.el" \
	      --kill \
	      "$f" \
	      -f org-reveal-export-to-html;
    fi
    mv "${f%%.org}.html" docs/talks/
done
