import try1 as t1

t = 0.9
inlayer = [0.6, 0.8, 0]
hlayer = [0, 0, 0]
w1 = t1.w1()
w2 = t1.w2()
b1, b2 = t1.bias()
hlayer = t1.cal_hid(inlayer, w1, hlayer, b1)
print(hlayer)
y = t1.cal_out(hlayer, w2, b2)
print(y)
w1, w2, b1, b2 = t1.Adjust_weights(inlayer, w1, b1, hlayer, w2, b2, y, t)

