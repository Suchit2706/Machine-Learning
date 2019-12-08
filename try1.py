import random
import numpy as np


def sigmoid(x):
    a = float(1/(1+np.exp(-x)))
    return a


def w1():
    b = [[2, 1, 0], [1, 2, 2], [0, 3, 1]]
    return b


def bias():
    a = [0, 0, -1]
    b = -1
    return a, b


def w2():
    a = [-1, 1, 2]
    return a


def cal_hid(inlayer, weights1, hlayer1, bias1):
    for i in range(0, 3):
        for j in range(0, 3):
            hlayer1[i] += float(weights1[j][i]) * inlayer[j]
        hlayer1[i] += float(bias1[i])
        hlayer1[i] = sigmoid(hlayer1[i])
        hlayer1[i] = round(hlayer1[i], 4)
    return hlayer1


def cal_out(hlayer1, weights2, bias2):
    olayer = 0.0
    for i in range(0, 3):
        olayer += float(hlayer1[i]) * float(weights2[i])
    olayer += float(bias2)
    y = sigmoid(olayer)
    y = round(y, 4)
    return y


def cal_error(y, t):
    a = (t - y)*(t - y)/2
    a = round(a, 4)
    return a


'''
inlayer = [1, 1, 1, 1, 1, 1, 1, 1, 1]
hlayer1 = [0, 0, 0, 0, 0, 0, 0, 0]
bias1 = []      # Bias between Input and Hidden Layer
bias2 = 0.0     # Bias between Hidden layer and Output
weights1 = []   # input to hidden
weights2 = []   # hidden to output
y = 0.0
t = 1.0
error = 0.0
olayer = 0.0

# Initialising weights1
weights1 = w1(weights1)

# Initializing Biases
bias1, bias2 = bias(bias1, bias2)

# Initialising weights2
weights2 = w2(weights2)

# Calculating hidden layers
hlayer1 = cal_hid(inlayer, weights1, hlayer1, bias1)

# Calculating output
# y = cal_out(hlayer1, weights2, y, bias2)
print(y)

# Calculating Error
error = cal_error(y, t)
'''


def Adjust_weights(inlayer, weights1, bias1, hlayer, weights2, bias2, y, t):
    alpha = 0.3
    e1 = y*(1 - y)*(t - y)
    e1 = round(e1, 4)
    print('1: ', e1)
    for i in range(0, 3):
        weights2[i] = float(weights2[i]) + alpha*e1*y
    bias2 = float(bias2) + alpha*e1

    for i in range(0, 3):
        e2 = hlayer[i] * (1 - hlayer[i]) * e1 * (weights2[i])
        e2 = round(e2, 4)
        print(i, e2)
        for j in range(0, 3):
            weights1[j][i] = round(float(weights1[j][i]) + alpha*e2*inlayer[j], 4)
        bias1[i] = round(float(bias1[i]) + alpha*e2, 4)
    print('w1', weights1)
    print('w2', weights2)

    return weights1, weights2, bias1, bias2


# weights1, weights2, bias1, bias2 = Adjust_weights(inlayer, weights1, bias1, hlayer1, weights2, bias2, y, t)
# print(error)