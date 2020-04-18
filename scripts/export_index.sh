#!/bin/sh
emacs --batch -l "~/.emacs.d/init.el" --kill src/index.org -f org-html-export-to-html
mv src/index.html docs/index.html
