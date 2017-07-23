import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
from dataprepare import pic2cnn


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding="SAME")


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding="SAME")


IMAGE_HEIGHT = 114
IMAGE_WIDTH = 450

#################################################################
# x = tf.placeholder("float", shape=[None, IMAGE_HEIGHT * IMAGE_WIDTH])
# y_ = tf.placeholder("float", shape=[None, 6 * 27])



W_conv1 = weight_variable([5, 5, ])
x_image = tf.reshape(x, [-1, 28, 28, 1])


##################################################################
data = pic2cnn()
x_raw, y_raw = data.gendata()       # 1818, 114, 450
x_ravel = x_raw.reshape(1818, -1)

sess = tf.Session()

sess.run(tf.global_variables_initializer())
y = tf.nn.softmax(tf.matmul(x, W) + b)



cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, dtype="float"))

for i in range(10000):
    batch = data.generatebatch(x_raw, y_raw, 50)
    sess.run(train_step, feed_dict={x: batch[0], y_: batch[1]})
    print(sess.run(y_, feed_dict={y_: y_raw}))
    if i % 100 == 0:
        print(sess.run(accuracy, feed_dict={x: x_ravel, y_: y_raw}))
