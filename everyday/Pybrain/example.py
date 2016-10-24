# -*- coding: utf-8 -*-
import numpy.random as npr
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork


inputVecTrain, outputVecTrain = npr.randn(20,104), npr.randn(20, 36)


# 建立训练数据集, 输入节点104个，  输出节点 36个
dsTrain = SupervisedDataSet(104, 36)

# 将输入输出数据加入Pybrain的数据集合
for i in range(len(inputVecTrain)):
    dsTrain.addSample(inputVecTrain[i], outputVecTrain[i])

# 建立测试数据集
dsTest = SupervisedDataSet(104, 36)

# 将输入输出数据加入Pybrain数据集合
for i in range(len(inputVecTrain)):
    dsTest.addSample(inputVecTrain[i], outputVecTrain[i])

# 这里是输出的样式， 第一个是输入层数据，共104个，第二个是输出层数据，共36个
for ipr, target in dsTrain:
    print ipr
    print target

fnn = buildNetwork(104, 100, 36, bias=True)

trainer = BackpropTrainer(fnn, dsTest, momentum=0.1, verbose=True, weightdecay=0.01)

# 开始训练
for i in range(200):
    trainer.trainEpochs(10)

    trnResult = percentError(trainer.testOnClassData(), dsTrain['target'])
    testResult = percentError(trainer.testOnClassData(dataset=dsTest), dsTest['target'])
    print "epoch: %4d" %trainer.totalepochs,\
          "train error: %5.2f%%" %trnResult,\
          "test error: %5.2f%%" %testResult