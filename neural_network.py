import random
import numpy as np


def sigmoid(x):
    a = float(1/(1+np.exp(-x)))
    return a


def w1(b):
    for i in range(0, 9):
        a = []
        for j in range(0, 8):
            a.append('%.1f' % (random.randrange(0, 10, 1) * 0.01))
        b.append(a)
    return b


def bias(a, b):
    for i in range(0, 8):
        a.append('%.1f' % (random.randrange(0, 10, 1) * 0.01))
    b = ('%.1f' % (random.randrange(0, 10, 1) * 0.01))
    return a, b


def w2(a):
    for i in range(0, 8):
        a.append('%.1f' % (random.randrange(0, 10, 1) * 0.01))
    return a


def cal_hid(inlayer, weights1, hlayer1, bias1):
    for i in range(0, 8):
        for j in range(0, 9):
            hlayer1[i] += float(weights1[j][i]) * inlayer[j]
        hlayer1[i] += float(bias1[i])
        hlayer1[i] = sigmoid((hlayer1[i]))
    return hlayer1


def cal_out(hlayer1, weights2, bias2):
    olayer = 0.0
    for i in range(0, 8):
        olayer += float(hlayer1[i]) * float(weights2[i])
    olayer += float(bias2)
    y = sigmoid(olayer)
    return y


def cal_error(y, t):
    a = (t - y)*(t - y)/2
    return a


def Adjust_weights(inlayer, weights1, bias1, hlayer, weights2, bias2, y, t):
    alpha = 0.2
    e1 = y*(1 - y)*(t - y)
    for i in range(0, 8):
        weights2[i] = float(weights2[i]) + alpha*e1*y
    bias2 = float(bias2) + alpha*e1

    for j in range(0, 8):
        e2 = hlayer[j] * (1 - hlayer[j]) * e1 * (weights2[j])
        for i in range(0, 9):
            weights1[i][j] = float(weights1[i][j]) + alpha*e2*inlayer[i]
        bias1[j] = float(bias1[j]) + alpha*e2

    return weights1, weights2, bias1, bias2


