all: pdf

# If you decide to go with pandoc-citeproc
#	pandoc -s -F pandoc-crossref -F pandoc-citeproc meta.yaml --data-dir=data-dir --template=mytemplate.tex -N \
#	-f markdown -t latex+raw_tex+tex_math_dollars+citations -o main.pdf main.md

# You can still use pandoc-crossref to easily reference figures with [@fig:label]

STYLE_DIR=../style
STYLE=$(STYLE_DIR)/apa-aut.csl
# DOC_STYLE=$(STYLE_DIR)/sdm.docx
# TEX_TMPL=$(STYLE_DIR)/sdm.tex
CSS_FILE=$(STYLE_DIR)/aut.css

NAME=will-ai-destroy-humankind
BIB_FILE=ai.bib

pdf:
	pandoc -s \
		--number-section \
		--filter pandoc-crossref \
		--filter pandoc-citeproc \
		--bibliography=$(BIB_FILE) \
		--csl=$(STYLE) \
		--metadata=link-citations \
		--metadata=reference-section-title:References \
		--pdf-engine=xelatex \
	 	-f markdown \
		-o $(NAME).pdf $(NAME).md
	# \
	--number-section \
	--template=$(TEX_TMPL) \
		--filter pandoc-citeproc \

html:
	pandoc -s -F pandoc-citeproc --bibliography=$(BIB_FILE) --csl=$(STYLE) -N \
		--metadata=link-citations \
		--metadata=reference-section-title:References \
		--css $(STYLE_DIR)/aut.css \
		-f markdown -t html -o $(NAME).html $(NAME).md

docx:
	pandoc -s -F pandoc-citeproc --bibliography=$(BIB_FILE) --csl=$(STYLE) -N \
		--metadata=link-citations \
		--metadata=reference-section-title:References \
	 	-f markdown -t docx -o $(NAME).docx $(NAME).md

	# \
	 	--reference-doc=$(DOC_STYLE) \

