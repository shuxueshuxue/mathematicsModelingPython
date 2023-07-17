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