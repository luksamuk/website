all:
	docker run -it --rm -v $(shell pwd):/root/app luksamuk/emacs-export sh app/ci-run.sh
