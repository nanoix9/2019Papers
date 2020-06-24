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
- People 20 years old or younger
- People older than 20 
- Everyone

The remainder of this article is organised as follows. In 
\cref{related-work} related works on topic mining and evaluation will be reviewed.
The methodology of topic mining are detailed in \cref{research-design}, while 
the results, analysis and evaluations are presented in \cref{result-analysis-and-evaluation}.
The works of this article are summarised in \cref{conclusion} and open issues 
and future works are discussed in \cref{open-issues-and-future-works}.

# Literature Review
<!-- b) A literature review of same or similar tasks attempted by other researchers. -->

@jacobi_quantitative_2016 conducted an in-depth study of how to apply topic modelling 
technologies on analysis of qualitative data in academic research. 

@boyd-graber_care_nodate provides a summary of topic evaluation methods, which
are divided into three categories: human evaluation, diagnostic metrics, and
coherent metrics. The first one needs human effort so it is expensive and time-consuming

**Human Evaluation** requires human involvement in the evaluation task. One method
in this category is accomplished by word intrusion task. Specifically, a person 
will be presented by a list of words and is asked to find an intruder in the meaning
of not belonging to others. The words list are constructed by first selecting 
highly possible words from a topic, and then randomly choose one word with low
probability in the same topic but high probability in a different topic. 
If the intruders are easily to be identified, then the topic is more likely coherent.

**Diagnostic Metrics** 

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
for each person are also counted. The result is summarised by Fig. \ref{fig:data-desc},
which is created by Python packages `Pandas` and `Matplotlib`.
From this figure we can acquire some basic statistics of the dataset, including

#. Gender: data samples are quite evenly distributed over both genders. 
#. Age: most bloggers are younger than 30, almost of them under 20. 
    On the other hand, there are two gaps around 20 and 30 which may implies
    some missing data points in the dataset
#. Zodiac: The distribution over zodiac is reasonable even.
#. Category: the most frequent category is unknown, which is trivial, while
    the second frequent one is student, far more than other categories.
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
  \subfloat[Gender-Age Range\label{category}]{%
       \includegraphics[width=0.48\linewidth]{img/show-gender-age.png}}
  %\hfill
  \subfloat[Zodiac\label{zodiac}]{%
       \includegraphics[width=0.48\linewidth]{img/show-zodiac.png}}
  \\
  \subfloat[Category\label{category}]{%
       \includegraphics[width=0.48\linewidth]{img/show-category.png}}
  \subfloat[{Number of Posts}\label{num-posts}]{%
        \includegraphics[width=0.48\linewidth]{img/show-blog-count.png}}
  \caption{Data Overview. Histogram over (a) gender (b) age (c) gender and age range 
      (d) zodiac (e) category (f) number of posts}
  \label{fig:data-desc}
\end{figure}

## Topic Mining Algorithm

The general idea for mining popular topics used in this project is to find 
the most significant "things" mentioned in the overall dataset, as well as 
the closely related information.

The overall architecture of the algorithm is shown as Fig. \ref{fig:overall}, 
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
  \caption{Overall Architecture of Topic Mining Algorithm}
  \label{fig:overall}
\end{figure*}

### Data Cleaning

Before applying any text mining techniques, it is important to do basic data
cleaning to improve data quality. In this step, a few operations for preprocessing 
will be carried out based on the observations of the dataset, with details as follows. 
<!--, as detailed
in \cref{tbl:data-cleaning} -->

- **Problem**: At some place there is no whitespace between a punctuation 
    and the word following it, which causes wrong tokenisation. 
    Specifically, the punctuation might be tokenised with the following word 
    as one token.

    **Solution**: Add whitespace after a punctuation if a word immediately follows it.

    <!-- **Example**:
    
    + \makebox[1cm][l]{input:}  `I brought...stuff...like clothes`
    + \makebox[1cm][l]{output:} `I brought... stuff... like clothes` -->

