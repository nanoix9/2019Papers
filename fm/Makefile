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

NAME=ass1
BIB_FILE=dl.bib

TEX=pdflatex
# TEX=xelatex

all: q1 q3

clean:
	rm *.aux *.dvi *.fdb_latexmk *.fls *.log *.synctex.gz *.bbl *.blg *.class

zip:
	zip ENSE803_A1_Fang_19049045.zip Q1_Rational_Numbers.pdf Q2_IsomorphicAlgebras.java Q3_Formal_Methods_in_IT.pdf

q2:
	javac Q2_IsomorphicAlgebras.java
	java Q2_IsomorphicAlgebras

q3: q3.pdf
	mv q3.pdf Q3_Formal_Methods_in_IT.pdf

q3.tex: q3.md q3-template.tex
	pandoc -s \
		--biblatex \
		--template=q3-template.tex \
		--metadata=link-citations \
		--metadata=reference-section-title:References \
	 	-f markdown \
		-o q3.tex \
		q3.md

	# --number-section \
	
q3.pdf: q3.tex
	$(TEX) q3.tex
	biber q3
	$(TEX) q3.tex
	$(TEX) q3.tex

tex: $(NAME).md $(TEX_TMPL)
	pandoc -s \
		--number-section \
		--biblatex \
		--template=$(TEX_TMPL) \
		--metadata=link-citations \
		--metadata=reference-section-title:References \
	 	-f markdown \
		-o $(NAME).tex \
		$(NAME).md
	
	# -t latex+raw_tex+tex_math_dollars+citations \
		-F pandoc-crossref  \
		--filter pandoc-citeproc \

tex2pdf: $(NAME).tex
	$(TEX) $(NAME).tex
	# biber $(NAME)
	# $(TEX) $(NAME).tex
	# $(TEX) $(NAME).tex

q1: tex tex2pdf
	mv $(NAME).pdf Q1_Rational_Numbers.pdf

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

