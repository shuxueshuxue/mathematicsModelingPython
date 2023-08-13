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
print(dataframe4)
print(dataframe4.keys())
print(dataframe4.set_index(keys='时间')) # keys参数将索引改为就地索引(即不新建序列0,1,2,...)
print(dataframe4.head())
print(dataframe4.tail())
print(dataframe4.info()) # 显示information
print(dataframe4.describe()) # count为数据总数量，mean为均值，std为标准差，25%为25%分位数(即样本中所有数值从小到大排列在第25%的数据)





#%% 数据预处理————缺失值处理
import numpy as np
import pandas as pd

dataframe5 = pd.DataFrame({'编号': ['A1', 'A2', np.nan, 'A4'],
                           '年龄': [54, 16, np.nan, 4],
                           '性别': ['男', np.nan, np.nan, '男'],
                           '注册时间': ['2018/8/8', '2018/8/9', np.nan, '2018/8/11']})
print(dataframe5)
print(dataframe5.info())
print(dataframe5.isnull()) # isnull函数将缺失值显示为True, 非缺失值显示为False
print(dataframe5.dropna()) # dropna函数用于缺失值删除，默认是how='any', 即删除含有缺失值的整行和整列数据
print(dataframe5.dropna(axis=0)) # axis=0表示删除含有缺失值的整行数据
print(dataframe5.dropna(axis=1)) # axis=1表示删除含有缺失值的整列数据
print(dataframe5.dropna(how='all')) # how='all'表示若整行或者整列都缺失才删除

print(dataframe5.fillna(0)) # 将缺失值全部变成0， 但是不改变原本的文件, 想要改变的话需要使用语句datafram = dataframe5.fillna(0)
print(dataframe5.fillna({'编号': 'A', '性别': '男', '年龄': '40', '注册时间': '2018/8/10'})) # 将对应的列对应到字典的key, 然后将values填入缺失值




#%% 数据预处理————重复值处理
import pandas as pd

dataframe6 = pd.DataFrame({
    'order': ['A1', 'A2', 'A3', 'A3', 'A4', 'A4'],
    'name': ['Alice', 'Bob', 'Jack', 'Jack', 'Luna', 'Luna'],
    'code': [101, 102, 103, 103, 104, 104],
    'date': ['2018/8/8', '2018/8/9', '2018/8/10', '2018/8/10', '2018/8/11', '2018/8/12']})
print(dataframe6)
print(dataframe6.drop_duplicates(subset=['order'], keep='last')) # keep参数默认是保留第一个(即删除之后重复的)
print(dataframe6['code'].dtype)
print(dataframe6['code'].astype('float64')) # 将int64类型转换成float64, 但是不改变原本的文件, 想要改变的话需要使用语句datafram6['code'] = dataframe6['code'].astype('float64')





#%% 修改行或列标题名称
import pandas as pd

dataframe7 = pd.DataFrame({
    'code': [1, 2, 2, 4, 5, 5, 6],
    'name': ['a', 'a', 'b', 'c', 'd', 'd', 'e',],
    'value': [12, 14, 17, 20, 25, 26, 30]})
print(dataframe7)
print(dataframe7.set_index(['code', 'name'])) # 以code、name作为索引(称为层次化索引), 不改变原本文件
print(dataframe7.set_index(['code', 'name']).reset_index()) # 取消层次化索引，不改变原本文件
print(dataframe7.rename(columns={'order': 'new_order', 'name': 'new_name'})) # 修改列标题名称，不改变原有文件
print(dataframe7.rename(index={0: 'a', 1: 'b'})) # 修改行标题名称，不改变原本文件




#%% 数据选取(切片)
import pandas as pd

dataframe8 = pd.DataFrame({
    'code': [1, 2, 2, 4, 5, 5, 6],
    'name': ['a', 'a', 'b', 'c', 'd', 'd', 'e',],
    'frequency': [2, 3, 4, 2, 1, 4, 5],
    'value': [12, 14, 17, 20, 25, 26, 30]},
    index=['一', '二', '三', '四', '五', '六', '七'])
print(dataframe8['code']) # 选取一列数据
print(dataframe8[['name', 'value']]) # 选取多列数据
print(dataframe8.iloc[:, 1:3]) # 选取标号为1到标号为3-1的列(即从第0列开始计算， 选取第一列到第3-1列)

print(dataframe8.loc['二']) # 选取一行数据
print(dataframe8.loc[['二', '六']]) # 选取多行数据
print(dataframe8.iloc[1:3, :]) # 选取标号为1到标号为3-1的行(即从第0行开始计算， 选取第一行到第3-1行)

print(dataframe8.loc[['一', '五'], ['name', 'frequency']]) # loc选取指定行列数据
print(dataframe8.iloc[[0, 1], [2, 3]]) # iloc选取指定行列数据



dataframe9 = pd.read_csv(r'data of data_preprocessing\\行业指数pe_ttm.CSV', engine='python', skiprows=1, encoding='gbk')
print(dataframe9)