- **Problem**: Two or more consecutive quote symbols may cause wrong tokenisation.

    **Solution**: Replace two or more quotes as a double quote.

    <!-- **Example**:
      + input: 
      + output:  -->

- **Problem**: The unicode quote may affect tokenisation and stopwords matching.

    **Solution**: Replace unicode quote by ASCII quote.

    <!-- **Example**:
      + input: 
      + output:  -->

- **Problem**: The unicode quote may affect tokenisation and stopwords matching.

    **Solution**: Replace unicode quote by ASCII quote.

    <!-- **Example**:
      + input: 
      + output:  -->

- **Problem**: Characters that are usually not part of normal
    English text may disturb tokenisation and POS tagging.

    **Solution**: Remove invalid characters such as "*", "#", and so on.

    <!-- **Example**:
      + input: 
      + output:  -->

- **Problem**: Sometimes people repeat a certain letter in a word for emphasis, 
    but it will result in wrong words and also increase the vocabulary size.

    **Solution**: No English word has more than two consecutive appearances of the same letter, 
    so three or more repetition of a letter is squeezed into two.

    <!-- **Example**:
      + input: 
      + output:  -->

- **Problem**: 

    **Solution**: 

    <!-- **Example**:
      + input: 
      + output:  -->



<!-- \begin{table}[ht]
\caption{My Table}
\label{tbl:data-cleaning}
\begin{center}
\small
  \begin{tabular}{|p{0.3\linewidth}|p{0.3\linewidth}|p{0.3\linewidth}|} 
  \hline
  Observation & Problem & Solution \\
  \hline
  No whitespace between a punctuation and the word following it 
  & Wrong tokenisation: the punctuation might be tokenised with the following word as one token & Add whitespace after a punctuation if a word immediately follows it \\
  \hline
\end{tabular}
\end{center}
\end{table} -->

These operations are implemented by regex matching and substitution, or simple text replacing. To use regex, the Python's `re` package are imported.

### Tokenisation

Tokenisation is usually the first step of all text mining pipelines, 
which includes sentence and word tokenisation. 
Sentence tokenisation is to split the whole text into sentences, 
while word tokenisation splits a sentence into word or tokens. 
In this project we use `nltk` package to do such task. This package
provides two functions `sent_tokenize()` and `word_tokenize()` 
for both tokenisation. A document is first tokenised into sentences,
and then each sentence is tokenised into words. Finally, a document
is represented as list of lists, as each sentence is a list of words.

### POS Tagging

Part-Of-Speech (POS) tagging is the second step following tokenisation. In this step,
each word is assigned by a POS tag. `nltk` provides a handy function `pos_tag()`
to do this task. This function works on sentence level, and maps each word
into a tuple which is the pair of word and POS tag.

### Entity Extraction

In this project, a topic is defined as a "thing" or "object". Therefore, 
in order to find the topics, we need to find all "things" or "objects" first.
There are a few options to do this task, among which two methods will be 
employed by this project: Named Entity Recognition (NER) and parsing.

#### NER

Named entities are ideal candidates of topics as they denote real-world objects.
`nltk` provides a function `ne_chunk()` to extract entities from sentences.
The input of the function should be a list of tokens with POS tags, which 
is another reason why POS tagging should be done in previous step. The return
value of this function is a list of chunks, each of which is basically a list 
and may contain a `label` attribute if it is a recognised entity. 
The entity type can be acquired by `label()` 
and the entity itself should be acquired by joining all the elements of the
chunk. 

#### Parsing

Another way to extract objects is parsing by pre-defined patterns. For example,
it is reasonable to treat definite nouns as objects according to the grammar. 

### Stopwords Removal

Stopwords are most common words which carries no significant meanings. 
Removing stopwords can reduce the size of data to be proceeded as well as
increase the result accuracy. `nltk` provides an out-of-the-box stopwords collection, but the experiment shows that some common words carrying no
meaning are not included in the list. In order to expand the stopword list,
more words are collected from website [^stopwords].

[^stopwords]: <https://gist.github.com/sebleier/554280>

