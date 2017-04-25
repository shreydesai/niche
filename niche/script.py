import os
import nltk
import math
import random
import itertools
import collections

from nltk.corpus import brown
from nltk.classify import accuracy
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import NuSVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORIES = ['entertainment', 'sports', 'fun', 'games',
              'weather', 'science', 'technology', 'politics']
FEATURES = 2500

def fileids(category):
    """Get file IDs of tweets for specified category"""
    path = os.path.join(PARENT, 'corpus', 'processed', category)
    return os.listdir(path)

def sents(file):
    """Get list of sentences from a document"""
    f = open(file, 'r', encoding='ISO-8859-1').read().strip()
    return [sent.strip() for sent in f.split('\n')]

def words(file):
    """Get list of words from a document"""
    f = open(file, 'r', encoding='ISO-8859-1').read().strip()
    sents = [sent.split(' ') for sent in f.split('\n')]
    words = [word for sent in sents for word in sent if len(word) > 0]
    return words

def features(document, word_features):
    """Builds unigram features from document"""
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

def bigram_features(document):
    """Builds bigram features from document"""
    #bigram_finder = BigramCollocationFinder.from_words(words)
    #bigrams = bigram_finder.nbest(score_fn, n)
    document_bigrams = set(nltk.bigrams(document))
    features = {}
    for bigram in bigram_word_features:
        features['contains({})'.format(bigram)] = (bigram in document)
    return features

def create_sets(documents, word_features, bigram):
    """Creates training and test sets"""
    #if bigram:
    #    feature_sets = [(bigram_features(d), c) for (d, c) in documents]
    #else:
    feature_sets = [(features(d, word_features), c) for (d, c) in documents]
    random.shuffle(feature_sets)
    cutoff = math.ceil(len(feature_sets) * 0.7)
    train_set, test_set = feature_sets[:cutoff], feature_sets[cutoff:]
    return (train_set, test_set)

def display(num):
    """Display classifier accuracy"""
    return '{0:.2f}'.format(num)

def run_classifier(name, classifier, train_set,
                    test_set, confusion_matrix, verbose):
    """Runs classifier on training and test set, with the
    optional parameter of a confusion matrix"""
    clf = SklearnClassifier(classifier)
    clf.train(train_set)

    # general classifier accuracy
    acc = accuracy(clf, test_set)
    if verbose:
        print('  ', '{}: {}%'.format(name, display(acc * 100)))

    # confusion matrix
    if confusion_matrix:
        gold = clf.classify_many([fs for (fs, l) in test_set])
        test = [l for (fs, l) in test_set]
        cm = nltk.ConfusionMatrix(gold, test)
        print(cm.pretty_format(show_percents=True))

    return acc

def setup_documents():
    """Sets up documents"""
    documents, total_words = [], []
    for category in CATEGORIES:
        for fileid in fileids(category):
            if fileid == '.DS_Store':
                continue
            path = os.path.join(PARENT, 'corpus', 'processed',
                                category, fileid)
            w = words(path)
            documents.append((w, category))
            total_words.extend(w)
    return (documents, total_words)

def setup_pos_documents():
    """Sets up documents for POS feature extraction"""
    documents, total_words = [], []
    brown_tagged_sents = brown.tagged_sents()
    tagger = nltk.UnigramTagger(
        brown_tagged_sents,
        backoff=nltk.DefaultTagger('NN')
    )

    for category in CATEGORIES:
        for fileid in fileids(category):
            if fileid == '.DS_Store':
                continue
            path = os.path.join(PARENT, 'corpus', 'processed',
                                category, fileid)
            doc_tags = []
            for sent in sents(path):
                tags = ['{}_{}'.format(x,y) for (x,y) in \
                        tagger.tag(sent.split(' '))]
                doc_tags.extend(tags)
                total_words.extend(tags)
            documents.append((doc_tags, category))
    return (documents, total_words)

if __name__ == '__main__':
    ITERATIONS = 50
    OUTPUT_FILE = 'exp10.csv'

    # part 1: prepare documents and vocabulary
    # - each document is a single user's tweet
    # - vocabulary contains entire collection of words
    documents, total_words = setup_documents()
    # documents, total_words = setup_pos_documents()

    # part 2a: prepare feature sets

    # Unigram settings
    # vocab = set(total_words)
    # word_features = list(vocab)

    # Bigram settings
    # bigram_finder = BigramCollocationFinder.from_words(word_features)
    # bigram_word_features = bigram_finder.nbest(BigramAssocMeasures.chi_sq, 2500)
    # feature_sets = [(bigram_features(d), c) for (d, c) in documents]

    # Combined settings
    # random.shuffle(word_features)
    # word_features = word_features[:FEATURES]
    # unigram_features = [(features(d), c) for (d, c) in documents]
    # bigram_features = [(bigram_features(d), c) for (d, c) in documents]

    # keep track of averages
    nb_avg = 0
    svm_avg = 0
    reg_avg = 0

    f = open(os.path.join(PARENT, 'data', OUTPUT_FILE), 'w+')

    for i in range(ITERATIONS):
        print('Iteration {}'.format(i + 1))

        # part 2b: shuffle feature sets

        # Unigram options
        # random.shuffle(word_features)
        # word_features = word_features[:FEATURES]
        # train_set, test_set = create_sets(documents, word_features, False)

        # Bigram options
        # random.shuffle(feature_sets)
        # cutoff = math.ceil(len(feature_sets) * 0.7)
        # train_set, test_set = feature_sets[:cutoff], feature_sets[cutoff:]

        # Combined options
        # random.shuffle(unigram_features)
        # random.shuffle(bigram_features)
        # feature_sets = unigram_features
        # cutoff = math.ceil(len(feature_sets) * 0.7)
        # train_set, test_set = feature_sets[:cutoff], feature_sets[cutoff:]

        # part 3: run classifiers
        # Naive Bayes, SVM, Logistic Regression
        nb_acc = run_classifier('Multinomial NB', MultinomialNB(),
                                train_set, test_set, False, True)
        svm_acc = run_classifier('NuSVC', NuSVC(), train_set,
                                    test_set, False, True)
        reg_acc = run_classifier('Logistic Regresion', LogisticRegression(),
                                    train_set, test_set, False, True)

        csv = '{},{},{},{}\n'
        f.write(csv.format(i, nb_acc, svm_acc, reg_acc))

        nb_avg += nb_acc
        svm_avg += svm_acc
        reg_avg += reg_acc

    f.close()

    print()
    print('Averages:')
    print('MultinomialNB: {}'.format(nb_avg / ITERATIONS))
    print('NuSVC: {}'.format(svm_avg / ITERATIONS))
    print('Logistic Regression: {}'.format(reg_avg / ITERATIONS))
