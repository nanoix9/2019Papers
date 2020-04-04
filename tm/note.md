
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