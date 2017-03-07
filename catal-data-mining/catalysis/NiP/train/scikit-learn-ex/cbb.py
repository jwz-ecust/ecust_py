#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 12/26/16
import numpy as np
from sklearn import datasets
from sklearn import svm
import pylab as pl
from sklearn import neighbors
from sklearn import cluster

iris = datasets.load_iris()
# print np.unique(iris.target)


digits = datasets.load_digits()
# pl.imshow(digits.images[0], cmap=pl.cm.gray_r)
# pl.show()
data = digits.images.reshape((digits.images.shape[0], -1))

clf = svm.LinearSVC()
clf.fit(iris.data, iris.target)
print clf.predict([[5., 3.6, 1.3, 0.25]])
# print clf.coef_

knn = neighbors.KNeighborsClassifier()
knn.fit(iris.data, iris.target)
print knn.predict([[5., 3.6, 1.3, 0.25]])


svc = svm.SVC(kernel='rbf')
svc.fit(iris.data, iris.target)
print svc.predict([[5., 3.6, 1.3, 0.25]])


k_means = cluster.KMeans(3)
k_means.fit(iris.data)
print k_means.labels_[::10]
print iris.target[::10]
