# -*- coding: utf-8 -*-
from pybrain.datasets import SequentialDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer
from scipy import diag, arange, meshgrid, where
import numpy as np

DS = SequentialDataSet(3, 2)

X = np.random.rand(100, 3)
Y = np.random.rand(100, 2)

for i in zip(X, Y):
    DS.appendLinked(i[0], i[1])


for i in range(DS.getNumSequences()):
    print i
