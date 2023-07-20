#%% 数组的基本属性
import numpy as np

array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
array2 = np.array([['a','b']])
print(array1.shape) # 数组的形状, 输出(3,3)
print(array1.size) # 数组的大小, 输出9
print(array1.dtype) # 数组的类型, 输出int32
print(array2.dtype) # 数组的类型， 输出<U1
print(array1.ndim) # 数组的维数, 输出2
print(array2.ndim) # 数组的维数, 输出2




#%% 数组的数据预处理
import numpy as np

array3 = np.array([1, 2, 3, 4, 5])
array4 = np.array([1.1, 2.2, 3.3, 4.4, 5.3221])
float_array3 = array3.astype(np.float64) # 数组的类型转换, dtype类型从int64变成float64, astype不改变原本文件
int_array4 = array4.astype(np.int32) #数组的类型转换, dtype类型从float64变成int32

array5 = np.array([1, 2, np.nan, 4])
print(np.isnan(array5)) # 数组的缺失值处理，isnan判断一个元素是否是NaN(Not-a-Number), 是返回True, 否返回False
print(array5[np.isnan(array5)]) #false不显示，True返回对应的元素，本例中为nan
#由此我们可以成功找到缺失值的位置，便可以用赋值语句对缺失值赋值，语句如下
array5[np.isnan(array5)] = 0 # 将缺失值全部替换为0

array6 = [1,3,2,2,3,1,2,3]
print(np.unique(array6)) # 数组的重复值处理， unique函数将重复值删除，并且从小到大排序，字母则从a排到z

array7 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(array7.reshape(12)) # 数组的形状处理，输出1维数组
print(array7.reshape(12, 1)) # 数组的形状处理，输出2维数组
print(array7.reshape(1, 12)) # 数组的形状处理，输出2维数组






#%% 1维列表切片
list_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_A[1:3]) # 切取[1,3), 即第2个数据到第3个数据 ： 中括号左边是取到而右边是取不到，右边需要减去1， 所以切取的实际上就是左边号码加上1而右边对应号码不变
print(list_A[-9:9]) # 切取[-9,8], 即倒数第9个数据到正数第9个数据 ： 对于负数不需要加上1
print(list_A[1:]) # 省略表示没有中止， 所以切到最后一个数据
print(list_A[:3]) # 省略表示从开头开始切
print(list_A.index(2)) # 找到第2个数据的元素，返回它的位置坐标，即1



#%% 1维数组切片
import numpy as np

array_A = np.arange(10) # 省略了0，arange函数从0开始数到10-1, 输出1维数组
array_B = np.arange(10,13) # arange函数从10开始数到13-1， 输出1维数组
# [::n]表示间隔n个切取一个元素
print(np.arange(10)[:1])
print(np.arange(10)[:-1]) #切到到最后一个元素，但是最后一个元素取不到
print(np.arange(10)[::1])
print(np.arange(10)[::-1])
print(np.arange(10)[1:])
print(np.arange(10)[-1:])
print(np.arange(10)[1::])
print(np.arange(10)[-1::])



#%% 2维数组切片，2维列表无法切片
import numpy as np

list_C = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_D = [11, 12, 13]
list1 = [list_C, list_D] # 将两个列表合并，不能用于2维切片, 输出2维列表
list2 =  [list(t) for t in zip(list_C,list_D)] # 2个1维列表合并成一个2维列表，每一个1维列表依次各取1个合成一个1维列表放入2维列表中， 不能用于2维切片，输出2维列表
list3 = list_C + list_D # 2个1维列表直接顺次合并成一个大的1维列表， 不能用于2维切片，输出1维列表
list4 = [list_C] + [list_D] # 效果和list1一样
list5 = np.array(list(zip(list_C, list_D)))# 将2个1维列表转成2维数组， 每一个1维列表依次各取1个合成一个1维数组放入2维数组中，输出2维数组
print(list5)
print(list5[:, 0]) # 取二维数组中所有行的第0个数据，即第1列数据， 输出1维数组
print(list5[0, :]) # 取二维数组中第0行的所有数据，即第0行数据， 输出1维数组
print(list5[:, 0:1]) # 取二维数组中第0列到1-1列数据， 输出2维数组


# 另一个注意点
list_E = list_C
list_F = list_C[:]
list_C[0] = 10
print(list_E)
print(list_F)


#%% 3维数组切片
import numpy as np
# x[n,::]、x[:,n:]、x[::,n]、x[:,:,n]
# m:n看成一个整体，除了m:n之外的两个冒号就是用来表明在哪个维度上操作的
# 在双冒号的前面的(n)意味着切取三维数组的第0号维度上的第n号元素
# 在双冒号的中间的(n)意味着切取三维数组的第1号维度上的第n号元素
# 在双冒号的后面的(n)意味着切取三维数组的第2号维度上的第n号元素
# 其中n均可以替换成m:n，表示切取第m号到第n-1号元素，注意的是逐一切取每一号元素得一个2维数组，然后将这些2维数组合并成一个新的3维数组
# x[:, n:]是省略了最后一个冒号，相当于x[:, n::]或者是x[:,n:,:]
# n维数组同理


