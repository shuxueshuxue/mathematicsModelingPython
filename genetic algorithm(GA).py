## 用GA求解Rosenbrock函数(香蕉函数)的极大值, f(x, y) = 100(x^2 - y) ** 2 + (1 - x) ** 2, -2.048 ≤ x, y ≤ 2.048


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

DNA_SIZE = 24
POP_SIZE = 80
CROSSOVER_RATE = 0.6
MUTATION_RATE = 0.01
N_GENERATIONS = 100
X_BOUND = [-2.048, 2.048]
Y_BOUND = [-2.048, 2.048]

print(*X_BOUND)


def F(x,y):
    return 100.0 * (y - x ** 2.0) ** 2.0 + (1 - x) ** 2.0

def plot_3d(ax):
    X = np.linspace(*X_BOUND, 100) # numpy.linspace函数用于在线性空间中以均匀步长生成数字序列
    Y = np.linspace(*Y_BOUND, 100)
    X, Y = np.meshgrid(X, Y) # 生成网格点坐标矩阵
    Z = F(X, Y)
    ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = cm.coolwarm) # 绘制3D图形，rstride设置行的跨度，cstride设置列的跨度，cmap设置颜色映射
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.pause(3) # plt.pause函数用于暂停每次更新的时间，并在更新网络图像后清除旧的图像。这样可以创建一个伪动态效果，因为它实际上是一系列静态图像
    plt.show

def translateDNA(pop): # pop为种群矩阵，一行表示一个二进制编码表示的DNA，矩阵的行数为种群的数量
    x_pop = pop[:, 0:DNA_SIZE]
    y_pop = pop[:, DNA_SIZE:]
    x = x_pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * (X_BOUND[1] - X_BOUND[0]) + ...



