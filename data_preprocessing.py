import numpy as np



## *args形参的使用: 当传入多个位置参数，这多个位置参数会自动组成一个元组，然后就可以遍历这个元组中的参数
# def fun(*args):
#     print(type(args))
#     print(args)
#     for item in args:
#         print(item)
#
# fun(2, 'alex', [3])




## 在列表、元素、字典、集合和numpy的数组前加上星号 * 的含义: 将数据结构中元素都被分成一个一个的独立元素
# List = ['a', 2, 3]
# Tuple = ('b', 'c', 5)
# Dict = {'name': 'Ada', 'age': 23}
#
# print(List)
# print(Tuple)
# print(Dict)
#
# print(*List)
# print(*Tuple)
# print(*Dict)

# def print_item(*args):
#     print(type(args))
#     print(args)
#     for item in args:
#         print(item)
#
# List = ['apple', 23, 'orange', 9]
# print_item(List) # list这个元组只有一个元素
# print_item(*List) # 加上 * 之后， 直接把列表里面的元素取出来放到一个元组中， 然后直接遍历




## **kwargs形参的使用: 当传入多个关键字参数，这多个位置参数会自动组成一个字典，然后就可以遍历这个字典中的参数
# def fun(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     for key in kwargs.keys():
#         print(key, kwargs[key])
#
# fun(name='Alvin', age=23, things=[1, 2, 'a'])







# 1维列表切片
# list_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_A[1:3]) # 切取第2个数据到第3个数据 ： 中括号左边是取到而右边是取不到，右边需要减去1， 所以切取的实际上就是左边号码加上1而右边对应号码不变
# print(list_A[-9:9]) # 切取倒数第9个数据到正数第9个数据 ： 对于负数不需要加上1
# print(list_A[1:]) # 省略表示没有中止， 所以切到最后一个数据
# print(list_A[:3]) # 省略表示从开头开始切
# print(list_A.index(2)) # 找到第2个数据的元素，返回它的位置坐标，即1



# 1维数组
# array_A = np.arange(10) # 省略了0，arange函数从0开始数到10-1, 输出1维数组
# array_B = np.arange(10,13) # arange函数从10开始数到13-1， 输出1维数组
## [::n]表示间隔n个切取一个元素
print(np.arange(10)[:1])
print(np.arange(10)[:-1])
print(np.arange(10)[::1])
print(np.arange(10)[::-1])
print(np.arange(10)[1:])
print(np.arange(10)[-1:])
print(np.arange(10)[1::])
print(np.arange(10)[-1::])



# 2维数组切片，2维列表无法切片
list_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_B = [11, 12, 13]
# list1 = [list_A, list_B] # 将两个列表合并，不能用于2维切片, 输出2维列表
# list2 =  [list(t) for t in zip(list_A,list_B)] # 2个1维列表合并成一个2维列表，每一个1维列表依次各取1个合成一个1维列表放入2维列表中， 不能用于2维切片，输出2维列表
# list3 = list_A + list_B # 2个1维列表直接顺次合并成一个大的1维列表， 不能用于2维切片，输出1维列表
# list4 = [list_A] + [list_B] # 效果和list1一样
# list5 = np.array(list(zip(list_A, list_B)))# 将2个1维列表转成2维数组， 每一个1维列表依次各取1个合成一个1维数组放入2维数组中，输出2维数组
# print(list5)
# print(list5[:, 0]) # 取二维数组中所有行的第0个数据，即第1列数据， 输出1维数组
# print(list5[0, :]) # 取二维数组中第0行的所有数据，即第0行数据， 输出1维数组
# print(list5[:, 0:1]) # 取二维数组中第0列到1-1列数据， 输出2维数组

## 另一个注意点
# list_C = list_A
# list_D = list_A[:]
# list_A[0] = 10
# print(list_C)
# print(list_D)

# 3维数组切片
# x[n,::]、x[:,n:]、x[::,n]、x[:,:,n]
# m:n看成一个整体，除了m:n之外的两个冒号就是用来表明在哪个维度上操作的
# 在双冒号的前面的(n)意味着切取三维数组的第0号维度上的第n号元素
# 在双冒号的中间的(n)意味着切取三维数组的第1号维度上的第n号元素
# 在双冒号的后面的(n)意味着切取三维数组的第2号维度上的第n号元素
# 其中n均可以替换成m:n，表示切取第m号到第n-1号元素，注意的是逐一切取每一号元素得一个2维数组，然后将这些2维数组合并成一个新的3维数组
# x[:, n:]是省略了最后一个冒号，相当于x[:, n::]或者是x[:,n:,:]
# n维数组同理