print(dataframe9['时间'].dtype)
dataframe9['时间'] = dataframe9['时间'].astype('datetime64') # 将时间这一列的数据类型(dtype)从object转换成datetime64, 改变了原本文件
print(dataframe9['时间'].dtype)
print(dataframe9[dataframe9['时间'] > '2019-02-01']) # 也可以写成'2019/2/1'

print(dataframe9[dataframe9['全指金融'] > 10])
print(dataframe9[dataframe9['全指金融'] > 10]['时间'])
print(dataframe9[dataframe9['全指金融'] > 10][['时间', '全指材料']])





#%% 数据修改(替换)
dataframe10 = pd.DataFrame({
    'code': [1, 2, 2, 4, 5, 5, 6],
    'name': ['a', 'a', 'b', 'c', 'd', 'd', 'e',],
    'frequency': [2, 3, 4, 2, 1, 4, 5],
    'value': [12, 14, 17, 20, 25, 26, 30]},
    index=['一', '二', '三', '四', '五', '六', '七'])
print(dataframe10['value'].replace(17, 0)) # 将datafram10中value列的17改为0, 但是不修改原本文件， 想要改变需要使用语句dataframe10['value'] = dataframe10['value'].replace(17, 0)
print(dataframe10['value'].replace(17, 0, inplace=True)) # inplace参数可以实现修改原本文件
print(dataframe10['value'].replace([17, 20], 0)) # 修改一列中的多个数据(多对一)
print(dataframe10.replace({'a': 'A', 'b': 'B'})) # 利用字典将数据表的指定数据(多对多)进行修改，默认是不修改原本文件




#%% 数据排序
import numpy as np
import pandas as pd

dataframe11 = pd.read_csv(r'data of data_preprocessing\\行业指数pe_ttm.CSV', engine='python', skiprows=1, encoding='gbk')

print(dataframe11.sort_values(by='全指金融', ascending=False)) # 按照金指金融这一列进行降序排序, ascending默认为True(即升序排序)
dataframe11.iloc[3:10, 3:10] = np.nan
print(dataframe11)
print(dataframe11.sort_values(by='全指金融', ascending=False, na_position='last')) #把缺失值排在最后面
print(dataframe11.sort_values(by=['全指金融', '全指工业'], ascending=[False, True], na_position='last'))

dataframe11 = dataframe11.set_index('时间')
print(dataframe11)
print(dataframe11.rank()) # rank通过“为各组分配一个平均排名”的方式破坏平级关系
print(dataframe11.rank() / len(dataframe11)) # len(dataframe11)为dataframe11的行数(不包括标题)




#%% 数据删除
import pandas as pd

dataframe12 = pd.DataFrame({
    'code': [1, 2, 2, 4, 5, 5, 6],
    'name': ['a', 'a', 'b', 'c', 'd', 'd', 'e',],
    'frequency': [2, 3, 4, 2, 1, 4, 5],
    'value': [12, 14, 17, 20, 25, 26, 30]},
    index=['一', '二', '三', '四', '五', '六', '七'])
print(dataframe12.drop(['frequency', 'value'], axis=1)) # 默认是axis=0(即竖着的方向)，不改变原本文件
print(dataframe12.drop(['一', '五']))
print(dataframe12[dataframe12['value'] >= 20])



#%% 总数量统计、唯一值获取、查找数据
import pandas as pd

dataframe13 = pd.read_excel(r'data of data_preprocessing\\个股及其行业数据.xlsx')
print(dataframe13)
print(dataframe13['industry_sw'].value_counts()) # .value_counts()对industry_sw这一列进行总数量统计
print(dataframe13['industry_sw'].unique()) # .unique()获取唯一值，生成一维数组(array)
print(dataframe13['name'].isin(['平安银行'])) # isin()查找对应数据, 找到返回True，没找到返回False
print(dataframe13[dataframe13['name'].isin(['平安银行'])]) # 利用isin()可进一步选取只包含想要查找对象的数据




#%% 分箱操作(即区间划分)
import pandas as pd

dataframe14 = pd.read_excel(r'data of data_preprocessing\\个股及其行业数据.xlsx')
pe_min = dataframe14['pe_ttm'].min()
pe_max = dataframe14['pe_ttm'].max()
bins = [pe_min, 0, 20, 60, 100, pe_max]
ca_pe = pd.cut(dataframe14['pe_ttm'], bins, labels=['垃圾股', '价值股', '成长股', '高估值', '泡沫股']) # .cut()对数据进行分箱
# print(ca_pe)
# print(ca_pe.value_counts()) # .value_counts()进行总数量统计
# print(pd.qcut(dataframe14['pe_ttm'], 5))
print(pd.qcut(dataframe14['pe_ttm'], 5).value_counts())
# .qcut用于对很大的数据集进行分箱操作, 分箱的依据不是单纯的等宽箱体或者没有确定的分解值，而是按照分位数进行分箱，比如前四分之一的是一个箱体这种要求



