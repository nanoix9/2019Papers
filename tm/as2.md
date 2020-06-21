---
title: Popular Topic Mining from Blogs
subtitle: xxx
author: 
    - name: "Stone Fang (Student ID: 19049045)"
      dept: Computers and Information Sciences
      org: Auckland University of Technology
      loc: Auckland, New Zealand
      email: fnk7060@autuni.ac.nz
footer: "Stone Fang (19049045)"
bibliography: [as2.bib]

graphics: true

appendix: appendix.tex
appendix-title: Source Code in Python

header-includes:
    - \usepackage[noabbrev]{cleveref}

---

# Overview
<!-- The task you set out to solve. -->
<!-- Research question and rationale description 10 -->

## Objective

<!-- 
your boss wants to know the two most popular topics that the bloggers 
have been talking about in the following demographics :
a) Males
b) Females
c) Age brackets <=20 and over 20. 
d) Everyone -->

# Related Work
<!-- b) A literature review of same or similar tasks attempted by other researchers. -->

# Research Design
<!-- c) The details of your strategy to solve the problem. In this part you should
describe the details of how you processed the data from start to finish 
including the details of how the data got processed in any external library 
you have used (if you have used it). -->
<!-- Data description and analysis 15
Research Design 30 -->

## Data Description

The dataset contains 19,320 files in XML format, each containing articles
 of one person posted generally between 2001 and 2004. 

## Topic Mining Algorithm

The general idea for mining popular topics used in this project is to find 
the most significant "things" mentioned in the overall dataset, as well as 
the closely related information.

The overall architecture of the algorithm is shown as \cref{fig:overall}.

\begin{figure*}[htbp]
  \centering
  % \sffamily
  {
  %\fontfamily{phv}\selectfont
  \fontsize{9}{10}\selectfont
  % \fontsize{7}{7}\selectfont
  \def\svgwidth{0.98\textwidth}
  %  \resizebox{0.9\textwidth}{!}{\input{as2-algo.pdf_tex}}
    \input{as2-algo.pdf_tex}
  }
  \caption{Algorithm}
  \label{fig:overall}
\end{figure*}

### Data Cleaning

### Tokenization

### POS Tagging

### NER

### Stopwords Removal

### Stemming and Lemmatization

### Counting and TF-IDF

# Results, Analysis, Evaluation, and Accuracy Insurance
<!-- d) How you ensured the accuracy of your results. -->
<!-- Analysis and Evaluation 20 -->

# Conclusion, Open Issues and Future Work
<!-- e) The conclusion and how you would do the task differently if you were to do it
again. -->
<!-- Conclusion, formatting and references 10 -->





<!-- Implementation (code) submitted as appendix 15  -->