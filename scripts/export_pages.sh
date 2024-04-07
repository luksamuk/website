#!/bin/bash
for f in `find src/pages -name "*.org"`; do
    echo "$f";
    emacs --batch \
	  -l "/root/.emacs.d/init.el" \
	  -l "./src/bindings.el" \
	  --kill \
	  "$f" \
	  -f org-html-export-to-html;
    mv "${f%%.org}.html" docs/pages/;
    cp src/pages/*.cpp docs/pages;
done

