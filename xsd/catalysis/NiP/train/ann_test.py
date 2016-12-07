import numpy
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import SigmoidLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer


# preparing data
data_path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/NiP/train/coulomb.txt"
data = numpy.loadtxt(data_path)
length = data.shape[0]


net = buildNetwork(10, 4, 1)
ds = SupervisedDataSet(10, 1)
for i in range(length):
    ds.addSample(data[i][:10], data[i][10])

trndata, tstdata = ds.splitWithProportion(0.25)


print tstdata
print trndata

# trainer = BackpropTrainer(net, dataset=trndata,
#                           momentum=0.1, verbose=True, weightdecay=0.01)
#
# for i in range(1000):
#     trainer.trainEpochs(10)
