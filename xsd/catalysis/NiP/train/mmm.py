# -*- coding: utf-8 -*-
from sklearn import svm
import numpy as np
from sklearn import preprocessing


def leave_one_validation(n, data):
    shape = data.shape
    leave_one = data[n]
    _data = np.zeros((shape[0]-1, shape[1]))
    _data[:i] = data[:i]
    _data[i:] = data[i+1:]
    return _data, leave_one


def svm_learn(train, test):
    clf = svm.SVR()
    clf.fit(train[:, :-1], train[:, -1])
    wait_pre = test[:-1].reshape(1, -1)
    p = clf.predict(wait_pre)
    real = test[-1]
    return real, p[0]


path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/NiP/train/gab.txt"
data = np.loadtxt(path)
shape = data.shape
rmse = 0.0
for i in range(shape[0]):
    train, test = leave_one_validation(i, data)
    r, p = svm_learn(train, test)
    print p, r
    rmse += (r - p)**2

RMSE = (rmse/60)**0.5
print RMSE
