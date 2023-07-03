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
    # 下面x,y操作是将给定长度的二进制串压缩到目标区间X_BOUND, Y_BOUND.
    x = x_pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * (X_BOUND[1] - X_BOUND[0]) + X_BOUND[0]
    y = y_pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * (Y_BOUND[1] - Y_BOUND[0]) + Y_BOUND[0]
    return x, y


# 适应度函数
def get_fitness(pop):
    x, y = translateDNA(pop)
    pred = F(x, y)
    return (pred - np.min(pred)) + 1e-3  # 减去最小的适应度是为了防止适应度出现负数，通过这一步fitness的范围为[0, np.max(pred)-np.min(pred)],最后在加上一个很小的数防止出现为0的适应度


# 变异函数
def mutation(child, MUTATION_RATE=0.003): # MUTATION_RATE=0.003表示缺省值，即默认值
    if np.random.rand() < MUTATION_RATE:  # 以MUTATION_RATE的概率进行变异
        mutate_point = np.random.randint(0, DNA_SIZE * 2)  # 随机产生一个实数，代表要变异基因的位置
        child[mutate_point] = child[mutate_point] ^ 1  # 将变异点的二进制为反转, ^ 是按位异或运算符


# 交叉和变异函数
def crossover_and_mutation(pop, CROSSOVER_RATE=0.8):
    new_pop = []
    for father in pop:  # 遍历种群中的每一个个体，将该个体作为父亲
        child = father  # 孩子先得到父亲的全部基因（一串二进制串的那些0，1称为基因）
        if np.random.rand() < CROSSOVER_RATE:  # 产生子代时不是必然发生交叉，而是以一定的概率发生交叉
            mother = pop[np.random.randint(POP_SIZE)]  # 再种群中选择另一个个体，并将该个体作为母亲
            cross_points = np.random.randint(low=0, high=DNA_SIZE * 2)  # 随机产生交叉的点
            child[cross_points:] = mother[cross_points:]  # 孩子得到位于交叉点后的母亲的基因
        mutation(child)  # 每个后代有一定的机率发生变异
        new_pop.append(child)
    return new_pop




