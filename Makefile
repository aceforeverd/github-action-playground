
.PHONY: all foo

all:
	@if [ "0" = "0" ]; then \
	    # comment line \
	    echo "all in"; \
	else \
	    echo "nobody"; \
	fi

foo:
	echo $$SHELL
