#!/bin/bash
for f in `find src/posts -name "*.org"`; do
    echo "$f";
    emacs --batch \
	  -l "~/.emacs.d/init.el" \
	  -l "./src/bindings.el" \
	  --kill \
	  "$f" \
	  -f org-html-export-to-html;
    mv "${f%%.org}.html" docs/posts/
done

