all: test_paper

# If you decide to go with pandoc-citeproc
#	pandoc -s -F pandoc-crossref -F pandoc-citeproc meta.yaml --data-dir=data-dir --template=mytemplate.tex -N \
#	-f markdown -t latex+raw_tex+tex_math_dollars+citations -o main.pdf main.md

# You can still use pandoc-crossref to easily reference figures with [@fig:label]

paper:
	pandoc -s -F pandoc-crossref --natbib meta.yaml --template=mytemplate.tex -N \
	 -f markdown -t latex+raw_tex+tex_math_dollars+citations -o main.tex main.md
	pdflatex main.tex &> /dev/null
	bibtex main &> /dev/null
	pdflatex main.tex &> /dev/null
	pdflatex main.tex &> /dev/null

pdf:
	pandoc -s -F pandoc-crossref --bibliography=testbib.bib --csl=apa.csl -N \
	 -f markdown -t latex+raw_tex+tex_math_dollars+citations -o ass1a.tex ass1a.md
	pdflatex ass1a.tex &> /dev/null
	bibtex ass1a &> /dev/null
	pdflatex ass1a.tex &> /dev/null
	pdflatex ass1a.tex &> /dev/null

html:
	pandoc -s -F pandoc-crossref --bibliography=ass1a.bib --csl=../style/apa.csl -N \
	 -f markdown -t html -o ass1a.html ass1a.md

docx:
	pandoc -s -F pandoc-crossref --bibliography=biblio.bib --csl=apa.csl -N \
	--reference-doc=/Users/stone/aut/SDM/blockchain/Phengthalangsy_Khounkham_and_Fang_Stone_EmergingTechReport_v2.docx \
	 -f markdown -t docx -o ass1a.docx ass1a.md
