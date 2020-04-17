#!/bin/bash

tex=pdflatex
bib=bibtex
file=ass1

$tex ${file}.tex
$bib ${file}
$tex ${file}
$tex ${file}
