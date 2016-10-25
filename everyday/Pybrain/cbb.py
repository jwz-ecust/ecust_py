# -*- coding: utf-8 -*-
from pybrain.structure import FeedForwardNetwork, LinearLayer,SigmoidLayer, FullConnection
from pybrain.supervised import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
import numpy as np
from pylab import ion, ioff, figure, draw, show, plot, savefig


def netBuild(ds):
    # 建立神经网络 fnn
    fnn = FeedForwardNetwork()
    # 设立三层, 一层输入, 一层隐藏, 一层输出
    inLayer = LinearLayer(13, name="inLayer")
    hiddenLayer_1 = SigmoidLayer(5, name="hiddenLayer_1")
    hiddenLayer_2 = SigmoidLayer(2, name="hiddenLayer_2")
    outLayer = LinearLayer(1, name="outLayer")
    # 将三层都加入神经网络
    fnn.addInputModule(inLayer)
    fnn.addModule(hiddenLayer_1)
    fnn.addModule(hiddenLayer_2)
    fnn.addOutputModule(outLayer)
    # 建立三层之间的链接
    in_to_hidden1 = FullConnection(inLayer, hiddenLayer_1)
    hidden1_hidden2 = FullConnection(hiddenLayer_1, hiddenLayer_2)
    hidden2_to_out = FullConnection(hiddenLayer_2, outLayer)
    # 将链接加入神经网络
    fnn.addConnection(in_to_hidden1)
    fnn.addConnection(hidden1_hidden2)
    fnn.addConnection(hidden2_to_out)
    # 让神经网络可用
    fnn.sortModules()
    print "Trainging starting==========>"
    trainer = BackpropTrainer(fnn, ds, verbose=True, learningrate=0.01)
    trainer.trainUntilConvergence(maxEpochs=1000)
    print "Finish training"
    return fnn


def readData(path):
    data = np.loadtxt(path)
    return data


def dsBuild(data):
    ds = SupervisedDataSet(13, 1)
    for ele in data:
        ds.addSample(tuple(ele[1:]),(ele[0]))
    dsTrain, dsTest = ds.splitWithProportion(0.8)
    return dsTrain, dsTest


dsTrain, dsTest = dsBuild(readData('./data.txt'))
netModel = netBuild(dsTrain)
res = []
result = []
RMSE = 0
print len(dsTest['input'])
for i in range(len(dsTest['input'])):
    figure(1, dpi=200)
    predict_value = netModel.activate(dsTest['input'][i])
    test_value = dsTest['target'][i]
    error = test_value - predict_value
    RMSE = RMSE + np.square(error)
    res.append(error)
    result.append((predict_value, test_value))

for j in result:
    plot(j[0], j[1], 'o')
ion()
draw()
ioff()
savefig('./Figure/myfig.jpg')

print "the RMSE (root-mean-square error): {}".format(np.sqrt(RMSE/58.0))
