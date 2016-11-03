import numpy as np


def latConverter(input):
    output = np.zeros((6, 1))
    x = np.array(input[0].strip().split(' ' * 5), dtype=np.float)
    y = np.array(input[1].strip().split(' ' * 5), dtype=np.float)
    z = np.array(input[2].strip().split(' ' * 5), dtype=np.float)
    output[0] = np.sqrt(sum(np.square(x)))
    output[1] = np.sqrt(sum(np.square(y)))
    output[2] = np.sqrt(sum(np.square(z)))
    output[3] = np.arccos(x.dot(y) / output[0] * output[1]) * 180.0 / np.pi
    output[4] = np.arccos(x.dot(z) / output[0] * output[2]) * 180.0 / np.pi
    output[5] = np.arccos(y.dot(z) / output[1] * output[2]) * 180.0 / np.pi
    return output




input = [
    '8.969174     0.000000     0.000000',
    '0.000000     8.969174     0.000000',
    '0.000000     0.000000     3.729227'
]

print latConverter(input)
