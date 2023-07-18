#%% 构建序列(Series数据结构)
import pandas as pd


print(pd.Series(['a', 'b', 'c', 'd'])) # 输出带索引标签的一组数据，索引标签默认是0, 1, 2, ...
print()
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(pd.Series(dictionary)) # 将字典输出成带索引标签的一组数据，索引标签为字典的键(key)
print()
print(pd.Series(['a', 'b', 'c', 'd'])[0]) # 输出第一行索引标签对应的元素
print()
print(pd.Series(['a', 'b', 'c', 'd'])[[0,1]]) # 输出第一、二行
print()
print(pd.Series([1,3,4,5,7,8,9], index=['A', 'B', 'C', 'D', 'E', 'F', 'G'])) # 通过index指定输出索引标签
print()
print(pd.Series([1,3,4,5,7,8,9], index=['A', 'B', 'C', 'D', 'E', 'F', 'G']).head()) # head(n)函数代表的意思是显示前多少行，可以指定显示的行数，不写n默认是前5行
print()
print(pd.Series([1,3,4,5,7,8,9], index=['A', 'B', 'C', 'D', 'E', 'F', 'G']).tail()) # tail(n)函数代表的意思是显示后多少行，可以指定显示的行数，不写n默认是后5行
print()
print(pd.Series([1,3,4,5,7,8,9], index=['A', 'B', 'C', 'D', 'E', 'F', 'G']).index) # 输出对应的index
print()
print(pd.Series([1,3,4,5,7,8,9], index=['A', 'B', 'C', 'D', 'E', 'F', 'G']).values) # 输出对应的values





#%% 构建表格(DataFrame数据结构)
import numpy as np
import pandas as pd


print(pd.DataFrame(['a', 'b', 'c', 'd']))
print()
print(pd.DataFrame(np.array(['a', 'b', 'c', 'd']))) # 用numpy模块的array函数效果一样
print()
print(pd.DataFrame([['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D']]))
print()
print(pd.DataFrame(np.array([['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D']]))) # 用numpy模块的array函数效果一样
print()

dataframe1 = pd.DataFrame(np.array([['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D']]),
                   columns=['lowercase', 'uppercase'],
                   index=['一', '二', '三', '四']) # 修改列名和行名
print(dataframe1)
print(dataframe1.index)
print(dataframe1.values)
print(dataframe1.columns)
print()

data = {'lowercase': ['a', 'b', 'c', 'd'], 'uppercase': ['A', 'B', 'C', 'D']} # 创建字典
print(pd.DataFrame(data, index=[3, 4, 5, 6])) # 通过字典来创建表格






#%% 读取数据
import pandas as pd

dataframe2 = pd.read_table(r'data of data_preprocessing\\pe_ttm.txt', header=None) # 读取txt文件, header默认将数据集的第一行用作表头
# print(dataframe2)
dataframe3 = pd.read_excel(r'data of data_preprocessing\\行业指数.xlsx', skiprows=1) # 读取excel文件
# print(dataframe3)
dataframe4 = pd.read_csv(r'data of data_preprocessing\\行业指数pe_ttm.CSV', engine='python', skiprows=1, encoding='gbk')
# print(dataframe4)
# print(dataframe4.head())
# print(dataframe4.tail())
print(dataframe4.info()) # 显示information
print(dataframe4.describe()) # count为数据总数量，mean为均值，std为标准差，25%为25%分位数(即样本中所有数值从小到大排列在第25%的数据)





#%% 数据预处理(缺失值、重复值、异常值处理)
import numpy as np
import pandas as pd

## 缺失值处理
dataframe5 = pd.DataFrame({'编号': ['A1', 'A2', np.nan, 'A4'],
                           '年龄': [54, 16, np.nan, 4],
                           '性别': ['男', np.nan, np.nan, '男'],
                           '注册时间': ['2018/8/8', '2018/8/9', np.nan, '2018/8/11']})
# print(dataframe5)
# print(dataframe5.info())
# print(dataframe5.isnull()) # isnull函数将缺失值显示为True, 非缺失值显示为False
# print(dataframe5.dropna()) # dropna函数用于缺失值删除，默认是how='any', 即删除含有缺失值的整行和整列数据
# print(dataframe5.dropna(axis=0)) # axis=0表示删除含有缺失值的整行数据
# print(dataframe5.dropna(axis=1)) # axis=1表示删除含有缺失值的整列数据
# print(dataframe5.dropna(how='all')) # how='all'表示若整行或者整列都缺失才删除

print(dataframe5.fillna(0)) # 将缺失值全部变成0， 但是不改变原本的文件, 想要改变的话需要使用语句datafram = dataframe5.fillna(0)
print(dataframe5.fillna({'编号': 'A', '性别': '男', '年龄': '40', '注册时间': '2018/8/10'})) # 将对应的列对应到字典的key, 然后将values填入缺失值


## 重复值处理
dataframe6 = pd.DataFrame({'order': ['A1', 'A2', 'A3', 'A3', 'A4', 'A4'],
                           'name': ['Alice', 'Bob', 'Jack', 'Jack', 'Luna', 'Luna'],
                           'code': [101, 102, 103, 103, 104, 104],
                           'date': ['2018/8/8', '2018/8/9', '2018/8/10', '2018/8/10', '2018/8/12']})


