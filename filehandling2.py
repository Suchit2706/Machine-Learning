import test
from matplotlib import pyplot as plt

# inlayer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
bias1 = []  # Bias between Input and Hidden Layer
bias2 = 0.0  # Bias between Hidden layer and Output
olayerlayer = 0.0
weights1 = []  # input to hidden1
weights2 = []  # hidden1 to hidden2
y = 0.0
error = 0.0
cost = 0.0
errors = []
errors1 = []
'''
weights1 = nn.w1(weights1)
weights2 = nn.w2(weights2)
bias1, bias2 = nn.bias(bias1, bias2)
'''

# print(weights1, '\n', weights2, '\n', bias1, '\n', bias2)


def nn1(weights1, weights2, bias1, bias2):
    import neural_network as nn
    f = open('move1.txt', 'r')
    inlayer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # bias1 = []  # Bias between Input and Hidden Layer
    # bias2 = 0.0  # Bias between Hidden layer and Output
    olayerlayer = 0.0
    # weights1 = []  # input to hidden1
    # weights2 = []  # hidden1 to hidden2
    y = 0.0
    error = 0.0
    cost = 0.0
    '''
    weights1 = nn.w1(weights1)
    weights2 = nn.w2(weights2)
    bias1, bias2 = nn.bias(bias1, bias2)
    weights1, weights2, bias1, bias2 = test.w()'''

    for k in range(50):
        cost = 0.0
        f.seek(0, 0)
        for j in range(100000):
            count1 = f.readline()
            count = str()
            for i in range(len(count1) - 1):
                count += count1[i]
            count = count.split(',')
            l = []
            for i in range(len(count)):
                l.append(int(count[i]))
            # print(l)
            # print(l)
            inlayer = []
            for i in range(9):
                inlayer.append(l[i])
            t = l[9]
            # print(inlayer, t)

            hlayer1 = [0, 0, 0, 0, 0, 0, 0, 0]
            hlayer1 = nn.cal_hid(inlayer, weights1, hlayer1, bias1)
            y = nn.cal_out(hlayer1, weights2, bias2)
            error = nn.cal_error(y, t)
            if k == 49:
                errors1.append(error)
            cost += error
            weights1, weights2, bias1, bias2 = nn.Adjust_weights(inlayer, weights1, bias1, hlayer1, weights2, bias2, y, t)
            del (count, count1)
        print("Epoch ", k + 1, " : ")
        print("\tCost : ", cost)
        errors.append(cost)
    f.close()
    return weights1, weights2, bias1, bias2


def nn2(weights1, weights2, bias1, bias2):
    import neural_network as nn
    f = open('move2.txt', 'r')
    inlayer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # bias1 = []  # Bias between Input and Hidden Layer
    # bias2 = 0.0  # Bias between Hidden layer and Output
    olayerlayer = 0.0
    # weights1 = []  # input to hidden1
    # weights2 = []  # hidden1 to hidden2
    y = 0.0
    error = 0.0
    cost = 0.0
    '''
    weights1 = nn.w1(weights1)
    weights2 = nn.w2(weights2)
    bias1, bias2 = nn.bias(bias1, bias2)
    weights1, weights2, bias1, bias2 = test.w()'''

    for k in range(100):
        cost = 0.0
        f.seek(0, 0)
        for j in range(100000):
            count1 = f.readline()
            count = str()
            for i in range(len(count1) - 1):
                count += count1[i]
            count = count.split(',')
            l = []
            for i in range(len(count)):
                l.append(int(count[i]))
            # print(l)
            inlayer = []
            for i in range(9):
                inlayer.append(l[i])
            t = l[9]
            # print(inlayer, t)

            hlayer1 = [0, 0, 0, 0, 0, 0, 0, 0]
            hlayer1 = nn.cal_hid(inlayer, weights1, hlayer1, bias1)
            y = nn.cal_out(hlayer1, weights2, bias2)
            error = nn.cal_error(y, t)
            if k == 99:
                errors1.append(error)
            cost += error
            weights1, weights2, bias1, bias2 = nn.Adjust_weights(inlayer, weights1, bias1, hlayer1, weights2, bias2, y, t)
            del (count, count1)
        print("Epoch ", k + 1, " : ")
        print("\tCost : ", cost)
        errors.append(cost)
    return weights1, weights2, bias1, bias2


