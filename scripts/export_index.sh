#!/bin/bash
# Soon: -l init.el
emacs --kill src/index.org -f org-html-export-to-html
mv src/index.html docs/index.html
