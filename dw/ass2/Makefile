# If you decide to go with pandoc-citeproc
#	pandoc -s -F pandoc-crossref -F pandoc-citeproc meta.yaml --data-dir=data-dir --template=mytemplate.tex -N \
#	-f markdown -t latex+raw_tex+tex_math_dollars+citations -o main.pdf main.md

# You can still use pandoc-crossref to easily reference figures with [@fig:label]

STYLE_DIR=../../style
# STYLE=$(STYLE_DIR)/apa-aut.csl
# STYLE=$(STYLE_DIR)/apa6.csl
STYLE=$(STYLE_DIR)/ieee.csl
# DOC_STYLE=$(STYLE_DIR)/sdm.docx
TEX_TMPL=$(STYLE_DIR)/tex2.tex
# TEX_TMPL=ass1-tmpl.tex
CSS_FILE=$(STYLE_DIR)/pubcss-ieee.css

# NAME=will-ai-destroy-humankind
NAME=projectReport
BIB_FILE=ass1.bib
# BIB_FILE=../ai/ai.bib

TEX=pdflatex
DRAW=/Applications/draw.io.app/Contents/MacOS/draw.io

all: tp

tex:
	pandoc -s \
		--number-section \
		--biblatex \
		--filter pandoc-fignos \
		--bibliography=$(BIB_FILE) \
		--template=$(TEX_TMPL) \
		--metadata=link-citations \
		--metadata=reference-section-title:Reference \
	 	-f markdown \
		-o $(NAME).tex $(NAME).md

	# \
	--number-section \
		--csl=$(STYLE) \
	--template=$(TEX_TMPL) \
		--table-of-contents \
		--filter pandoc-citeproc \
		
tex2pdf:
	# bibtool --  'rename.field{title=title2}' $(BIB_FILE) \
		| 
	# bibtool --  'add.field{note="\href{%s(url)}{this is a note}"}' $(BIB_FILE) -o ass1-tmp.bib
	# $(TEX) $(NAME)
	# bibtex $(NAME)
	$(TEX) $(NAME)
	$(TEX) $(NAME)
	# dvipdfm $(NAME).dvi
	# mv $(NAME).pdf Fang_19049045.pdf
	
tp: tex tex2pdf

clean:
	rm *.aux *.dvi *.fdb_latexmk *.fls *.log *.synctex.gz *.bbl *.blg

svg:
	$(DRAW) -x -f svg -o star-schema.svg star-schema.drawio 
	inkscape --export-filename=star-schema.pdf --export-latex star-schema.svg
	sed -i -e 's/_/\\_/g' star-schema.pdf_tex

png:
	$(DRAW) -x -f png -o star-schema.png star-schema.drawio 