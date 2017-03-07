import numpy
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import SigmoidLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.utilities import percentError


# preparing data
data_path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/NiP/train/gab.txt"
data = numpy.loadtxt(data_path)
print data.shape

length = data.shape

# print length
net = buildNetwork(length[1] - 1, 4, 4, 1)
ds = SupervisedDataSet(length[1] - 1, 1)
for i in range(length[0]):
    ds.addSample(data[i][:length[1] - 1], data[i][length[1] - 1])

print ds.data
trndata, testdata = ds.splitWithProportion(0.75)

trainer = BackpropTrainer(net, dataset=trndata,
                          momentum=0.1, verbose=True, weightdecay=0.01)
for i in range(20):
    trainer.trainEpochs(10)

a = trainer.testOnData(dataset=testdata, verbose=True)
print a
