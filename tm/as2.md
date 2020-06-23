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

People's concerns and opinions are important reference for innovations of
 new products or services. However, accomplishing such task by humans is
expensive, time-consuming and difficult to scale. As a response, 
a number of individuals and organisations are leveraging text mining technologies 
to mining meaningful information from large volume of text such as news media 
[@jacobi_quantitative_2016].
Among a variety of studies and applications, topic modelling is an important
method to extract hot topics which reflects public attention and opinion 
from massive texts [@jacobi_quantitative_2016; @waila_blog_2013; @guo_mining_2012]. 
However, effective method of extracting useful information from text on the Internet 
remains an open challenge [@guo_mining_2012]. 

Evaluation of topics mined from text is another challenge, mostly due to the 
lack of ground truth because topic modelling is an unsupervised learning task
[@boyd-graber_care_nodate]. 

<!-- ## Objective -->

<!-- 
your boss wants to know the two most popular topics that the bloggers 
have been talking about in the following demographics :
a) Males
b) Females
c) Age brackets <=20 and over 20. 
d) Everyone -->

The goal of this project is to mine most popular topics that people were discussing 
from blog posts by utilising various text mining algorithms and tools. 
Specifically, we will find two most popular topics for each group in the following demographics:

- Males
- Females
- People younger than or equal to 20 years old
- People older than 20 years old
- Everyone

The remainder of this article is organised as follows. In 
\cref{related-work} related works on topic mining and evaluation will be reviewed.
The methodology of topic mining are detailed in \cref{research-design}, while 
the results, analysis and evaluations are presented in \cref{results-analysis-and-evaluation}.
The works of this article are summarised in \cref{conclusion} and open issues 
and future works are discussed in \cref{open-issues-and-future-works}.

# Related Work
<!-- b) A literature review of same or similar tasks attempted by other researchers. -->

@jacobi_quantitative_2016 conducted an in-depth study of how to apply topic modelling 
technologies on analysis of qualitative data in academic research. 

# Research Design
<!-- c) The details of your strategy to solve the problem. In this part you should
describe the details of how you processed the data from start to finish 
including the details of how the data got processed in any external library 
you have used (if you have used it). -->
<!-- Data description and analysis 15
Research Design 30 -->

In this section the solution will be described in detail. First an overview
of the dataset is given, and then the algorithm of topic mining is detailed.

## Data Description

The dataset contains 19,320 files in XML format, each containing articles
of one person posted generally between 2001 and 2004. Metadata of the bloggers
includes gender, age, category, and zodiac. In addition, the number of posts 
for each person are also counted. The result is summarised in \cref{fig:data-desc}.
From this figure we can acquire some basic statistics of the dataset, including

#. Gender: data samples are quite evenly distributed over both genders. 
#. Age: most bloggers are younger than 30, almost of them under 20. 
    On the other hand, there are two gaps around 20 and 30 which may implies
    some missing data points in the dataset
#. Category: the most frequent category is unknown, which is trivial, while
    the second frequent one is student, far more than other categories.
#. Zodiac: The distribution over zodiac is reasonable even.
#. Number of posts: most bloggers published less than 100 posts, while the peak
    appears at 10, which implies people are most likely to write around 10 posts.

\begin{figure}[htbp]
  \centering
  \subfloat[Gender\label{gender}]{%
       \includegraphics[width=0.48\linewidth]{img/show-gender.png}}
  %\hfill
  \subfloat[Age\label{age}]{%
        \includegraphics[width=0.48\linewidth]{img/show-age.png}}
  \\
  \subfloat[Category\label{category}]{%
       \includegraphics[width=0.96\linewidth]{img/show-category.png}}
  \\
  \subfloat[Zodiac\label{zodiac}]{%
       \includegraphics[width=0.48\linewidth]{img/show-zodiac.png}}
  %\hfill
  \subfloat[{Number of Posts}\label{num-posts}]{%
        \includegraphics[width=0.48\linewidth]{img/show-blog-count.png}}
  \caption{Data Overview. Histogram over (a) gender (b) age (c) category
          (d) zodiac (c) number of posts}
  \label{fig:data-desc}
\end{figure}

## Topic Mining Algorithm

The general idea for mining popular topics used in this project is to find 
the most significant "things" mentioned in the overall dataset, as well as 
the closely related information.

The overall architecture of the algorithm is shown as \cref{fig:overall}, 
and the details of each step are described in the following subsections.

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

Before applying any text mining techniques, it is important to do basic data
cleaning to improve data quality. In this step, a few operations for preprocessing 
will be carried out based on the observations of the dataset, as detailed
in \cref{tbl:data-cleaning}

Table: (table title) \label{tbl:data-cleaning}

| Observation | Problem       | Solution 
|:----------- |:--------------|:-----------
| No whitespace between a punctuation and the word following it | Wrong tokenisation: the punctuation might be tokenised with the following word as one token | Add whitespace after a punctuation if a word immediately follows it


### Tokenization

### POS Tagging

### NER

### Stopwords Removal

### Stemming and Lemmatization

### Counting and TF-IDF

# Results, Analysis, and Evaluation
<!-- d) How you ensured the accuracy of your results. -->
<!-- Analysis and Evaluation 20 -->

# Conclusion
<!-- e) The conclusion and how you would do the task differently if you were to do it
again. -->
<!-- Conclusion, formatting and references 10 -->

# Open Issues and Future Works



<!-- Implementation (code) submitted as appendix 15  -->