def nn3(weights1, weights2, bias1, bias2):
    import neural_network as nn
    f = open('move3.txt', 'r')
    inlayer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # bias1 = []  # Bias between Input and Hidden Layer
    # bias2 = 0.0  # Bias between Hidden layer and Output
    olayerlayer = 0.0
    # weights1 = []  # input to hidden1
    # weights2 = []  # hidden1 to hidden2
    y = 0.0
    error = 0.0
    cost = 0.0
    '''
    weights1 = nn.w1(weights1)
    weights2 = nn.w2(weights2)
    bias1, bias2 = nn.bias(bias1, bias2)
    weights1, weights2, bias1, bias2 = test.w()'''

    for k in range(500):
        cost = 0.0
        f.seek(0, 0)
        for j in range(94901):
            count1 = f.readline()
            count = str()
            for i in range(len(count1) - 1):
                count += count1[i]
            count = count.split(',')
            l = []
            for i in range(len(count)):
                l.append(int(count[i]))
            # print(l)
            inlayer = []
            for i in range(9):
                inlayer.append(l[i])
            t = l[9]
            # print(inlayer, t)

            hlayer1 = [0, 0, 0, 0, 0, 0, 0, 0]
            hlayer1 = nn.cal_hid(inlayer, weights1, hlayer1, bias1)
            y = nn.cal_out(hlayer1, weights2, bias2)
            error = nn.cal_error(y, t)
            if k == 499:
                errors1.append(error)
            cost += error
            weights1, weights2, bias1, bias2 = nn.Adjust_weights(inlayer, weights1, bias1, hlayer1, weights2, bias2, y, t)
            del (count, count1)
        print("Epoch ", k + 1, " : ")
        print("\tCost : ", cost)
        errors.append(cost)
    return weights1, weights2, bias1, bias2


def nn4(weights1, weights2, bias1, bias2):
    import neural_network as nn
    f = open('move4.txt', 'r')
    inlayer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # bias1 = []  # Bias between Input and Hidden Layer
    # bias2 = 0.0  # Bias between Hidden layer and Output
    olayerlayer = 0.0
    # weights1 = []  # input to hidden1
    # weights2 = []  # hidden1 to hidden2
    y = 0.0
    error = 0.0
    cost = 0.0
    '''
    weights1 = nn.w1(weights1)
    weights2 = nn.w2(weights2)
    bias1, bias2 = nn.bias(bias1, bias2)
    weights1, weights2, bias1, bias2 = test.w()'''

    for k in range(500):
        cost = 0.0
        f.seek(0, 0)
        for j in range(55763):
            count1 = f.readline()
            count = str()
            for i in range(len(count1) - 1):
                count += count1[i]
            count = count.split(',')
            l = []
            for i in range(len(count)):
                l.append(int(count[i]))
            # print(l)
            inlayer = []
            for i in range(9):
                inlayer.append(l[i])
            t = l[9]
            # print(inlayer, t)

            hlayer1 = [0, 0, 0, 0, 0, 0, 0, 0]
            hlayer1 = nn.cal_hid(inlayer, weights1, hlayer1, bias1)
            y = nn.cal_out(hlayer1, weights2, bias2)
            error = nn.cal_error(y, t)
            if k == 499:
                errors1.append(error)
            cost += error
            weights1, weights2, bias1, bias2 = nn.Adjust_weights(inlayer, weights1, bias1, hlayer1, weights2, bias2, y, t)
            del (count, count1)
        print("Epoch ", k + 1, " : ")
        print("\tCost : ", cost)
        errors.append(cost)
    return weights1, weights2, bias1, bias2


weights1, weights2, bias1, bias2 = test.w1()
weights1, weights2, bias1, bias2 = nn1(weights1, weights2, bias1, bias2)
print(weights1, '\n', weights2, '\n', bias1, '\n', bias2)
plt.figure(1)
plt.subplot(421)
plt.plot(errors)
plt.subplot(422)
plt.plot(errors1)

weights1, weights2, bias1, bias2 = test.w2()
weights1, weights2, bias1, bias2 = nn2(weights1, weights2, bias1, bias2)
print(weights1, '\n', weights2, '\n', bias1, '\n', bias2)
plt.subplot(423)
plt.plot(errors)
plt.subplot(424)
plt.plot(errors1)

weights1, weights2, bias1, bias2 = test.w3()
weights1, weights2, bias1, bias2 = nn3(weights1, weights2, bias1, bias2)
print(weights1, '\n', weights2, '\n', bias1, '\n', bias2)
plt.subplot(425)
plt.plot(errors)
plt.subplot(426)
plt.plot(errors1)

weights1, weights2, bias1, bias2 = test.w()
weights1, weights2, bias1, bias2 = nn4(weights1, weights2, bias1, bias2)
print(weights1, '\n', weights2, '\n', bias1, '\n', bias2)
plt.subplot(427)
plt.plot(errors)
plt.subplot(428)
plt.plot(errors1)

plt.show()