import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.family'] = 'Times New Roman'

N = 3

unigram_means = (0.8174468085106384, 0.859148936170213, 0.9165957446808518)
bigram_means = (0.9302127659574474, 0.5893617021276597, 0.9097872340425538)
pos_unigram_means = (0.5378723404255318, 0.538723404255319, 0.5446808510638296)
pos_bigram_means = (0.5668085106382977, 0.5702127659574467, 0.5804255319148934)
all_means = (0.8310638297872345, 0.8795744680851069, 0.936170212765958)

bars = [pos_unigram_means, pos_bigram_means, unigram_means,
        bigram_means, all_means]
colors = ['#DFF8EB', '#9AD1D4', '#80CED7', '#007EA7', '#003249']
labels = ['POS Unigram', 'POS Bigram', 'Unigram', 'Bigram', 'All Features']

ind = np.arange(N)
width = 0.15

fig, ax = plt.subplots()
ax.set_title('Classifier Performance Across Feature Sets')
ax.set_xlabel('Classifiers')
ax.set_ylabel('Accuracy')
ax.set_xticks(ind + width * 2)
ax.set_xticklabels(('NB', 'SVM', 'LR'))

for i in range(5):
    rect = ax.bar(ind + width * i, bars[i], width, color=colors[i])

handles = []
for i in range(5):
    patch = mpatches.Patch(color=colors[i], label=labels[i])
    handles.append(patch)

plt.legend(
    loc='lower right',
    edgecolor='#D8D8D8',
    framealpha=1,
    fancybox=False,
    shadow=False,
    handles=handles
)

plt.savefig('performance.png', format='png', dpi=1000)
