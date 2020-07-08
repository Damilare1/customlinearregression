from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)


def get_m(x, y):
    m = (
        ((mean(x)*mean(y)) - mean(x*y)) /
        (((mean(x))**2) - mean(x**2))
    )
    return m

def get_y_intercept(x, y, m):
    b = mean(y) - m*(mean(x))
    return b

slope = get_m(xs, ys)
intercept = get_y_intercept(xs, ys, slope)
new_y  = slope * xs + intercept

plt.scatter(xs, new_y)
plt.show()

