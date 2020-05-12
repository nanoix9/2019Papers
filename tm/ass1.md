---
title: Location NER from Tweets
subtitle: xxx
author: 
    - name: "Stone Fang (Student ID: 19049045)"
      dept: Computers and Information Sciences
      org: Auckland University of Technology
      loc: Auckland, New Zealand
      email: fnk7060@autuni.ac.nz
footer: "Stone Fang (19049045)"
bibliography: [ass1.bib]

---

# Metrics

- exact match: both entity type and boundaries are matched
- relaxed match

# Algorithms

## Knowledge/Rule-based

hand-crafted rules. rely on lexicon resources and domain specific knowledge.

pros:
do not require annotated training data
high precision

cons: 
need domain experts construct and maintain the knowledge resources
low recall


## Unsupervised and bootstrapped systems

earliest systems,

pros:
required very minimal training data.

## Feature-engineered supervised learning

learn models from data, but need manual feature engineering

common approaches:

- Hidden Markov Models (HMM)
- Support Vector Machines (SVM)
- Conditional Random Fields (CRF)
- decision trees

## Feature-inferring neural networks

features are also learned from data, e.g. embeddings

### Representation(Embedding)

- Word level Architecture

- Character level Architecture

- Character+Word level architectures

- Character + Word + affix model

### Context encoder

- CNN
- RNN -> LSTM -> bi-LSTM -> window bi-LSTM
- Recursive neural networks
- Neural Language Models
- Attention -> Transformer -> BERT/GPT/ELMo

### Tag decoder

- Multi-Layer Perceptron + Softmax
- Conditional Random Fields
- RNN
- Pointer Networks


# Algorithm analysis

## choosed algorithms

This paper conducted a two-stage location extraction system for tweets, where a location predictor followed by an extractor. In the first stage, a classification model predicts if an input text contains any location or not, where only inputs with positive predictions will be feed into next stage. In the second stage, a combined NER model from various tools extracts locations from the text filtered out by previous stage. By a variety of experiments, the author demonstrated that: 1) combining various NER tools can improve F-score of the model; 2) the final precision of location extraction can be improved if a proper predictor is set before it.

### Location Extraction

This is the second stage in the whole pipeline but it was studied first. In this stage, a compound model is combined by some of the three NER tools: Ritter tool, the Gate NLP framework (Gate) and the Stanford NER. In addition, in some combinations the result will be post-filtered by DBPedia. To achieve this, each tool is applied to input texts to extract locations, then the individual outputs are merged as final result. To filter the locations, locations extracted from NER models are kept only if they appears in DBPedia. 

In the experiment, combined NER extractors are compared to the Ritter tool as the baseline. The results showed that combining with either Gate or Stanford NER could improve the model performance under the evaluation of F-score. Moreover, the DBPedia post-filtering dramatically increased precision but also caused great decline in recall. The best F-score on Ritter dataset was obtained by "Ritter tool + Stanford NER + DBPedia", and "Ritter tool + Stanford NER" for MSM2013 dataset.


### Location Prediction

In location prediction stage, the author first showed the usefulness of prior predictors by passing tweets through a perfect (that is, 100% correct results) location predictor before feeding into extractor, where the precision were significantly improved with the recall unchanged. Though perfect prediction models are impossible in real-world applications, this is a reasonable proof-of-concept. Then several features were defined for predictive models, including:

- **Geography gazetteer**: if any word is included by a geography gazetteer (Gate was chosen in the experiment)
- **Prep**: if input text contains any of the 7 prepositions regarding to place (*at, in, on, from, to, toward, towards*)
- **Prep + PP**: if input text contains a preposition directly followed by a proper noun (PP)
- **Place + PP**: if any word of place (*town, city, state, region, department, country*) appears directly after or before a proper noun
- **Time**: if any word regarding to time exists, including *today, tomorrow, weekend, tonight*, as well as all the names of months and the days of a week
- **DefArt + PP**: if any proper noun appears after the definitive article "the"
- **Htah**: if the tweet contains any hash tag
- **PP, Adj, Verb**: the counts of proper nouns, adjectives and verbs in the text

After features generated, three machine learning algorithms are trained on Ritter and MSM2013 datasets with 10-folds cross validation, namely Naive Baiyes (NB), Support Vector Machine (SVM) and Random Forest (RF). Experiments under various parameters have been carried out.

The author found that some features are more useful than others. Though there are minor difference between performances on two datasets, most significant common features includes: Geography gazetteer, Prep+PP, PP, and Place+PP. On Ritter dataset, the best F-score was 65% with an accuracy of 94%, achieved by RF under threshold 0.5. On MSM2013 dataset, the best F-score was 61% along with accuracy 84%, also obtained by RF but with a different threshold 0.75. Naive Bayes is also a comparable solution which is preferred over SVM.

After that, various predictors are applied before extractor for evaluation. In this experiment, only Ritter tool was used instead of combined tools, and RF models with different thresholds were used as predictors. The result showed that the precision was significantly improved, while the recall decreased due to prediction error. Another advantage of predictor is reducing the number of tweets that are fed into extractor.

### Summary

To summarise, this work showed that 1) combining different NER tools is a reasonable way to improve the location extraction model metrics such as F-score; 2) a preceding location predictor can benefit the precisions of final result but reduce the recall. Furthermore, from the experiment of perfect predictor conclusions can be drawn that better prediction model will mitigate the recall decline. 


# Proposed Approach

## Algorithm Description

Our proposed NER algorithm for locations on Twitter follows the two-stage model as studied by @hoang_location_2018, but the machine learning models in each stage will be replaced by deep learning ones which was employed by @mao2019mapping. The overall process of our proposal is shown as Fig @fig:two-stage.

```{=latex}
\begin{figure}
\centering
\begin{tikzpicture}
    \tikzstyle{entity} = [rectangle, minimum width=1cm, minimum height=1cm, text centered, text width=1.5cm, draw=black]
    \tikzstyle{every node}=[font=\small]
    \tikzstyle{arrow} = [thick,->,>=stealth]

    % Dialectics
    \node (x) [] {\small \textbf{x}};
    \node (P) [entity, right of=x, xshift=0.4cm] {Location Prediction};
    \node (E) [entity, right of=P, xshift=1.5cm] {Location Tagging};
    \node (Post) [entity, right of=E, xshift=1.5cm] {Post Processing};
    \node (y) [right of=Post, xshift=0.4cm] {\textbf{y}};

    \draw[arrow] (x) to (P);
    \draw[arrow] (P) to (E);
    \draw[arrow] (E) to (Post);
    \draw[arrow] (Post) to (y);
  
\end{tikzpicture}
\caption{Proposed Algorithm: Two-Stage Location Extraction} \label{fig:two-stage}
\end{figure}
```

### Location Prediction

### Location Tagging

### Post-processing

