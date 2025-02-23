# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))    

# X = np.arange(-0.1, 1.1, 0.1)
# Y = sigmoid(X)
# plt.plot(X, Y)
# plt.ylim(-0.1, 1.1)
# plt.show()

def e(x):
    return np.exp(x)

X = np.arange(-10.0, 10.0, 0.1)
Y = e(X)
plt.plot(X, Y)
plt.ylim(-10.0, 10.0)
plt.show()