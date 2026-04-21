#!/bin/bash
docker run -it --rm -v "$PWD":/root/app luksamuk/emacs-export:hermes sh app/ci-run.sh
