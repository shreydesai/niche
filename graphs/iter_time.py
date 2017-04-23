import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.family'] = 'Times New Roman'

iters = []
nb_time, svm_time, lr_time = [], [], []

f = open('../data/selection.csv', 'r')
for line in f.read().strip().split('\n'):
    line = line.strip()
    tokens = [float(token) for token in line.split(',')]
    num, a1, a2, a3, t1, t2, t3 = tokens
    iters.append(num)
    nb_time.append(t1)
    svm_time.append(t2)
    lr_time.append(t3)
f.close()

plt.title('Classifier Training Time with Different Feature Sets')
plt.xlabel('Number of Features')
plt.ylabel('Time (sec)')

# plots
plt.scatter(iters, nb_time, s=np.pi * 3, color='#80CED7')
plt.scatter(iters, svm_time, s=np.pi * 3, color='#007EA7')
plt.scatter(iters, lr_time, s=np.pi * 3, color='#003249')

# legend
l1 = mpatches.Patch(label='NB', color='#80CED7')
l2 = mpatches.Patch(label='SVM', color='#007EA7')
l3 = mpatches.Patch(label='LR', color='#003249')

# focus box
plt.axvspan(4900, 5100, linewidth=0, color='#000000', alpha=0.2)

# legend
plt.legend(
    loc='upper right',
    edgecolor='#D8D8D8',
    framealpha=1,
    fancybox=False,
    shadow=False,
    handles=[l1, l2, l3]
)

plt.savefig('iter_time.png', format='png', dpi=1000)
