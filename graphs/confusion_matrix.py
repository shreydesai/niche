import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Times New Roman'

def create_confusion_matrix(cm, title, fname):
    fig = plt.figure()
    plt.clf()
    ax = fig.add_subplot(111)
    ax.set_aspect(1)
    res = ax.imshow(np.array(cm), cmap=plt.get_cmap('GnBu'),
                    interpolation='nearest')

    width, height = len(cm), len(cm[0])

    for x in range(width):
        for y in range(height):
            ax.annotate(str(cm[x][y]), xy=(y, x),
                        horizontalalignment='center',
                        verticalalignment='center')

    cb = fig.colorbar(res)
    alphabet = ['ent', 'fun', 'games', 'politics', 'science',
                'sports', 'tech', 'weather']

    plt.tight_layout()
    plt.xticks(range(width), alphabet[:width])
    plt.yticks(range(height), alphabet[:height])

    plt.title(title)
    plt.xlabel('Predicted')
    plt.ylabel('Reference')

    locs, labels = plt.xticks()
    plt.setp(labels, rotation=45, ha='right')

    plt.tight_layout()

    plt.savefig('{}.png'.format(fname), format='png', dpi=1000)

# Naive Bayes
cm = [[2.1, 0, 6.4, 0, 0, 2.1, 4.3, 0],
        [2.1, 8.5, 2.1, 0, 0, 0, 0, 0],
        [0, 0, 8.5, 0, 0, 0, 0, 0],
        [0, 0, 0, 12.8, 0, 0, 0, 0],
        [0, 0, 0, 0, 6.4, 0, 2.1, 6.4],
        [0, 0, 0, 0, 0, 14.9, 0, 0],
        [0, 0, 0, 0, 0, 0, 10.6, 0],
        [0, 2.1, 0, 0, 0, 0, 0, 8.5]]
create_confusion_matrix(cm, 'Naive Bayes Classifier Accuracy',
                        'nb_cm')

# SVM
cm = [[2.1, 0, 0, 0, 0, 0, 2.1, 0],
        [2.1, 8.5, 0, 0, 0, 0, 0, 0],
        [0, 2.1, 14.9, 0, 0, 0, 0, 0],
        [0, 0, 0, 12.8, 0, 0, 0, 0],
        [0, 0, 0, 0, 4.3, 0, 0, 0],
        [0, 0, 0, 0, 0, 17.0, 0, 0],
        [0, 0, 0, 0, 2.1, 0, 14.9, 0],
        [0, 0, 2.1, 0, 0, 0, 0, 14.9]]
create_confusion_matrix(cm, 'SVM Classifier Accuracy',
                        'svm_cm')

# Logistic Regression
cm = [[2.1, 0, 0, 0, 0, 0, 2.1, 0],
        [2.1, 10.6, 0, 0, 0, 0, 0, 0],
        [0, 0, 17.0, 0, 0, 0, 0, 0],
        [0, 0, 0, 12.8, 0, 0, 0, 0],
        [0, 0, 0, 0, 6.4, 0, 0, 0],
        [0, 0, 0, 0, 0, 17.0, 0, 0],
        [0, 0, 0, 0, 0, 0, 14.9, 0],
        [0, 0, 0, 0, 0, 0, 0, 14.9]]
create_confusion_matrix(cm, 'Logistic Regression Classifier Accuracy',
                        'lr_cm')
