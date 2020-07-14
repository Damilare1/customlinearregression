from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)

def get_y_intercept_and_m(x, y):
    m = (
        ((mean(x)*mean(y)) - mean(x*y)) /
        (((mean(x))**2) - mean(x**2))
    )
    b = mean(y) - m*(mean(x))
    return m, b

def squared_error(ys_orig, ys_line):
    return sum((ys_line-ys_orig)**2)

def coefficient_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regression = squared_error(ys_orig, ys_line)
    squared_error_mean = squared_error(ys_orig, y_mean_line)

    return 1-(squared_error_regression/squared_error_mean)

slope, intercept = get_y_intercept_and_m(xs, ys)
regression_line = [(slope*x)+intercept for x in xs]

r_squared = coefficient_of_determination(ys, regression_line)

print(r_squared)

#predict_x = 10.0
#predict_y = (slope*predict_x) + intercept

#plt.scatter(xs, ys)
#plt.scatter(predict_x, predict_y)

#plt.plot(xs, regression_line)
#plt.show()