Stopwords removal is conducted after POS tagging and entity extraction 
because these two steps are sequence model, which means their performance
rely on word order. If stopwords are removed before them, we will get 
sentences which do not comply with English grammar. In addition,
stopwords removal are carried out on tagged documents as well as
entities extracted. Theoretically, stopwords cannot be entity, but errors
will happen in any POS tagging and NER model. Therefore, trying to remove 
stopwords can reduce the error introduced in previous steps.

### Stemming and Lemmatisation

Stemming and lemmatisation are both techniques for text normalisation,
that is, convert an inflected word into its root form. However, stemming
and lemmatisation work in different way. Stemming removes suffix or prefix
from a word, returning a word stem which is not necessarily a word. 
On the other hand, lemmatisation always looks for the lemma from word variations
with morphological analysis. For example, stemming against the third-person
singular form "flies" returns "fli", while lemmatisation returns "fly". 
In this project, these two methods are combined together to reach the maximum
extent of word normalisation. 

`nltk` provides various stemming algorithms such as `PorterStemmer` and 
`LancasterStemmer`, and one lemmatisation algorithm `WordNetLemmatizer`.
In the code we use `WordNetLemmatizer` followed by `PorterStemmer`.

### Word Count and TF-IDF

After all "objects" have been extracted and normalised, the next step is to 
find most popular ones as the most dominant topics. Popularity can be defined
in various ways, and in this project two approaches are used: word count and 
Term Frequency-Inverse Document Frequency (TF-IDF). In the first method, 
we simply count the appearances of each entity
and get the most two frequent ones. In the second method, we calculate 
the TF-IDF value of each entity word, following the definition 

\begin{align*}
\mathrm{TF{\text -}IDF}(t_i, d_j) &= 
\mathrm{TF}(t_i, d_j) \times \mathrm{IDF}(t_i) \\
& = \mathrm{TF}(t_i, d_j) \log \frac{N}{\mathrm{DF}(t_i)}
\end{align*}

$\mathrm{TF}(t_i, d_j)$ is the Term Frequency of term $t_i$ in document $d_j$,
which is computed by count of $t_i$ in $d_j$ divided by the total number of terms
in $d_j$. $\mathrm{DF}(t_i)$ is the Document Frequency, which is the number of
documents that contains $t_i$. As we can see here, TF-IDF is a term-document-wise
number so a term has different TF-IDF values in different documents. In order to
rank all terms over the whole dataset, TF-IDF values of a term are averaged over
all documents as the score of that term.

$$\mathrm{score}(t_i)=\underset{d_j}{\mathrm{avg}}\ \mathrm{TF{\text -}IDF}(t_i, d_j)$$

Two different methods might return different results, which will be compared
and analysed in \cref{result-analysis-and-evaluation}.

## Evaluation Method

Evaluation of topics is challenging due to its nature of unsupervised learning.
Among existing metrics, xx is chosen to evaluate the result of the methodology.

# Result, Analysis, and Evaluation
<!-- d) How you ensured the accuracy of your results. -->
<!-- Analysis and Evaluation 20 -->

This section will show the results generated from the methodology described above,
and provides evaluation and discussion of how good the topics are. Due to
the large volume of the original dataset, the experiments
were conducted with 5,000 and 10,000 documents randomly sampled out of the total
19,320 ones, and the results demonstrated consistency. Therefore, in the following
part of this section, only results from 10,000 samples are presented.

## Result

The results are displayed as word cloud generated by `wordcloud` package. 
Fig. \ref{fig:wc-tf} shows the topics mined
by word count while Fig. \ref{fig:wc-tfidf} shows that by TF-IDF.

