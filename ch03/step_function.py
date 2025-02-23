# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    return np.array(x > 0, dtype=int)

X = np.arange(-5.0, 5.0, 0.1) # 在-5.0  到5.0范围内，以0.1为步长，生成一个数组[-5.0, -4.9, -4.8, -4.7, -4.6, -4.5, -4.4, -4.3, -4.2, -4.1, -4.0, -3.9, -3.8, -3.7, -3.6, -3.5, -3.4, -3.3, -3.2]
Y = step_function(X) # 将X数组，通过阶跃函数转换为数组Y
plt.plot(X, Y) # 绘制X和Y的图像
plt.ylim(-0.1, 1.1)  # 指定图中绘制的y轴的范围
plt.show()
