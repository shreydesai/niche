import time
from niche.script import setup_documents

documents, total_words = setup_documents()
vocab = set(total_words)
word_features = list(vocab)

START = 100
END = 10000 + START

f = open('selection.csv', 'w+')

for i in range(START, END, 100):
    feature_size = i
    nb_avg, svm_avg, lr_avg = (0,) * 3
    init_time, nb_time, svm_time, lr_time = (0,) * 4

    for k in range(5):
        t0 = time.time()
        random.shuffle(word_features)
        word_features = word_features[:FEATURES]
        train_set, test_set = create_sets(documents, bigram=False)
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

    nb_avg /= 5
    svm_avg /= 5
    lr_avg /= 5

    nb_time /= 5
    svm_time /= 5
    lr_time /= 5

    f.write('{},{},{},{},{},{},{}\n'.format(
        i, nb_avg, svm_avg, lr_avg, nb_time, svm_time, lr_time
    ))

f.close()
