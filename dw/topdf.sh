#!/bin/bash

file=ass1

if [[ x"$1" == x"clean" ]]; then
    rm *.aux *.dvi *.fdb_latexmk *.fls *.log *.synctex.gz *.bbl *.blg
    exit 0
fi

latex $file
bibtex $file
latex $file
latex $file
dvipdfm $file.dvi
