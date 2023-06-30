import numpy as np

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







# 1维列表切片
# list_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_A[1:3]) # 切取第2个数据到第3个数据 ： 中括号左边是取到而右边是取不到，右边需要减去1， 所以切取的实际上就是左边号码加上1而右边对应号码不变
# print(list_A[-9:9]) # 切取倒数第9个数据到正数第9个数据 ： 对于负数不需要加上1
# print(list_A[1:]) # 省略表示没有中止， 所以切到最后一个数据
# print(list_A[:3]) # 省略表示从开头开始切
# print(list_A.index(2)) # 找到第2个数据的元素，返回它的位置坐标，即1


# 2维数组切片，2维列表无法切片
list_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_B = [11, 12, 13]
# list1 = [list_A, list_B] # 将两个列表合并，不能用于2维切片
# list2 =  [list(t) for t in zip(list_A,list_B)] # 2个1维列表合并成一个2维列表，每一个1维列表依次各取1个合成一个1维列表放入2维列表中， 不能用于2维切片
# list3 = list_A + list_B # 2个1维列表直接顺次合并成一个大的1维列表， 不能用于2维切片
# list4 = [list_A] + [list_B] # 效果和list1一样
list5 = np.array(list(zip(list_A, list_B)))# 将2个1维列表转成2维数组， 每一个1维列表依次各取1个合成一个1维数组放入2维数组中
print(list5)
print(list5[:, 0]) # 取二维数组中所有行的第0个数据，即第1列数据， 输出1维数组
print(list5[0, :]) # 取二维数组中第0行的所有数据，即第0行数据， 输出1维数组
print(list5[:, 0:1]) # 取二维数组中第0列到1-1列数据， 输出2维数组




