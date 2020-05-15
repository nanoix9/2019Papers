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

This paper conducted a two-stage location extraction system for tweets, where a location predictor followed by an extractor. In the first stage, a classification model predicts if an input text contains any location or not, where only inputs with positive predictions will be feed into next stage. In the second stage, a combined NER model from various tools extracts locations from the text filtered out by previous stage. By a variety of experiments, the author demonstrated that: 1) combining various NER tools can improve F1-score of the model; 2) the final precision of location extraction can be improved if a proper predictor is set before it.

### Location Extraction

This is the second stage in the whole pipeline but it was studied first. In this stage, a compound model is combined by some of the three NER tools: Ritter tool, the Gate NLP framework (Gate) and the Stanford NER. In addition, in some combinations the result will be post-filtered by DBPedia. To achieve this, each tool is applied to input texts to extract locations, then the individual outputs are merged as final result. To filter the locations, locations extracted from NER models are kept only if they appears in DBPedia. 

In the experiment, combined NER extractors are compared to the Ritter tool as the baseline. The results showed that combining with either Gate or Stanford NER could improve the model performance under the evaluation of F1-score. Moreover, the DBPedia post-filtering dramatically increased precision but also caused great decline in recall. The best F1-score on Ritter dataset was obtained by "Ritter tool + Stanford NER + DBPedia", and "Ritter tool + Stanford NER" for MSM2013 dataset.


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

The author found that some features are more useful than others. Though there are minor difference between performances on two datasets, most significant common features includes: Geography gazetteer, Prep+PP, PP, and Place+PP. On Ritter dataset, the best F1-score was 65% with an accuracy of 94%, achieved by RF under threshold 0.5. On MSM2013 dataset, the best F1-score was 61% along with accuracy 84%, also obtained by RF but with a different threshold 0.75. Naive Bayes is also a comparable solution which is preferred over SVM.

After that, various predictors are applied before extractor for evaluation. In this experiment, only Ritter tool was used instead of combined tools, and RF models with different thresholds were used as predictors. The result showed that the precision was significantly improved, while the recall decreased due to prediction error. Another advantage of predictor is reducing the number of tweets that are fed into extractor.

### Summary

To summarise, this work showed that 1) combining different NER tools is a reasonable way to improve the location extraction model metrics such as F1-score; 2) a preceding location predictor can benefit the precisions of final result but reduce the recall. Furthermore, from the experiment of perfect predictor conclusions can be drawn that better prediction model will mitigate the recall decline. 

### Discussion

Compared to the work of @mao2019mapping, the most important advantage of the algorithm reviewed in this section is the incorporation of location prediction stage. Although there is also a classifier in [@mao2019mapping], its goal is outage detection instead of improving the performance of NER model. By contrast, @hoang_location_2018 showed that location prediction can increase the eventual precision of NER system. Though recall was sacrificed to some extent, the drawback can be further reduced if we increase the accuracy of location predictor. Another advantage is that @hoang_location_2018 conducted a comprehensive study on features including gazetteers and POS tags, greatly enriching the features that can be used for location extraction models. On the ther hand, @mao2019mapping only used neural networks to learn all features automatically, which reduced less human efforts but also limited the model performance. Finally, @hoang_location_2018 also carried out a number of experiments on algorithm comparison and parameter optimisation, which provided strong guidelines for the design of our own algorithm.


# Proposed Approach

## Data Preparation

There are some public available datasets containing texts from social media with human annotations, including Ritter [@ritter2011named] and WNUT [@derczynski_results_2017]. In addition, more data can be gathered by Twitter's API and annotated by crowdsourcing. Moreover, as there are some existing works having already demonstrated that gazetteer features can improve neural NER models [@Li_Jing_2020; @liu_towards_2019], we will use the same gazetteers from UIUC NER system as in the experiment of [@liu_towards_2019].

## Evaluation

NER systems are usually evaluated by recall and precision [@Li_Jing_2020; @hoang_location_2018; @mao2019mapping], which are controversial in nature though. A balanced metrics taking into account both sides is called F1-score, also known as F-score or F-measure:

$$\operatorname{F1-score} = 2 \times \frac{\mathrm{Precision} \times \mathrm{Recall}}{\mathrm{Precision} + \mathrm{Recall}}$$

## Algorithm Description

Our proposed NER algorithm for locations on Twitter follows the two-stage model as studied by @hoang_location_2018, but the machine learning models in each stage will be replaced by deep learning ones which was employed by @mao2019mapping. Before and after this model, pre- and post-processing are incorporated for necessary tasks such as POS tagging and formatting. The overall process of our proposal is shown as Fig @fig:two-stage.

