
import sys
import pickle as pkl
import nltk
from nltk.corpus import brown
from nltk.tag import tnt, perceptron, CRFTagger
from sklearn.model_selection import train_test_split
from sklearn import metrics

def split_data():
    # load Brown corpus and split by 80/20 as training/testing set 
    sents = brown.tagged_sents(categories='news')
    # sents = brown.tagged_sents()
    # print(sents[:2])
    print(f'number of sentences: {len(sents)}')

    train_sents, test_sents = train_test_split(sents, test_size=0.2)
    print(f'training/testing split: {len(train_sents)}/{len(test_sents)}')

    # print(train_sents[:2])
    # print(test_sents[:2])
    save_pkl(train_sents, 'train_sents')
    save_pkl(test_sents, 'test_sents')

def train_taggers():
    train_sents = load_pkl('train_sents')

    # instantiate taggers
    unigram_tagger = nltk.UnigramTagger(train_sents)
    tnt_tagger = tnt.TnT()
    perceptron_tagger = perceptron.PerceptronTagger(load=False)
    # limit the number of iteractions as the training takes too long
    crf_tagger = CRFTagger(training_opt={'max_iterations': 100})

    print('Unigram tagger has already been trained')
    save_pkl(unigram_tagger, 'unigram-tagger')

    print('training TnT tagger ...', end='', flush=True)
    tnt_tagger.train(train_sents)
    print('Done')
    save_pkl(tnt_tagger, 'tnt-tagger')

    print('training Perceptron tagger ...', end='', flush=True)
    perceptron_tagger.train(train_sents)
    print('Done')
    save_pkl(perceptron_tagger, 'perceptron-tagger')

    print('training CRF tagger ...', end='', flush=True)
    crf_tagger.train(train_sents, 'crf-tagger.model')
    print('Done')
    # save_pkl(crf_tagger, 'crf-tagger')  # CRF tagger cannot be saved as pickle. use model file instead

# #Store it.
def save_pkl(obj, name):
    print(f'save to file {name}.pkl')
    output = open(name + '.pkl', 'wb')
    pkl.dump(obj, output, -1)
    output.close()

# #Retrieve it from a file
def load_pkl(name):
    print(f'load from file {name}.pkl')
    input = open(name + '.pkl', 'rb')
    obj = pkl.load(input)
    input.close()
    return obj

def test_taggers():
    # load taggers
    unigram_tagger = load_pkl('unigram-tagger')
    tnt_tagger = load_pkl('tnt-tagger')
    perceptron_tagger = load_pkl('perceptron-tagger')
    # crf_tagger = load_pkl('crf-tagger')
    crf_tagger = CRFTagger()
    crf_tagger.set_model_file('crf-tagger.model')

    test_sents = load_pkl('test_sents')[:10]
    print(f'{len(test_sents)} sentences in testing set')

    taggers = [
        ['Unigram tagger', unigram_tagger, 0, 0],
        ['TnT tagger', tnt_tagger, 0, 0],
        ['Perceptron tagger', perceptron_tagger, 0, 0],
        ['CRF tagger', crf_tagger, 0, 0],
    ]

    for t in taggers:
        print(f'evaluating {t[0]} ... ', end='', flush=True)
        f1 = t[1].evaluate(test_sents)
        t[2] = f1
        # the evaluation result is the same as f1 score calculated by sklearn
        # f1 = cal_f1_score(t[1], test_sents)
        # t[3] = f1
        # f1 = 0
        print(f'done. f1 score: {f1}')

    best_tagger_info = max(taggers, key=lambda t: t[2])
    print('best tagger is ' + best_tagger_info[0])
    best_tagger = best_tagger_info[1]

def cal_f1_score(tagger, test_sents):
    pred_sents = tagger.tag_sents([[token for token,tag in sent] for sent in test_sents])
    gold = [str(tag) for s in test_sents for token,tag in s]
    pred = [str(tag) for s in pred_sents for token,tag in s]
    # print(metrics.classification_report(gold, pred))
    f1 = metrics.f1_score(gold, pred, average='micro')
    return f1

def load_txt(filename):
    f = open(filename)
    txt = f.read()
    f.close()
    return txt

def analyse_text():
    # Perceptron tagger is the best one, but CRF tagger needs too long
    # to train on the overall corpus so this is not a fair comparison. 
    # However, since it's hard to train CRF tagger completely, I had to 
    # pick perceptron tagger.
    tagger = load_pkl('perceptron-tagger')

    tagged_words_all = []
    for i in range(1, 11):
        text = load_txt(f'news{i}.txt')
        sents = nltk.sent_tokenize(text)
        words = [nltk.word_tokenize(s) for s in sents]
        tagged_words = tagger.tag_sents(words)
        # print(tagged_words[:5])
        tagged_words_all.append(tagged_words)

    nouns_all = []
    for txt in tagged_words_all:
        for sent in txt:
            # if any('“' == w for w, p in sent):
            #     print(sent)
            nouns = list(t.lower() for t, p in sent if p in ('NN', 'NNS', 'NP', 'NPS'))
            nouns_all.extend(nouns)
    # print(nouns_all)
    noun_fd = nltk.FreqDist(n for n in nouns_all)
    total_appear = len(nouns_all)
    print(f'total nouns: {len(noun_fd)}, appearance: {total_appear}')
    print('top 50 nouns:')
    for w, c in noun_fd.most_common(50):
        print(f'{w}\t{c}\t{c/total_appear*100:.2f}%')
    

if len(sys.argv) <= 1:
    split_data()
    train_taggers()
    test_taggers()
elif sys.argv[1] == 'split':
    split_data()
elif sys.argv[1] == 'train':
    train_taggers()
elif sys.argv[1] == 'test':
    test_taggers()
elif sys.argv[1] == 'ana':
    analyse_text()

# f1 scores of taggers:
# Unigram tagger:      0.9257950530035336
# TnT tagger:          0.9681978798586572
# Perceptron tagger:   0.9858657243816255
# CRF tagger:          0.9646643109540636

# Top 50 common words:
# covid-19	32	2.61%
# coronavirus	32	2.61%
# cases	27	2.20%
# people	27	2.20%
# health	16	1.31%
# news	15	1.22%
# bloomfield	14	1.14%
# number	13	1.06%
# source	13	1.06%
# “	12	0.98%
# $	11	0.90%
# māori	10	0.82%
# banks	10	0.82%
# customers	10	0.82%
# virus	9	0.73%
# closures	9	0.73%
# dr	8	0.65%
# contact	8	0.65%
# community	8	0.65%
# care	8	0.65%
# country	7	0.57%
# auckland	7	0.57%
# travel	7	0.57%
# patients	7	0.57%
# day	7	0.57%
# deaths	7	0.57%
# school	7	0.57%
# time	7	0.57%
# hendy	7	0.57%
# government	7	0.57%
# statement	6	0.49%
# tests	6	0.49%
# system	6	0.49%
# world	6	0.49%
# controls	6	0.49%
# aut	6	0.49%
# students	6	0.49%
# q+a	6	0.49%
# kiwibank	6	0.49%
# things	6	0.49%
# risk	5	0.41%
# transmission	5	0.41%
# information	5	0.41%
# mar	5	0.41%
# disease	5	0.41%
# –	5	0.41%
# staff	5	0.41%
# ’	5	0.41%
# numbers	5	0.41%
# outbreak	5	0.41%