# -*- coding: utf-8 -*-
from pybrain.structure import FeedForwardNetwork, LinearLayer,SigmoidLayer, FullConnection
from pybrain.supervised import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
import numpy as np

def netBuild(ds):
    # 建立神经网络 fnn
    fnn = FeedForwardNetwork()

    # 设立三层, 一层输入, 一层隐藏, 一层输出
    inLayer = LinearLayer(13, name="inLayer")
    hiddenLayer = SigmoidLayer(13, name="hiddenLayer")
    outLayer = LinearLayer(1, name="outLayer")
    # 将三层都加入神经网络
    fnn.addInputModule(inLayer)
    fnn.addModule(hiddenLayer)
    fnn.addOutputModule(outLayer)
    # 建立三层之间的链接
    in_to_hidden = FullConnection(inLayer, hiddenLayer)
    hidden_to_out = FullConnection(hiddenLayer, outLayer)
    # 将链接加入神经网络
    fnn.addConnection(in_to_hidden)
    fnn.addConnection(hidden_to_out)
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
        ds.addSample(tuple(data[1:]),(data[0]))
    dsTrain, dsTest = ds.splitWithProportion(0.8)
    return dsTrain, dsTest

dsTrain, dsTest = dsBuild(readData('/Users/zhangjiawei/Dropbox/zjw/everyday/Pybrain/data.txt'))
netModel = netBuild(dsTrain)
for i in range(0, len(dsTest['input'])):
    res = []
    for j in range(1,len(dsTest[i])):
        res.append(i[j])
    temp_data = tuple(res)
    error = dsTest['target'][i] - netModel.activate(temp_data)
    print error
