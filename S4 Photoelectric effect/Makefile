all: build/main.pdf


build/photocurrent_incorrect.pdf: analysis_own_measurement.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 analysis_own_measurement.py  

build/main.pdf: build/photocurrent_incorrect.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
