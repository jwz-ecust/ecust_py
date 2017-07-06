import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_circles
from mpl_toolkits import mplot3d
import numpy as np
from sklearn.svm import SVC

X, y = make_circles(100, factor=.1, noise=0.1)

r = np.exp(-(X ** 2).sum(1))

def plot3d(elev=30, azim=30, X=X, y=y):
    ax = plt.subplot(projection="3d")
    ax.scatter(X[:,0], X[:,1], r, c=y, s=50, cmap="autumn")
    ax.view_init(elev=elev, azim=azim)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("r")
    plt.show()


# plot3d()


clf = SVC(kernel='rbf', C=1E6)
clf.fit(X, y)

plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap="autumn")
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=300)
plt.show()
