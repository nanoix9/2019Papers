all: test_paper

# If you decide to go with pandoc-citeproc
#	pandoc -s -F pandoc-crossref -F pandoc-citeproc meta.yaml --data-dir=data-dir --template=mytemplate.tex -N \
#	-f markdown -t latex+raw_tex+tex_math_dollars+citations -o main.pdf main.md

# You can still use pandoc-crossref to easily reference figures with [@fig:label]

STYLE_DIR=../style
STYLE=$(STYLE_DIR)/apa-aut.csl
DOC_STYLE=$(STYLE_DIR)/sdm.docx
TEX_TMPL=$(STYLE_DIR)/sdm.tex

pdf1:
	pandoc -s -F pandoc-crossref  \
	 -f markdown -t latex+raw_tex+tex_math_dollars+citations -o ass1a.tex ass1a.md
	
	#--natbib meta.yaml --template=mytemplate.tex -N

	pdflatex ass1a.tex &> /dev/null
	bibtex ass1a &> /dev/null
	pdflatex ass1a.tex &> /dev/null
	pdflatex ass1a.tex &> /dev/null


pdf:
	pandoc -s --filter pandoc-citeproc \
		--pdf-engine=xelatex \
		--bibliography=ass1a.bib --csl=$(STYLE) \
		--template=$(TEX_TMPL) \
	 	-f markdown \
		-o ass1a.pdf ass1a.md
	#--number-section \
	--template=$(TEX_TMPL) \

html:
	pandoc -s -F pandoc-crossref --bibliography=ass1a.bib --csl=$(STYLE) -N \
	 -f markdown -t html -o ass1a.html ass1a.md

docx:
	pandoc -s -F pandoc-crossref --bibliography=ass1a.bib --csl=$(STYLE) -N \
	 --reference-doc=$(DOC_STYLE) \
	 -f markdown -t docx -o ass1a.docx ass1a.md
