all: pdf

# If you decide to go with pandoc-citeproc
#	pandoc -s -F pandoc-crossref -F pandoc-citeproc meta.yaml --data-dir=data-dir --template=mytemplate.tex -N \
#	-f markdown -t latex+raw_tex+tex_math_dollars+citations -o main.pdf main.md

# You can still use pandoc-crossref to easily reference figures with [@fig:label]

STYLE_DIR=../style
STYLE=$(STYLE_DIR)/apa-aut.csl
# STYLE=$(STYLE_DIR)/apa6.csl
# DOC_STYLE=$(STYLE_DIR)/sdm.docx
TEX_TMPL=$(STYLE_DIR)/sdm.tex
# TEX_TMPL=$(STYLE_DIR)/times.tex
CSS_FILE=$(STYLE_DIR)/aut.css

NAME=will-ai-destroy-humankind
NAME=dl-proposal
BIB_FILE=dl.bib

all: pdf

tex:
	pandoc -s \
		--number-section \
		--bibliography=$(BIB_FILE) \
		--csl=$(STYLE) \
		--template=$(TEX_TMPL) \
		--metadata=link-citations \
		--metadata=reference-section-title:References \
	 	-f markdown \
		-o $(NAME).tex \
		$(NAME).md
	
	# -t latex+raw_tex+tex_math_dollars+citations \
		-F pandoc-crossref  \
		--filter pandoc-citeproc \
	
	# xelatex $(NAME).tex
	# biber $(NAME)
	# xelatex $(NAME).tex
	# xelatex $(NAME).tex

pdf:
	pandoc -s \
		--number-section \
		--filter pandoc-crossref \
		--filter pandoc-citeproc \
		--bibliography=$(BIB_FILE) \
		--csl=$(STYLE) \
		--template=$(TEX_TMPL) \
		--metadata=link-citations \
		--metadata=reference-section-title:Reference \
		--pdf-engine=pdflatex \
	 	-f markdown \
		-o COMP825_mid_term_proposal_Fang_19049045.pdf $(NAME).md
	# \
		--table-of-contents \
	--number-section \
	--template=$(TEX_TMPL) \
		--pdf-engine=xelatex \
		--filter pandoc-citeproc \

html:
	pandoc -s -F pandoc-citeproc --bibliography=$(BIB_FILE) --csl=$(STYLE) -N \
		--metadata=link-citations \
		--metadata=reference-section-title:References \
		--css $(STYLE_DIR)/aut.css \
		-f markdown -t html -o $(NAME).html $(NAME).md

docx:
	pandoc -s \
		-F pandoc-citeproc \
		--bibliography=$(BIB_FILE) \
		--csl=$(STYLE) -N \
		--metadata=link-citations \
		--metadata=reference-section-title:References \
	 	-f markdown \
		-t docx \
		-o COMP825_mid_term_proposal_Fang_19049045.docx $(NAME).md

	# \
	 	--reference-doc=$(DOC_STYLE) \

