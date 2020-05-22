all: pdf

# If you decide to go with pandoc-citeproc
#	pandoc -s -F pandoc-crossref -F pandoc-citeproc meta.yaml --data-dir=data-dir --template=mytemplate.tex -N \
#	-f markdown -t latex+raw_tex+tex_math_dollars+citations -o main.pdf main.md

# You can still use pandoc-crossref to easily reference figures with [@fig:label]

STYLE_DIR=../style
# STYLE=$(STYLE_DIR)/apa-aut.csl
STYLE=$(STYLE_DIR)/apa7.csl
# DOC_STYLE=$(STYLE_DIR)/sdm.docx
TEX_TMPL=$(STYLE_DIR)/sdm.tex
TEX_TMPL=$(STYLE_DIR)/tex2.tex
CSS_FILE=$(STYLE_DIR)/aut.css
BEAMER_TMPL=$(STYLE_DIR)/beamer.tex

NAME=dl-proposal
SLIDES_NAME=proposal-slides
BIB_FILE=dl.bib

TEX=pdflatex
# TEX=pdflatex --shell-escape

all: tp

clean:
	rm *.aux *.dvi *.fdb_latexmk *.fls *.log *.synctex.gz *.bbl *.blg

fig:
	inkscape --export-filename=model.pdf --export-latex model2.svg
	sed -i -e 's/lineheight{1.25}/lineheight{1}/g' model.pdf_tex

sl: sl-tex sl-tex2pdf

sl-tex2pdf:
	$(TEX) $(SLIDES_NAME).tex
	biber $(SLIDES_NAME)
	$(TEX) $(SLIDES_NAME).tex
	$(TEX) $(SLIDES_NAME).tex

sl-tex:
	pandoc -s --biblatex \
		--table-of-contents \
		--slide-level=2 \
		--template=$(BEAMER_TMPL) \
		-t beamer $(SLIDES_NAME).md \
		-o $(SLIDES_NAME).tex

tex:
	pandoc -s \
		--number-section \
		--biblatex \
		--template=$(TEX_TMPL) \
		--include-after-body appendix.tex \
		--metadata=link-citations \
		--metadata=reference-section-title:References \
	 	-f markdown \
		-o $(NAME).tex \
		$(NAME).md
	
	# -t latex+raw_tex+tex_math_dollars+citations \
		-F pandoc-crossref  \
		--filter pandoc-citeproc \

tex2pdf:
	$(TEX) $(NAME).tex  # > /dev/null
	biber $(NAME)
	$(TEX) $(NAME).tex  # > /dev/null
	$(TEX) $(NAME).tex  # > /dev/null

tp: tex tex2pdf
	mv dl-proposal.pdf COMP825_proposal_Fang_19049045.pdf

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

