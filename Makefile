.PHONY: test
test:
	pytest test_*.py

ifndef VERBOSE
.SILENT:
endif
