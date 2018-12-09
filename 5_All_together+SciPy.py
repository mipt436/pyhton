import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import minimize
from scipy.optimize import curve_fit


def polynom(x, coeffs):
    return sum([coeffs[i] * x ** i for i in range(len(coeffs))])


def true_func(x):
    return polynom(x, [2, -3, 2, 1])


def rel_error(a, b):
    return abs(a - b) / abs(b)


def loss_function(coeffs):
    C = 0
    loss = 0.0
    loss += sum((polynom(x, coeffs) - y_with_noise) ** 2)
    loss += C * sum(coeffs ** 2)
    return loss


fig = plt.figure()
ax1 = plt.subplot(121)
data_points = 500
xmax = 10

x = np.linspace(-xmax, xmax, data_points)
y = true_func(x)
y_with_noise = y + 50 * (np.random.randn(data_points))

approx_coeffs = minimize(loss_function,
                         np.array([0, 0, 0, 0]),
                         options={'disp': True})
print approx_coeffs
y_approx = polynom(x, approx_coeffs.x)

plt.plot(x, y_with_noise, label='noise', color='b')
plt.plot(x, y, label='true', color='g')
plt.plot(x, y_approx, label='approx', color='r')
plt.grid()
plt.legend()

ax2 = plt.subplot(122)
plt.plot(x, rel_error(y_approx, y), color='red', label='error, %')
plt.legend()
plt.grid()

plt.show()

