import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.family'] = 'Times New Roman'

def create_feature_graph(data, feature, fname):
    N = 3

    ind = np.arange(N)
    width = 0.55

    fig, ax = plt.subplots()
    ax.set_title('Classifier Performance With {} Features'.format(feature))
    ax.set_xlabel('Classifiers')
    ax.set_ylabel('Accuracy')
    ax.set_xticks(ind)
    ax.set_xticklabels(('NB', 'SVM', 'LR'))

    rect = ax.bar(ind, data, width, color='#003249')

    for i,r in enumerate(rect):
        acc = '{0:.5f}'.format(data[i])
        height = r.get_height()
        ax.text(r.get_x() + r.get_width() / 2, height - (height * 0.07),
                acc, ha='center', va='bottom', color='#FFFFFF')

    plt.savefig('{}.png'.format(fname), format='png', dpi=1000)

unigram_means = (0.8174468085106384, 0.859148936170213, 0.9165957446808518)
bigram_means = (0.9302127659574474, 0.5893617021276597, 0.9097872340425538)
pos_unigram_means = (0.5378723404255318, 0.538723404255319, 0.5446808510638296)
pos_bigram_means = (0.5668085106382977, 0.5702127659574467, 0.5804255319148934)

create_feature_graph(unigram_means, 'Unigram', 'unigram')
create_feature_graph(bigram_means, 'Bigram', 'bigram')
create_feature_graph(pos_unigram_means, 'POS Unigram', 'pos_unigram')
create_feature_graph(pos_bigram_means, 'POS Bigram', 'pos_bigram_means')
