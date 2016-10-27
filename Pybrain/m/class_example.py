# -*- coding: utf-8 -*-
from pybrain.datasets import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer
from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot, savefig
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal

'''
To have a nice dataset for visualization,
we produce a set of points in 2D belonging to three different classes.
You could also read your data from a file, e.g. using pylab.load().
'''

means = [(-1, 0), (2, 4), (3, 1)]
cov = [diag([1, 1]), diag([0.5, 1.2]), diag([1.5, 0.7])]
alldata = ClassificationDataSet(2, 1, nb_classes=3)

for n in xrange(400):
    for klass in range(3):
        in_put = multivariate_normal(means[klass], cov[klass])
        # 高斯正态分布, numpy.random.multivariate_normal(mean, cov[, size])
        # 其中mean代表正态分布的平均值
        # cov代表正态分布的均方差
        # mean 和 cov 的length代表了不同维数
        # 返回的值也是一个与mean,cov的length相同的array
        alldata.addSample(in_put, [klass])
        # 通过numpy的 multivariate_normal 产生一个(x,y),符合高斯分布
        #这些数据分别对应于[0,1,2]三个class, 并将他们分类

# randomly split the dataset into 75% training and 25% test data sets.
# We could also have created two different datasets to begin with.
tstdata_temp, trndata_temp = alldata.splitWithProportion(0.25)

tstdata = ClassificationDataSet(inp=tstdata_temp['input'].copy(),
                                target=tstdata_temp['target'].copy(),
                                nb_classes=3
                                )

trndata = ClassificationDataSet(2, 1, nb_classes=3)
trndata = ClassificationDataSet(inp=trndata_temp['input'].copy(),
                                target=trndata_temp['target'].copy(),
                                nb_classes=3
                                )

'''
for neural classfication,
it is highly advisable to encode classes with one output neuron per class.
Note that this operation duplicates the original targets and
 stores them in an (integer) field named 'class'.
'''

trndata._convertToOneOfMany()
tstdata._convertToOneOfMany()


'''
there is relationship
[0] ==> [1, 0, 0]
[1] ==> [0, 1, 0]
[2] ==> [0, 0, 1]

generally: for n
[i] ==> a=[0,0,0...,1,...0,0,0]
(a[i]=1)
'''

# build a feed-forward network with 5 hidden units
# use the shortcut buildNetwork()
# input and output layer size must match dataset' input and tartget dimension
# you could add additional hidden layers-
# by inserting more numbers giving the desired layer sizes
# the output layer uses a softmax function because we are doing classfication

fnn = buildNetwork(trndata.indim, 5, trndata.outdim, outclass=SoftmaxLayer)

# set up a trainer that basically takes the network and training dataset-
# as input (using BackpropTrainer for this)
# Backpropagation BP --> 误差反向传播算法
# verbose = True 表示训练时会把Total error打印出来
trainer = BackpropTrainer(fnn, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)
tricks = arange(-3., 6., 0.2)

# generate a square grid of data points and put it into a dataset
# classify to obtain a nice contour field for visualization
#
X, Y = meshgrid(tricks, tricks)
# need column vectors in dataset, not arrays
gridata = ClassificationDataSet(2, 1, nb_classes=3)
for i in xrange(X.size):
    gridata.addSample([X.ravel()[i], Y.ravel()[i]], [0])

gridata._convertToOneOfMany()

# train the network for some  epochs.
# Usally you would set something like 5 here,
# but for visualization purposes we do this one epoch at a time
for i in range(20):
    trainer.trainEpochs(1)
    # evalueate the network on the training and test data
    trnresult = percentError(trainer.testOnClassData(), trndata['class'])
    tstresult = percentError(trainer.testOnClassData(dataset=tstdata), tstdata['class'])
    print "epoch: %4d" % trainer.totalepochs, \
          " train error: %5.2f%%" % trnresult, \
          " test error: %5.2f%%" % tstresult
    # run our grid data throught the FNN,
    # get the most likely class and shape it into a aquare array again
    out = fnn.activateOnDataset(gridata)
    out = out.argmax(axis=1)
    out = out.reshape(X.shape)
    print out
    # plot the test date and the underlying grid as a filled contour
    figure(1)
    ioff()         # interactive graphics off
    clf()          # clear the plot
    hold(True)     # overplot on
    for c in [0, 1, 2]:
        here, _ = where(tstdata['class']==c)
        plot(tstdata['input'][here, 0], tstdata['input'][here, 1], 'o')
    if out.max() != out.min():       # safety check against flat field
        contourf(X, Y, out)          # plot the contour
    ion()                            # interacive graphics on
    draw()                           # update the plot
    savefig('figure' + str(i) + '.jpg')
# keep showing the plot until user kills it
ioff()
show()
