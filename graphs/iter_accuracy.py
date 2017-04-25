import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.family'] = 'Times New Roman'

iters = []
nb_avg, svm_avg, lr_avg = [], [], []

f = open('../data/selection.csv', 'r')
for line in f.read().strip().split('\n'):
    line = line.strip()
    tokens = [float(token) for token in line.split(',')]
    num, a1, a2, a3, t1, t2, t3 = tokens
    iters.append(num)
    nb_avg.append(a2)
    svm_avg.append(a1)
    lr_avg.append(a3)
f.close()

plt.title('Classifier Accuracy with Different Feature Sets')
plt.xlabel('Number of Features')
plt.ylabel('Accuracy')

# plots
plt.scatter(iters, nb_avg, s=np.pi * 3, color='#80CED7')
plt.scatter(iters, svm_avg, s=np.pi * 3, color='#007EA7')
plt.scatter(iters, lr_avg, s=np.pi * 3, color='#003249')

# legend
l1 = mpatches.Patch(label='NB', color='#80CED7')
l2 = mpatches.Patch(label='SVM', color='#007EA7')
l3 = mpatches.Patch(label='LR', color='#003249')

# focus box
plt.axvspan(4900, 5100, linewidth=0, color='#000000', alpha=0.2)

# legend
plt.legend(
    loc='lower right',
    edgecolor='#D8D8D8',
    framealpha=1,
    fancybox=False,
    shadow=False,
    handles=[l1, l2, l3]
)

plt.savefig('iter_accuracy.png', format='png', dpi=1000)
