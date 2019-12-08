import neural_network as nn
from matplotlib import pyplot as plt
import test

f = open('New Text Document (7).txt', 'r')

# inlayer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
bias1 = []      # Bias between Input and Hidden Layer
bias2 = []      # Bias between Hidden layer and Output
olayer = 0.0
weights1 = []   # input to hidden1
weights2 = []   # hidden1 to hidden2
y = 0.0
error = 0.0
cost = 0.0
errors = []
errors1 = []

weights1 = nn.w1(weights1)
weights2 = nn.w2(weights2)
bias1, bias2 = nn.bias(bias1, bias2)
# weights1, weights2, bias1, bias2 = test.w()

for k in range(50000):
    cost = 0.0
    f.seek(0, 0)
    for j in range(1252):
        count1 = f.readline()
        count = str()
        for i in range(len(count1)-1):
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
        y, olayer = nn.cal_out(hlayer1, weights2, y, bias2)
        error = nn.cal_error(y, t)
        if k == 49999:
            errors1.append(error)
        cost += error
        weights1, weights2, bias1, bias2 = nn.Adjust_weights(inlayer, weights1, bias1, hlayer1, weights2, bias2, y, t)
        del (count, count1)
    print("Epoch ", k, " : ")
    print("Cost : ", cost)
    errors.append(cost)
    if k % 10 == 0:
        print(weights1, '\n', weights2, '\n', bias1, '\n', bias2)

plt.figure(1)
plt.subplot(211)
plt.plot(errors)
plt.subplot(212)
plt.plot(errors1)
plt.show()
print(weights1, '\n', weights2, '\n', bias1, '\n', bias2)