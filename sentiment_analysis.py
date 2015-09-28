import re, math, collections, itertools
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier

def features(words):
	return dict([(word, True) for word in words])

pos = []
neg = []
pos_file = open('ffxiv_pos.txt', 'r', encoding='utf-8')
neg_file = open('ffxiv_neg.txt', 'r', encoding='utf-8')
pos_comments = re.split(r'\n', pos_file.read())
neg_comments = re.split(r'\n', neg_file.read())

for comment in pos_comments:
	pos_words = re.findall(r"[\w']+|[.,!?;*]", comment.rstrip())
	pos_words = [features(pos_words), 'pos']
	pos.append(pos_words)

for comment in neg_comments:
	neg_words = re.findall(r"[\w']+|[.,!?;*]", comment.rstrip())
	neg_words = [features(neg_words), 'neg']
	neg.append(neg_words)

poscutoff = int(len(pos) * 3/4)
negcutoff = int(len(neg) * 3/4)

trainfeats = neg[:negcutoff] + pos[:poscutoff]
testfeats = neg[negcutoff:] + pos[poscutoff:]

classifier = NaiveBayesClassifier.train(trainfeats)

accuracy = nltk.classify.util.accuracy(classifier, testfeats)

# currently 47% with 1000 comments
# print(accuracy) 

# most informative features are currently not very informative due to low sample length
classifier.show_most_informative_features()

# TODO:
## more comments
## once accuracy hits ~75%, look into precision and recall
## include bigrams