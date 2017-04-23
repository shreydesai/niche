import os
import numpy as np

parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = os.path.join(parent, 'data')
blacklist = set(['.DS_Store', 'selection.csv'])

for item in os.listdir(data):
    if item.endswith('.csv') and item not in blacklist:
        print('{} stats'.format(item))

        f = open(os.path.join(data, item), 'r')
        nb, svm, lr = [], [], []
        # read header
        f.readline()
        # parse data
        fdata = f.read().strip().split('\n')
        for line in fdata:
            i, t1, t2, t3 = line.split(',')
            nb.append(float(t1))
            svm.append(float(t2))
            lr.append(float(t3))
        # calculate std dev
        nb_std = np.std(nb)
        svm_std = np.std(svm)
        lr_std = np.std(lr)

        print(' ', 'NB Std: {}'.format(nb_std))
        print(' ', 'SVM Std: {}'.format(svm_std))
        print(' ', 'LR Std: {}'.format(lr_std))

        f.close()
