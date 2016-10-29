import numpy as np
import operator

label = ['A', 'A', 'B', 'B']

dataset = np.array([
    [1., 1.1],
    [1., 1.],
    [0., 0.],
    [0., 0.1]
])

inX = np.array([1.2, 1.0])
dataSetSize = dataset.shape[0]
diffMat = np.tile(inX, (dataSetSize, 1),) - dataset
a = diffMat**2
dis = np.sqrt(a.sum(axis=1))
print dis.argsort()