```{=latex}
\begin{figure}
\centering
\begin{tikzpicture}
    \tikzstyle{entity} = [rectangle, minimum width=0.8cm, minimum height=1cm, text centered, text width=1.4cm, draw=black]
    \tikzstyle{every node}=[font=\small]
    \tikzstyle{arrow} = [thick,->,>=stealth]

    % Dialectics
    \node (x) [] {\small \textbf{x}};
    \node (Pre) [entity, dotted, right of=x, xshift=0.3cm] {Pre-processing};

    %\node (x) [] {\texttt{"When I go to New York ..."}};
    %\node (P) [entity, right of=x, below of=x, xshift=0.4cm, yshift=0.5cm] {Location Prediction};

    \node (P) [entity, right of=Pre, xshift=1.2cm] {Location Prediction};
    \node (E) [entity, right of=P, xshift=1.2cm] {Location Tagging};
    \node (Post) [entity, dotted, right of=E, xshift=1.2cm] {Post-processing};
    \node (y) [right of=Post, xshift=0.3cm] {\textbf{y}};

    \draw[arrow] (x) to (Pre);
    \draw[arrow] (Pre) to (P);
    \draw[arrow] (P) to (E);
    \draw[arrow] (E) to (Post);
    \draw[arrow] (Post) to (y);
  
\end{tikzpicture}
\caption{Proposed Algorithm: Two-Stage Location Extraction} \label{fig:two-stage}
\end{figure}
```

### Pre-processing

Before input text is fed into the two-stage location extraction model, some pre-processing will be beneficial for the subsequent stages. Basically in this phase the input text will be tokenized and Part-of-Speech (POS) will be tagged, because according to some research [@hoang_location_2018] the POS tag can increase the final model performance. In addition, since tweets are highly informal texts, for example, with many spelling errors, spelling correction will also be carried out as normalisation in this phase.

### Location Prediction

The work of @hoang_location_2018 showed that a good location predictor can increase the metrics of the location extraction model. However, this work also showed that while this preceding filter increased precision, it did have negative impact on recall, which has controversial impact on the final F1-score. This is reasonable because some locations are missing because of false negative prediction. Therefore, the performance of predictor is crucial; a less efficient one would even decrease the overall performance in terms of F1-score. 

In [@hoang_location_2018] three classification model has been tested: Naive Bayes, Support Vector Machine and Random Forest. However, in a more recent study, @lee_sequential_2016 has demonstrated that deep learning models outperform traditional machine learning algorithms on classification of short texts like tweets. @lee_sequential_2016 also showed that generally CNN had a better metrics over RNN, so our location predictor will be a CNN-based text classification model, which consists of three components: embedding, CNN and full-connected(FC). First, in the embedding layer, some popular pre-trained embeddings such as GloVe or BERT will be used. In addition, since @hoang_location_2018 has showed that features including gazetteer and POS tags were significant to final results, we will include these features in our model. Specifically, a variable indicating if the word exists in gazetteer and POS tags generated from pre-processing step are concatenated into word embeddings. Second, multi layered CNN model will be followed. Finally the output of CNN will be fed into a full-connected layer for prediction. Because the result is binary, that is, whether the input contains any location or not, softmax is not necessary. Instead, a logistic activation function is sufficient.

Once a probability has been produced by prediction model, a threshold is required for decision-making. Selection of this threshold is more of a trade-off between recall and precision, and will be optimised based on the dataset and application. For example, in some application where precision is preferred over recall, we can increase the threshold for stricter filtering.

### Location Tagging

After an input tweet passes the filtering by location predictor, a sequence tagging model will be applied for entity tagging. We use the biLSTM-CRF model which has been shown outperformed Standford NER tool [@mao2019mapping; @Li_Jing_2020]. In addition, char-level embeddings is also an effective method to improve the overall performance so it will also be included in our model [@Li_Jing_2020]. 

First, the input word sequence will be fed to an embedding layer which combines both word embedding and char-level embedding. A pre-trained word embedding called GloVe was adopted by @mao2019mapping, but some other ones such as BERT are also worth trying. In addition, incorporating extra knowledge such as gazetteers and POS tags will improve the overall system performance [@Li_Jing_2020], therefore, these two features will also be appended to vector representation. Second, the combined embedding vectors are give to a bidirectional LSTM (bi-LSTM) layer. The output of bi-LSTM is transformed by a softmax module into probabilities over all tag categories. Third, the sequences of these probabilities are fed to a CRF layer for maximum likelihood estimation over entire sequence.

Following @mao2019mapping and also Stanford NER, the final tags generated by this tagging model is  encoded by standard Beginning/Inside/Outside (BIO) format.

### Post-processing

Since the output of location tagging model is a sequence of labels, the actually locations will be formed by post-processing. All B- and I- tags will be retrieved and formatted into entities. 

