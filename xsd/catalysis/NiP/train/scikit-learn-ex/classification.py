from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import  accuracy_score
from matplotlib.colors import ListedColormap

sc = StandardScaler()
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
Y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
sc.fit(X_train)

X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

ppn = Perceptron(n_iter=5000, eta0=0.1, random_state=0)
ppn.fit(X_train, y_train)
y_pre = ppn.predict(X_test)
# print "Accuracy: {:.2%}".format(accuracy_score(y_test, y_pre))


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    print np.unique(y)

    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    xxx = np.array([xx1.ravel(), xx2.ravel()]).T

    Z = classifier.predict(xxx)

    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, slpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, c=cmap(idx), marker=markers[idx], label=cl)

    if test_idx:
        x_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(x_test[:, 0], x_test[:, 1], c='', alpha=1.0, linewidths=1, marker='o', s=55, label='test data')


X_combined_std = np.vstack((X_train_std, X_test_std))

y_combined = np.hstack((y_train, y_test))

plot_decision_regions(X=X_combined_std, y=y_combined, classifier=ppn, test_idx=range(105, 150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.show()

# xx1, xx2 = np.meshgrid(np.arange(-3.0, 3.0, 0.02), np.arange(-3.0, 3.0, 0.02))
#
# xxx = np.array([xx1.ravel(), xx2.ravel()]).T
# zjw = ppn.predict(xxx)
# print np.unique(zjw)
