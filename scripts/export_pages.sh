#!/bin/bash
for f in `find src/pages -name "*.org"`; do
    echo "$f";
    if [ -f "${f%%.org}-bindings.el" ]; then
	emacs --batch \
	      -l "/root/.emacs.d/init.el" \
	      -l "${f%%.org}-bindings.el" \
	      --kill \
	      "$f" \
	      -f org-html-export-to-html;
    else
	emacs --batch \
	      -l "/root/.emacs.d/init.el" \
	      -l "./src/pages/bindings.el" \
	      --kill \
	      "$f" \
	      -f org-html-export-to-html;
    fi
    mv "${f%%.org}.html" docs/pages/;
    cp src/pages/*.cpp docs/pages;
done

