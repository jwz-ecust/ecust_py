import numpy
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import SigmoidLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.utilities import percentError


# preparing data
data_path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/NiP/train/bader_coulomb.txt"
data = numpy.loadtxt(data_path)

length = data.shape[1]

# print length
net = buildNetwork(length - 1, 3, 1)
ds = SupervisedDataSet(length - 1, 1)
for i in range(length):
    ds.addSample(data[i][:length - 1], data[i][length - 1])

trndata, testdata = ds.splitWithProportion(0.75)
# print trndata.getLength()
# print testdata.getLength()

trainer = BackpropTrainer(net, dataset=trndata,
                          momentum=0.1, verbose=True, weightdecay=0.01)
for i in range(10000):
    trainer.trainEpochs(10)

print trainer.testOnData(dataset=testdata, verbose=True)
