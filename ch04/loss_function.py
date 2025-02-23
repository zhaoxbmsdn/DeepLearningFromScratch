import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta)); # delta是避免log(0)的取值 np.log(0)值为负无限大-inf

def softmax_loss(a, t):
    batch_size = a.shape[0]
    return -np.sum(np.log(a[np.arange(batch_size), t] + 1e-7)) / batch_size

