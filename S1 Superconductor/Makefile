all: build/main.pdf

# Sample on how to include python scripts
build/conductivity_example.pdf: conductivity_example.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 conductivity_example.py

build/resistance-temperature.pdf: resistance-temperature.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 resistance-temperature.py

build/main.pdf: build/conductivity_example.pdf
build/main.pdf: build/resistance-temperature.pdf

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
