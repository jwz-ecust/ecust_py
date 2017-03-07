#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 17/1/4

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
import numpy as np
from sklearn import metrics

iris = datasets.load_iris()
x_iris, y_iris = iris.data, iris.target

X, y = x_iris[:, :2], y_iris

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)      # 标准化数据
X_test = scaler.transform(X_test)

colors = ['red', 'greenyellow', 'blue']
# for i in xrange(len(colors)):
#     px = X_train[:, 0][y_train == i]
#     py = X_train[:, 1][y_train == i]
#     print px.shape, py.shape
#     plt.scatter(px, py, c=colors[i])
# plt.legend(iris.target_names)
# plt.xlabel('Sepal length')
# plt.ylabel('Sepal width')
# plt.show()

clf = SGDClassifier()
clf.fit(X_train, y_train)

y_train_pred = clf.predict(X_train)
print metrics.accuracy_score(y_train, y_train_pred)
y_test_pred = clf.predict(X_test)
print metrics.accuracy_score(y_test, y_test_pred)

print metrics.classification_report(y_test, y_test_pred)


x_min, x_max = X_train[:, 0].min() -0.5, X_train[:, 0].max() + 0.5
y_min, y_max = X_train[:, 1].min() -0.5, X_train[:, 1].max() + 0.5
xs = np.arange(x_min, x_max, 0.5)   # 用于画分界线的
# fig, axes = plt.subplots(1, 3)
# fig.set_size_inches(8.5, 5)
# for i in [0, 1, 2]:
#     axes[i].set_aspect('equal')
#     axes[i].set_title('Class' + str(i) + 'versus the rest')
#     axes[i].set_xlabel('Sepal length')
#     axes[i].set_ylabel('Sepal width')
#     axes[i].set_xlim(x_min, x_max)
#     axes[i].set_ylim(y_min, y_max)
#     plt.sca(axes[i])
#     for j in xrange(len(colors)):
#         px = X_train[:, 0][y_train == j]
#         py = X_train[:, 1][y_train == j]
#         plt.scatter(px, py, c=colors[j])
#     ys = (-clf.intercept_[i] - xs*clf.coef_[i, 0])/clf.coef_[i, 1]
#     plt.plot(xs, ys, hold=True)
# plt.show()




for j in xrange(len(colors)):
    px = X_train[:, 0][y_train == j]
    py = X_train[:, 1][y_train == j]
    plt.scatter(px, py, c=colors[j])
    ys = (-clf.intercept_[j] - xs*clf.coef_[j, 0])/clf.coef_[j, 1]
    plt.plot(xs, ys, hold=True)
plt.show()
