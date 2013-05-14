ROOTNAME = main
PDFFILE = $(ROOTNAME).pdf
PSFILE = $(ROOTNAME).ps
DVIFILE = $(ROOTNAME).dvi
TEXFILE = $(ROOTNAME).tex

all: standard

standard: 
	make bbl
	make pdflatex


pdflatex: 
	pdflatex $(ROOTNAME)
	pdflatex $(ROOTNAME)
	pdflatex $(ROOTNAME)
	
bbl:
	pdflatex $(ROOTNAME)
	bibtex $(ROOTNAME) 

clean:
	rm -f *.dvi *.ps *.pdf *.aux *.bbl *.blg *.ent *.log *.out $(DRAFT_SETTINGS)

