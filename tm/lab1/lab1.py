import sys
import nltk

# 1.	Type the following sample starter code and run it to get started.
grammar = "NP: {<DT>?<JJ>*<NN>}"
dcp = nltk.RegexpParser(grammar)

def parse_sent(sent, cp=dcp):
    taggedS = nltk.pos_tag(nltk.word_tokenize(sent))
    # print(taggedS)
    result = cp.parse(taggedS)
    return result

def ques1():
    sent = "I saw a boy in the park with a telescope."
    result = parse_sent(sent)
    print(result)
    result.draw()

# 2.	Interpret the output to determine which of the two interpretations 
# the parser parses the sentence.

# 3.	Try and rewrite the sentence in a different way to get the other 
# interpretation without changing the overall meaning.

def ques3():
    sent = "In the park I spotted a boy carrying a telescope."
    result = parse_sent(sent)
    print(result)
    result.draw()

# 4.	Try other sentences and interpret the output and see if the parser output is correct.

def ques4():
    sent = 'The quick brown fox jumps over the lazy dog'
    result = parse_sent(sent)
    print(result)
    result.draw()

# 5.	Download a news article from NZ Herald or another site and read in 
# the article as a text file.

def load_txt(filename):
    with open(filename) as f:
        return [line for line in f.readlines() if line.strip()]

# 6.	Parse all the sentences in the text file.

def parse_all(sents, cp):
    return [parse_sent(sent, cp) for sent in sents]

# 7.	Extract all the definite nouns in the text. (definite nouns are nouns 
# followed by the determiner “the”). 

def get_def_nouns(pt):
    # print('-' * 30)
    # print(type(pt), pt)
    # exit(0)
    # print(pt[0])
    # print(type(pt[0][0]))
    # print(repr(pt[0][1]))
    # print(dir(pt[0]))
    # idx = filter(lambda i: pt[i-1])
    ret = []
    for i in range(1, len(pt)):
        # print(type(pt[i]))
        # print(repr(pt[i]))
        # if isinstance(pt[i-1], tuple) and isinstance(pt[i], tuple) \
        #         and pt[i-1][0].lower() == 'the' and pt[i-1][1] == 'DT' \
        #         and pt[i][1] == 'NN':
        #     ret.append(pt[i])
        # el
        if isinstance(pt[i], nltk.tree.Tree) and pt[i].label() == 'NP':
            # ret.append(pt[i][0] + pt[i][-1])
            ret.append(pt[i][-1])
        # print('ret', ret)
    # print('------------- ret ---------------')
    return ret

def get_all_def_nouns(fname):
    grammar = "NP: {<DT><JJ>*<NN|NNS|NNP|NNPS>}"
    cp = nltk.RegexpParser(grammar)

    pts = parse_all(load_txt(fname), cp)
    # print(get_def_nouns(pts[29]))
    ret = []
    for pt in pts:
        ret.extend(get_def_nouns(pt))
        # print(ret)
        # break
    return ret

def ques7():
    ret = get_all_def_nouns('article.txt')
    dn = sorted(set(w for w, pos in ret))
    print('all definite nouns:', dn)

# 8.	Count the definite nouns and output them in a sorted ascending order.

def ques8():
    ret = get_all_def_nouns('article.txt')
    dnc = nltk.FreqDist(ret)
    print(dnc.most_common()[::-1])

# 9.	Upload your python code file to Blackboard by 6pm Friday this week. 

def run(i):
    key = 'ques' + str(i)
    if key in globals():
        print('running: ' + key)
        globals()[key]()

if len(sys.argv) <= 1:
    for i in range(8):
        run(i)
else:
    run(int(sys.argv[1]))