# Example(注：2维数组及以上的"::"和":"是等价的, ",:"可以省略)
b = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
              [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]],
              [[25, 26, 27, 28], [29, 30, 31, 32], [33, 34, 35, 36]],
              ])
print("b = ", b)
print(b.shape)
print("b[0, ::] = ",b[0, ::], b[0, ::].shape) # 切取b的第0号维度上的第0号元素，输出2维数组
print("b[1, ::] = ",b[1, ::], b[1, ::].shape) #切取b的第0号维度上的第1号元素，输出2维数组
print("b[0:2, ::] = ",b[0:2, ::], b[0:2, ::].shape) #切取b的第0号维度上的第0和1两号元素，两个元素都是一个2维数组，然后合并成一个3维数组。

print("b[0, :, :] = ",b[0, :, :], b[0, :, :].shape) # 等同于b[0, ::]

print("b[:, 0,:] = ",b[:, 0,:], b[:, 0, :].shape) # 切取b的第1号维度上的第0号元素，输出2维数组
print("b[:, 1,:] = ",b[:, 1,:], b[:, 1, :].shape) # 切取b的第1号维度上的第1号元素，输出2维数组
print("b[:, 0:2,:] = ",b[:, 0:2,:], b[:, 0:2,:].shape) # 切取b的第1号维度上的第0号到第2-1号元素，输出2维数组，不同于b[0:2, ::]的合并之后再输出.

print("b[:, 0:] = ",b[:, 0:], b[:, 0:].shape) # 切取b的全部元素，输出3维数组
print("b[:, 1:] = ",b[:, 1:], b[:, 1:].shape) # 切取b的第1号维度上除第0号外的所有元素，输出3维数组
print("b[:, -1:] = ",b[:, -1:], b[:, -1:].shape) # 切取b的第1号维度上最后一个位置的元素，仍然输出3维数组

print("b[::, 0] = ", b[:, 0], b[::, 0].shape) # 切取b的第1号维度上的第0号元素，输出2维数组
print("b[::, 1] = ", b[::, 1], b[::, 1].shape) # 切取b的第1号维度上的第1号元素，输出2维数组
print("b[::, -1] = ", b[::, -1], b[::, -1].shape) # 切取b的第1号维度上的最后一个元素，输出2维数组
print("b[::, 0:2] = ", b[::, 0:2], b[::, 0:2].shape) # 切取b的第1号维度上的第0号到第2-1号元素，输出3维数组，不同于合并之后再输出.

print("b[:, :, 0] = ", b[:, :, 0], b[:, :, 0].shape) #切取b的第2号维度的所有元素中的第0号元素，输出2维数组
print("b[:, :, 0:2] = ", b[:, :, 0:2], b[:, :, 0:2].shape) #切取b的第2号维度的所有元素中的第0号到第2-1号元素，输出3维数组，不同于合并之后再输出





#%% 数组的重塑(重塑、转置、合并)
import numpy as np

print(np.arange(8).reshape(2,4))
# reshape()函数用于在不更改数据的情况下为数组赋予新形状.
# 若用负数, 则表示模糊控制，负数可以为任何数。
# 比如`reshape(2,-1)`, 固定两行，多少列系统根据元素数量自动计算好；同理，`reshape(-2,2)`: 固定两列，行数自动计算好。
# 若出现了无法整除的情况，系统会报错


print(np.arange(8).reshape(2,4).T) # 数组的转置


array8 = np.array([[1, 2, 3], [4, 5, 6]])
array9 = np.array([[7, 8, 9], [10, 11, 12]])

print(np.concatenate([array8, array9])) # 省略的默认是axis=0, 纵向合并
print(np.vstack([array8, array9])) # v是vertical缩写，纵向合并
print(np.row_stack([array8, array9])) # 纵向合并

print(np.concatenate([array8, array9], axis=1)) # 横向合并
print(np.hstack([array8, array9])) # h是horizontal缩写，横向合并
print(np.column_stack([array8, array9])) # 横向合并





#%% 数组的条件函数与集合关系
import numpy as np

array10 = np.arange(10)
print(np.where(array10>5, 1, 0)) #where函数为条件函数，True返回1， False返回0


# 包含关系：np.inld(array1, array2)
# 交集关系 np.intersectld(array1, array2)
# 并集关系 np.unionld(array1, array2)
# 差集关系 np.setdiffld(array1, array2)




#%% 矩阵的运算
import numpy as np

array11 = np.random.rand(2,2)
print(array11)
print(np.mat(array11)) # 将数组变成矩阵

print(np.linalg.inv(array11))
print(np.linalg.inv(np.mat(array11))) # 矩阵求逆运算

eig_value, eigvector = np.linalg.eig(array11) # linalg.eig函数可以同时求解特征值和特征向量
print(eig_value)
print(eigvector)
