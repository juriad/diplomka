.PHONY: all

images := $(patsubst %.dot,%.pdf,$(wildcard *.dot))

all: thesis.pdf

# LaTeX must be run multiple times to get references right
thesis.pdf: thesis.tex $(wildcard *.tex) bibliography.bib Makefile $(images)
	pdflatex $<
	bibtex thesis
	pdflatex $<
	pdflatex $<


%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f *.log *.dvi *.aux *.toc *.lof *.lot *.out *.bbl *.blg
	rm -f thesis.pdf $(images)

show: thesis.pdf
	zathura --synctex-forward=0:0:$< $<