# Example of .cut() and .qcut()
ll = [1,2,3,5,3,4,1,2]
print('- - - pd.cut()示例1 - - -')
print(pd.cut(ll, 4, precision=2).value_counts()) # precision参数表示精度(即区间边界值保留的小数点位数)
print('- - - pd.cut()示例2 - - -')
print(pd.cut(ll, [1,2,4], precision=2).value_counts())
print('- - - pd.qcut()示例 - - -')
print(pd.qcut(ll, 4, precision=2).value_counts())




#%% 转置、插入新的行或列、索引重塑、长宽表转换
import pandas as pd

dataframe15 = pd.DataFrame({
    'A1': [1, 2, 2],
    'A2': [2, 3, 1],
    'A3': [7, 3, 2]},
    index=['一', '二', '三'])
# print(dataframe15)
# print(dataframe15.T) # 数据表行列互换(即转置)

# dataframe15.insert(loc=0, column='haha', value=6) # .insert()插入新的行或列
# print(dataframe15)
# print(dataframe15.stack()) # 利用.stack()进行索引重塑，将每一行叠起来， .unstack()为反向操作(比如初始数据为好几年的股票数据，将每一种股票的数据用.unstack()按年份反向铺开)

dataframe16 = pd.read_excel(r'data of data_preprocessing\\2015_2017年A股公司净利润增长率.xlsx', skipfooter=2)
# dataframe17 = dataframe16.set_index(['code', 'name'])
# print(dataframe17.stack().reset_index()) # 将3列的数据合并成1列

# 长宽表转换函数： .stack() .reset_index() .melt() .pivot_table()
dataframe17 = dataframe16.melt(id_vars=['code', 'name'], var_name=['year'], value_name='yoy') # 利用.melt()生成长表
print(dataframe17)
print(dataframe17.pivot_table(index=['code', 'name'], columns=['year'], values=['yoy'])) # 利用.pivot_table()生成宽表





#%% .apply()函数
import pandas as pd

def plusone(x):
    return x + 1

dataframe18 = pd.DataFrame({
    'A1': [1, 2, 2],
    'A2': [2, 3, 1],
    'A3': [7, 3, 2]},
    index=['一', '二', '三'])
print(dataframe18.apply(plusone)) # 将函数作用到每一个数值单元格
print(dataframe18.apply(sum)) # sum为python内置函数




#%% 算术运算、比较运算、汇总运算(计数、和、均值、最大值、最小值、中位数、众数、方差、标准差和分位数)
import numpy as np
import pandas as pd

dataframe19 = pd.DataFrame({
    'A1': [1, 2, 2],
    'A2': [2, 3, 1],
    'A3': [7, 3, 2]},
    index=['一', '二', '三'])
print(dataframe19)
print(dataframe19['A1'] + dataframe19['A3']) # 两列相加运算
print(dataframe19['A1'] > dataframe19['A3']) # 两列比较运算
print(dataframe19.count()) # 每一列计数，返回int64
print(dataframe19.sum()) # 每一列求和，返回int64
print(dataframe19.mean()) # 每一列求均值，返回float64
print(dataframe19.max()) # 每一列求最大值，返回int64
print(dataframe19.min()) # 每一列求最小值，返回int64
print(dataframe19.median()) # 每一列求中位数，返回float64
#print(dataframe19.mode()) # 每一列求众数
print(dataframe19.var()) # 每一列求方差，返回float64
print(dataframe19.std()) # 每一列求标准差，返回float64
print(dataframe19.quantile(0.1)) # 每一列求前10%分位数，返回float64(p分位数计算两者方法：1.(n+1)p 2. 1+(n-1)p)
print(dataframe19.quantile(np.arange(1, 11) / 10)) # 每一列求前10%、前20%、前60%分位数





#%% 相关性计算
import pandas as pd

dataframe20 = pd.read_excel(r'data of data_preprocessing\\行业指数.xlsx', skiprows=1)
print(dataframe20.corr()) # 相关性计算
print(dataframe20['全指医药'].corr(dataframe20['全指消费'])) # 计算全指医药和全指消费的相关性系数



#%% 获取当前时间
from datetime import datetime
from dateutil.parser import parse

print(datetime.now())
print(datetime.now().date())
print(datetime.now().day)
x = datetime.now() # 输出的类型(type)为datetime.datetime
y = x.strftime('%Y-%m-%d   %H:%M:%S') # 输出的类型(type)为str
z = parse(y)
print()
print(type(x))
print(type(y))
print(type(z))
print()
print(x)
print(y)
print(z)




#%% 时间索引和时间运算
import numpy as np
import pandas as pd

index = pd.DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04'])
dataframe21 = pd.DataFrame(np.arange(4), columns=['num'], index=index)
print(dataframe21)

dataframe22 = pd.read_csv(r'data of data_preprocessing\\行业指数pe_ttm.CSV', engine='python', skiprows=1, encoding='gbk')
print(dataframe22)
dataframe22['时间'] = dataframe22['时间'].astype('datetime64') # 将type从object变成datetime64
dataframe22.set_index('时间', inplace=True)
dataframe22.sort_index(inplace=True) # 按时间升序排列
print(dataframe22['2018-01':'2019-01'])