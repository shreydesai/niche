import time
import random

from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import NuSVC
from sklearn.linear_model import LogisticRegression

from niche.script import setup_documents, create_sets, run_classifier

documents, total_words = setup_documents()
vocab = set(total_words)
wf_master = list(vocab)

START = 100
END = 10000 + START
ITERS = 25

f = open('selection.csv', 'w+')
feature_size = 100

for i in range(START, END, 100):
    nb_avg, svm_avg, lr_avg = (0,) * 3
    init_time, nb_time, svm_time, lr_time = (0,) * 4

    for k in range(ITERS):
        t0 = time.time()
        word_features = wf_master[:feature_size]
        train_set, test_set = create_sets(documents, word_features, False)
        init_time = (time.time() - t0)

        t1 = time.time()
        nb_acc = run_classifier('Multinomial NB', MultinomialNB(),
                                train_set, test_set, False, False)
        nb_time += init_time + (time.time() - t1)

        t2 = time.time()
        svm_acc = run_classifier('SVM', NuSVC(),
                        train_set, test_set, False, False)
        svm_time += init_time + (time.time() - t2)

        t3 = time.time()
        lr_acc = run_classifier('LR', LogisticRegression(),
                        train_set, test_set, False, False)
        lr_time += init_time + (time.time() - t3)

        nb_avg += nb_acc
        svm_avg += svm_acc
        lr_avg += lr_acc

    nb_avg /= ITERS
    svm_avg /= ITERS
    lr_avg /= ITERS

    nb_time /= ITERS
    svm_time /= ITERS
    lr_time /= ITERS

    feature_size += 100

    print('{},{},{},{},{},{},{}'.format(
        i, nb_avg, svm_avg, lr_avg, nb_time, svm_time, lr_time
    ))

    f = open('selection.csv', '')
    f.write('{},{},{},{},{},{},{}\n'.format(
        i, nb_avg, svm_avg, lr_avg, nb_time, svm_time, lr_time
    ))
    f.close()



f.close()
