import numpy as np
import operator

def classify0(inX, dataset, labels, k):
    dataSetSize = dataset.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1),) - dataset
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()

    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


label = ['A', 'A', 'B', 'B']
dataset = np.array([
    [1., 1.1],
    [1., 1.],
    [0., 0.],
    [0., 0.1]
])

inX = np.array([1.2, 1.0])
k = 3

print classify0(inX, dataset, label, k)