\begin{figure}[htbp]
  \centering
  \subfloat[Male\label{wc-tf-male}]{%
        \centering
       \includegraphics[width=0.45\linewidth]{img/male-tf-1.png}
       \hfill
       \includegraphics[width=0.45\linewidth]{img/male-tf-2.png}}
  \\[0.15cm]
  \subfloat[Female\label{wc-tf-female}]{%
        \centering
        \includegraphics[width=0.45\linewidth]{img/female-tf-1.png}
        \hfill
        \includegraphics[width=0.45\linewidth]{img/female-tf-2.png}}
  \\[0.15cm]
  \subfloat[20 or younger\label{wc-tf-less}]{%
        \centering
        \includegraphics[width=0.45\linewidth]{img/less_or_20-tf-1.png}
        \hfill
        \includegraphics[width=0.45\linewidth]{img/less_or_20-tf-2.png}}
  \\[0.15cm]
  \subfloat[Over 20\label{wc-tf-over}]{%
        \centering
        \includegraphics[width=0.45\linewidth]{img/over_20-tf-1.png}
        \hfill
        \includegraphics[width=0.45\linewidth]{img/over_20-tf-2.png}}
  \\[0.15cm]
  \subfloat[Everyone\label{wc-tf-all}]{%
        \centering
        \includegraphics[width=0.45\linewidth]{img/all-tf-1.png}
        \hfill
        \includegraphics[width=0.45\linewidth]{img/all-tf-2.png}}
  \\[0.15cm]
  \caption{Topics mined by word count. (a) male (b) female (c) 20 or younger (d) over 20 (e) everyone}
  \label{fig:wc-tf}
\end{figure}


\begin{figure}[htbp]
  \centering
  \subfloat[Male\label{wc-tfidf-male}]{%
        \centering
       \includegraphics[width=0.45\linewidth]{img/male-tfidf-1.png}
       \hfill
       \includegraphics[width=0.45\linewidth]{img/male-tfidf-2.png}}
  \\[0.15cm]
  \subfloat[Female\label{wc-tfidf-female}]{%
        \centering
        \includegraphics[width=0.45\linewidth]{img/female-tfidf-1.png}
        \hfill
        \includegraphics[width=0.45\linewidth]{img/female-tfidf-2.png}}
  \\[0.15cm]
  \subfloat[20 or younger\label{wc-tfidf-less}]{%
        \centering
        \includegraphics[width=0.45\linewidth]{img/less_or_20-tfidf-1.png}
        \hfill
        \includegraphics[width=0.45\linewidth]{img/less_or_20-tfidf-2.png}}
  \\[0.15cm]
  \subfloat[Over 20\label{wc-tfidf-over}]{%
        \centering
        \includegraphics[width=0.45\linewidth]{img/over_20-tfidf-1.png}
        \hfill
        \includegraphics[width=0.45\linewidth]{img/over_20-tfidf-2.png}}
  \\[0.15cm]
  \subfloat[Everyone\label{wc-tfidf-all}]{%
        \centering
        \includegraphics[width=0.45\linewidth]{img/all-tfidf-1.png}
        \hfill
        \includegraphics[width=0.45\linewidth]{img/all-tfidf-2.png}}
  \\[0.15cm]
  \caption{Topics mined by TF-IDF. (a) male (b) female (c) 20 or younger (d) over 20 (e) everyone}
  \label{fig:wc-tfidf}
\end{figure}

## Analysis

## Evaluation



# Conclusion
<!-- e) The conclusion and how you would do the task differently if you were to do it
again. -->
<!-- Conclusion, formatting and references 10 -->

This project has designed and implemented a complete solution
to mine most popular topics from blogs. A variety of text mining technologies
are employed and combined together to reach the goal. The results are compared
and evaluated. Further and in-depth discussion is also provided.

# Open Issues and Future Works

There are still a few open issues remaining in the solution which can be improved
by future work or changed if re-do this project.


<!-- Implementation (code) submitted as appendix 15  -->

fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 
gdwgd
fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 
fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 

fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 
fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 

fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 

fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 

fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 

fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 

fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 
fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 
fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 
fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 
fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 
fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 
fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 


fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 


fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 
fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 

fake wtdwt dwt  wd twdt  w d dw w wdt wd tw dtdw wd dwt d tagfdygafdgkdwlrn 