## Example(注：2维数组及以上的"::"和":"是等价的, ",:"可以省略)
# b = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
#               [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]],
#               [[25, 26, 27, 28], [29, 30, 31, 32], [33, 34, 35, 36]],
#               ])
# print("b = ", b)
# print(b.shape)
# print("b[0, ::] = ",b[0, ::], b[0, ::].shape) # 切取b的第0号维度上的第0号元素，输出2维数组
# print("b[1, ::] = ",b[1, ::], b[1, ::].shape) #切取b的第0号维度上的第1号元素，输出2维数组
# print("b[0:2, ::] = ",b[0:2, ::], b[0:2, ::].shape) #切取b的第0号维度上的第0和1两号元素，两个元素都是一个2维数组，然后合并成一个3维数组。

# print("b[0, :, :] = ",b[0, :, :], b[0, :, :].shape) # 等同于b[0, ::]

# print("b[:, 0,:] = ",b[:, 0,:], b[:, 0, :].shape) # 切取b的第1号维度上的第0号元素，输出2维数组
# print("b[:, 1,:] = ",b[:, 1,:], b[:, 1, :].shape) # 切取b的第1号维度上的第1号元素，输出2维数组
# print("b[:, 0:2,:] = ",b[:, 0:2,:], b[:, 0:2,:].shape) # 切取b的第1号维度上的第0号到第2-1号元素，输出2维数组，不同于b[0:2, ::]的合并之后再输出.

# print("b[:, 0:] = ",b[:, 0:], b[:, 0:].shape) # 切取b的全部元素，输出3维数组
# print("b[:, 1:] = ",b[:, 1:], b[:, 1:].shape) # 切取b的第1号维度上除第0号外的所有元素，输出3维数组
# print("b[:, -1:] = ",b[:, -1:], b[:, -1:].shape) # 切取b的第1号维度上最后一个位置的元素，仍然输出3维数组

# print("b[::, 0] = ", b[:, 0], b[::, 0].shape) # 切取b的第1号维度上的第0号元素，输出2维数组
# print("b[::, 1] = ", b[::, 1], b[::, 1].shape) # 切取b的第1号维度上的第1号元素，输出2维数组
# print("b[::, -1] = ", b[::, -1], b[::, -1].shape) # 切取b的第1号维度上的最后一个元素，输出2维数组
# print("b[::, 0:2] = ", b[::, 0:2], b[::, 0:2].shape) # 切取b的第1号维度上的第0号到第2-1号元素，输出3维数组，不同于合并之后再输出.

# print("b[:, :, 0] = ", b[:, :, 0], b[:, :, 0].shape) #切取b的第2号维度的所有元素中的第0号元素，输出2维数组
# print("b[:, :, 0:2] = ", b[:, :, 0:2], b[:, :, 0:2].shape) #切取b的第2号维度的所有元素中的第0号到第2-1号元素，输出3维数组，不同于合并之后再输出




filepath = "example_of_txt_data.txt"

# read() 一次性读全部内容 ： 以字符串的形式返回结果
# with open(filepath, "r") as f:  # 打开文件
#     data = f.read()  # 读取文件
#     print(data)

# readline() 读取第一行内容 ： 以字符串的形式返回结果
# with open(filepath, "r") as f:
#     data = f.readline()
#     print(data)

# readlines() 列表 ： 读取文本所有内容，并且以数列的格式返回结果，一般配合for in使用
# with open(filepath, "r") as f:
#     data = f.readlines()
#     print(data)




# 写入txt文本
# with open("test.txt","w") as f:
#     f.write("这是个测试！") # 自带文件关闭功能，不需要再写f.close()




# 缩写字母含义汇总
# r : 读取文件，若文件不存在则会报错
# w: 写入文件，若文件不存在则会先创建再写入，会覆盖原文件
# a : 写入文件，若文件不存在则会先创建再写入，但不会覆盖原文件，而是追加在文件末尾
# rb,wb： 分别于r,w类似，但是用于读写二进制文件
# r+ : 可读、可写，文件不存在也会报错，写操作时会覆盖
# w+ : 可读，可写，文件不存在先创建，会覆盖
# a+ : 可读、可写，文件不存在先创建，不会覆盖，追加在末尾

# JFR - 那接下来应该是学 Pandas 了. 👻
