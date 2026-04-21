all:
	docker run -it --rm -v $(shell pwd):/root/app luksamuk/emacs-export:hermes sh app/ci-run.sh
