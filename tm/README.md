What you need to download to your local disk is "ass1.tex" and "ass1.bib".

"ass1.bib" makes it easier to manage references. It requires bibtex. If you have TexLive installed it should come with it. 

To generate pdf file from tex, run the following four commands in order in console (yes, should run `pdflatex` twice after `bibtex`):

    pdflatex ass1.tex
    bibtex ass1
    pdflatex ass1
    pdflatex ass1

I've created a "to_pdf.bat" file to avoid type these commands manually every time, but I'm using Mac so it's not tested. If you have any problem running it please let me know.