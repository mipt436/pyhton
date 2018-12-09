# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pylab
import math as m
from mpl_toolkits.mplot3d import Axes3D


def draw_elementary():
    x = np.linspace(-m.pi, m.pi, 1000)

    plt.title(u'Элементарные функции')

    y1 = np.sin(x)
    plt.plot(x, y1, label='$sin(x)$')

    y2 = np.exp(x)
    plt.plot(x, y2, label='$e^{x}$')

    y3 = x ** 2
    plt.plot(x, y3, label='$x^{2}$')

    plt.xlabel(u'Ось абсцисс')
    plt.ylabel(u'Ось оординат')

    plt.grid()
    plt.legend(loc='best')

    plt.savefig('elementary_functions.png')

    plt.show()


def draw_subplots():
    fig = plt.figure()

    ax1 = fig.add_subplot(221)
    ax1.set_title(u'Парабола')
    x = np.linspace(-3, 3, 1000)
    y = x ** 2
    plt.plot(x, y, label='$x^2$', color='r')
    plt.grid()
    plt.legend()

    ax2 = fig.add_subplot(222)
    ax2.set_title(u'Кубическая парабола')
    x = np.linspace(-3, 3, 1000)
    y = x ** 3
    plt.plot(x, y, label='$x^3$', color='b')
    plt.grid()
    plt.legend()

    ax3 = fig.add_subplot(223)
    ax3.set_title(u'Экспонента')
    x = np.linspace(-3, 3, 1000)
    y = np.exp(x)
    plt.plot(x, y, label='$e^x$', color='g')
    plt.grid()
    plt.legend()

    ax4 = fig.add_subplot(224)
    ax4.set_title(u'Логарифм')
    x = np.linspace(0.001, 3, 1000)
    y = np.log(x)
    plt.plot(x, y, label='$log(x)$', color='y')
    plt.grid()
    plt.legend()

    plt.show()


def draw_heatmap():
    def makeData():
        x = np.linspace(0, 0.5, 1000)
        y = np.linspace(0, 0.5, 1000)

        xgrid, ygrid = np.meshgrid(x, y)

        zgrid = 3 * xgrid * ygrid + xgrid - 2 * ygrid
        return xgrid, ygrid, zgrid

    x, y, z = makeData()

    fig = pylab.figure()
    axes = Axes3D(fig)

    axes.plot_surface(x, y, z)

    pylab.show()


# draw_elementary()
# draw_subplots()
draw_heatmap()
