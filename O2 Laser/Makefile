all: build/main.pdf

# Sample on how to include python scripts
build/intensity.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 plot.py  

build/spectrum.pdf: spectroscopy.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 spectroscopy.py

build/main.pdf: build/intensity.pdf
build/main.pdf: build/spectrum.pdf

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
