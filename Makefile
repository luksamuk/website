all:
	docker run -it --rm -v "$PWD":/root/app luksamuk/emacs-export sh app/ci-run.sh
