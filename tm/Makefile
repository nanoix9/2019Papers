# If you decide to go with pandoc-citeproc
#	pandoc -s -F pandoc-crossref -F pandoc-citeproc meta.yaml --data-dir=data-dir --template=mytemplate.tex -N \
#	-f markdown -t latex+raw_tex+tex_math_dollars+citations -o main.pdf main.md

# You can still use pandoc-crossref to easily reference figures with [@fig:label]

STYLE_DIR=../style
# STYLE=$(STYLE_DIR)/apa-aut.csl
# STYLE=$(STYLE_DIR)/apa6.csl
STYLE=$(STYLE_DIR)/ieee.csl
# DOC_STYLE=$(STYLE_DIR)/sdm.docx
# TEX_TMPL=$(STYLE_DIR)/raw-body.tex
TEX_TMPL=ass1-tmpl.tex
# TEX_TMPL=$(STYLE_DIR)/tex2.tex
# CSS_FILE=$(STYLE_DIR)/pubcss-ieee.css

# NAME=will-ai-destroy-humankind
NAME=ass1
NAME2=as2
BIB_FILE=ass1.bib
# BIB_FILE=../ai/ai.bib
FIG_FILES=as2-algo

DRAW=/Applications/draw.io.app/Contents/MacOS/draw.io
TEX=pdflatex
TEX=pdflatex -shell-escape

all: tex

tex-b:
	pandoc \
		--number-section \
		--biblatex \
		--filter pandoc-fignos \
	 	-f markdown+raw_attribute \
		-o $(NAME)-b.tex $(NAME).md

tex:
	pandoc -s \
		--number-section \
		--biblatex \
		--filter pandoc-fignos \
		--template=$(TEX_TMPL) \
		--metadata=link-citations \
		--metadata=reference-section-title:Reference \
	 	-f markdown+raw_attribute \
		-t latex \
		-o $(NAME).tex $(NAME).md

	# \
	--number-section \
	--template=$(TEX_TMPL) \
		--table-of-contents \
		--filter pandoc-citeproc \
		
tex2pdf:
	# bibtool --  'rename.field{title=title2}' $(BIB_FILE) \
		| 
	# bibtool --  'add.field{note="\href{%s(url)}{this is a note}"}' $(BIB_FILE) -o ass1-tmp.bib
	$(TEX) $(NAME)
	bibtex $(NAME)
	$(TEX) $(NAME)
	$(TEX) $(NAME)
	# dvipdfm $(NAME).dvi
	
tp: tex tex2pdf


tex-2: as2-py as2-eval-py
	pandoc -s \
		--number-section \
		--biblatex \
		--filter pandoc-fignos \
		--template=$(TEX_TMPL) \
		--metadata=link-citations \
		--metadata=reference-section-title:Reference \
	 	-f markdown \
		-t latex \
		-o $(NAME2).tex $(NAME2).md

	# \
		--include-after-body appendix.tex \
	--number-section \
	--template=$(TEX_TMPL) \
		--table-of-contents \
		--filter pandoc-citeproc \
		
tex2pdf-2:
	# bibtool --  'rename.field{title=title2}' $(BIB_FILE) \
		| 
	# bibtool --  'add.field{note="\href{%s(url)}{this is a note}"}' $(BIB_FILE) -o ass1-tmp.bib
	$(TEX) $(NAME2)
	bibtex $(NAME2)
	$(TEX) $(NAME2)
	$(TEX) $(NAME2)
	# dvipdfm $(NAME).dvi
	
as2: tex-2 tex2pdf-2
	mv as2.pdf COMP814_Fang_19049045.pdf

clean:
	rm *.aux *.dvi *.fdb_latexmk *.fls *.log *.synctex.gz *.bbl *.blg

pdf:
	pandoc -s \
		--table-of-contents \
		--number-section \
		--filter pandoc-crossref \
		--filter pandoc-citeproc \
		--bibliography=$(BIB_FILE) \
		--csl=$(STYLE) \
		--template=$(TEX_TMPL) \
		--metadata=link-citations \
		--metadata=reference-section-title:Reference \
		--pdf-engine=xelatex \
	 	-f markdown \
		-o $(NAME).pdf $(NAME).md
	# \
	--number-section \
	--template=$(TEX_TMPL) \
		--filter pandoc-citeproc \

html:
	pandoc -s \
		--filter pandoc-crossref \
		--filter pandoc-citeproc \
		--bibliography=$(BIB_FILE) \
		--csl=$(STYLE) \
		--metadata=link-citations \
		--metadata=reference-section-title:Reference \
		--css=$(CSS_FILE) \
	 	-f markdown \
		-t html \
		-o $(NAME).html $(NAME).md
	
	# \
		--pdf-engine=xelatex \
		--template=$(TEX_TMPL) \

docx:
	pandoc -s -F pandoc-citeproc --bibliography=$(BIB_FILE) --csl=$(STYLE) -N \
		--metadata=link-citations \
		--metadata=reference-section-title:References \
	 	-f markdown -t docx -o $(NAME).docx $(NAME).md

	# \
	 	--reference-doc=$(DOC_STYLE) \

as2-py:
	head -n 2 as2.py > as2.py.tmp
	grep -v -E '^\s*#[^#]' as2.py | grep -v '´' | sed -e 's/\(\s*\)##/\1#/' >> as2.py.tmp

as2-run: 
	python as2.py

as2-eval-py:
	head -n 2 as2-eval.py > as2-eval.py.tmp
	grep -v -E '^\s*#[^#]' as2-eval.py | grep -v '´' | sed -e 's/\(\s*\)##/\1#/' >> as2-eval.py.tmp

as2-show: 
	python as2-eval.py show

as2-eval: 
	python as2-eval.py eval $(TOPICS)

svg:
	for f in $(FIG_FILES); do \
		$(DRAW) -x -f svg -o $${f}.svg $${f}.drawio; \
		inkscape --export-filename=$${f}.pdf --export-latex $${f}.svg; \
		sed -i -e 's/_/\\_/g' $${f}.pdf_tex; \
	done