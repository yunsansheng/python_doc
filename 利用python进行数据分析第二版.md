引入惯例

```
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm
```

# Numpy

## 1. arange 列表

```python
my_list = list(range(1000000))
my_arr = np.arange(1000000)
```

## 2. ndarray 多维数组简介

```python
data = np.random.randn(2, 3)

In [12]: import numpy as np

# Generate some random data
In [13]: data = np.random.randn(2, 3)

In [14]: data
Out[14]: 
array([[-0.2047,  0.4789, -0.5194],
       [-0.5557,  1.9658,  1.3934]])

In [15]: data * 10
In [16]: data + data 

In [17]: data.shape
Out[17]: (2, 3)

In [18]: data.dtype
Out[18]: dtype('float64')
```

## 3. ndarray

### 创建ndarray

```python
1. 使用array函数
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)

data3 = [[1, 2, 3, 4], [5, 6, 7, 8,9]]
arr3 = np.array(data3)
#array([list([1, 2, 3, 4]), list([5, 6, 7, 8, 9])], dtype=object)

In [25]: arr2.ndim
Out[25]: 2

In [26]: arr2.shape  
Out[26]: (2, 4)  #arr1.shape(5,)
    
In [17]: arr2.dtype
Out[17]: dtype('int64')
  
np.zeros(10)
np.zeros((3, 6))
#由于NumPy关注的是数值计算，因此，如果没有特别指定，数据类型基本都是float64（浮点数)

np.eye(10) == np.identity(10)

#你可以通过ndarray的astype方法明确地将一个数组从一个dtype转换成另一个dtype：
In [37]: arr = np.array([1, 2, 3, 4, 5])
In [39]: float_arr = arr.astype(np.float64)
In [40]: float_arr.dtype
Out[40]: dtype('float64')
#笔记：调用astype总会创建一个新的数组（一个数据的备份），即使新的dtype与旧的dtype相同。    
```

### 数组运算

```python
#大小相等的数组之间的任何算术运算都会将运算应用到元素级
In [51]: arr = np.array([[1., 2., 3.], [4., 5., 6.]])

In [52]: arr
Out[52]: 
array([[ 1.,  2.,  3.],
       [ 4.,  5.,  6.]])

In [53]: arr * arr
Out[53]: 
array([[  1.,   4.,   9.],
       [ 16.,  25.,  36.]])
#不同大小的数组之间的运算叫做广播（broadcasting）

基本的索引和切片
In [60]: arr = np.arange(10)

In [61]: arr
Out[61]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [62]: arr[5]
Out[62]: 5

In [63]: arr[5:8]
Out[63]: array([5, 6, 7])

In [64]: arr[5:8] = 12 # 批量赋值

In [65]: arr
Out[65]: array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])
#数组切片是原始数组的视图。这意味着数据不会被复制，视图上的任何修改都会直接反映到源数组上。

arr_slice = arr[5:8]
#我修稿arr_slice中的值，变动也会体现在原始数组arr中
arr_slice[:] = 64 #切片[ : ]会给数组中的所有值赋值

#注意：如果你想要得到的是ndarray切片的一份副本而非视图，就需要明确地进行复制操作，例如arr[5:8].copy()

#可以对各个元素进行递归访问，你可以传入一个以逗号隔开的索引列表来选取单个元素。也就是说，下面两种方式是等价的：
In [74]: arr2d[0][2]
Out[74]: 3

In [75]: arr2d[0, 2]
Out[75]: 3
    
#你可以一次传入多个切片，就像传入多个索引那样 如前两行，每行去除第一个
In [92]: arr2d[:2, 1:]
Out[92]: 
array([[2, 3],
       [5, 6]])

#arr2d[:, :1] 所有行
```

### 布尔型索引

```python
In [36]: names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

In [37]: data = np.random.randn(7, 4)

In [38]: names
Out[38]: array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'], dtype='<U4')

In [39]: data
Out[39]: 
array([[-1.28094306,  0.22443958, -0.72829024, -0.65421242],
       [ 0.76700128,  0.90503752,  0.90887145,  0.50170408],
       [ 2.09725609,  0.75188075, -0.18841508, -2.2570084 ],
       [-1.04108276, -0.92723638, -0.08526999,  0.50544112],
       [ 0.02961374, -1.50935888,  1.48222305,  1.0115633 ],
       [-0.56025129, -0.29855465,  0.68972887,  0.00423075],
       [-0.30038172,  2.21520797,  0.61505429,  0.29316577]])

In [40]: names == 'Bob'
Out[40]: array([ True, False, False,  True, False, False, False])

In [41]: data[names == 'Bob']
Out[41]: 
array([[-1.28094306,  0.22443958, -0.72829024, -0.65421242],
       [-1.04108276, -0.92723638, -0.08526999,  0.50544112]])
# 布尔型数组的长度必须跟被索引的轴长度一致。此外，还可以将布尔型数组跟切片、整数（或整数序列，稍后将对此进行详细讲解）混合使用：

#要选择除"Bob"以外的其他值，既可以使用不等于符号（!=），也可以通过~对条件进行否定
data[names != 'Bob']
data[~(names == 'Bob')]

cond = names == 'Bob'
data[~cond]
使用&（和）、|（或）之类的布尔算术运算符即可：
mask = (names == 'Bob') | (names == 'Will')
#通过布尔型索引选取数组中的数据，将总是创建数据的副本，即使返回一模一样的数组也是如此。
#Python关键字and和or在布尔型数组中无效。要使用&与|。

#将所有负值变成0
data[data < 0] = 0
data[names != 'Joe'] = 7
```

### 花式索引

```python
arr = np.array([[ 0.,  0.,  0.,  0.],
       [ 1.,  1.,  1.,  1.],
       [ 2.,  2.,  2.,  2.],
       [ 3.,  3.,  3.,  3.],
       [ 4.,  4.,  4.,  4.],
       [ 5.,  5.,  5.,  5.],
       [ 6.,  6.,  6.,  6.],
       [ 7.,  7.,  7.,  7.]])
#为了以特定顺序选取行子集，只需传入一个用于指定顺序的整数列表或ndarray即可：
In [56]: arr[[4, 3, 0, 6]] #注意和切片不一样，切片是arr2d[0, 2]
Out[56]: 
array([[4., 4., 4., 4.],
       [3., 3., 3., 3.],
       [0., 0., 0., 0.],
       [6., 6., 6., 6.]])

arr = np.arange(32).reshape((8, 4))

array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23],
       [24, 25, 26, 27],
       [28, 29, 30, 31]])
In [124]: arr[[1, 5, 7, 2], [0, 3, 1, 2]]
Out[124]: array([ 4, 23, 29, 10])
#最终选出的是元素(1,0)、(5,3)、(7,1)和(2,2)。无论数组是多少维的，花式索引总是一维的
#花式索引跟切片不一样，它总是将数据复制到新数组中。
```

### 数组转置和轴对换

```python
#转置是重塑的一种特殊形式，它返回的是源数据的视图（不会进行任何复制操作）。数组不仅有transpose方法，还有一个特殊的T属性
arr = np.arange(15).reshape((3, 5))
arr
arr.T
np.dot(arr.T, arr)
```

## 4.通用函数

```python
#一元（unary）ufunc 接受一个数组
np.sqrt(arr)
np.exp(arr)

#二元（binary）ufunc 接受两个数组
x = np.random.randn(8)
y = np.random.randn(8)
np.maximum(x,y)

#Ufuncs可以接受一个out可选参数，这样就能在数组原地进行操作：
np.sqrt(arr)  #不改变原数组
np.sqrt(arr，arr) #改变原数组 

```

## 5. 利用数组进行数据处理

```python
points = np.arange(-5, 5, 0.01) # 1000 equally spaced point
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)

import matplotlib.pyplot as plt

#将条件逻辑表述为数组运算
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
#cond中的值选取xarr和yarr的值：当cond中的值为True时，选取xarr的值，否则从yarr中选取。
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
#缺点1.速度慢2.无法用于多维数组，可以用以下方法代替
result = np.where(cond, xarr, yarr)
#np.where的第二个和第三个参数不必是数组，它们都可以是标量值。在数据分析工作中，where通常用于根据另一个数组而产生一个新的数组。假设有一个由随机数据组成的矩阵，你希望将所有正值替换为2，将所有负值替换为－2。
arr = np.random.randn(4, 4)
np.where(arr > 0, 2, -2)
#传递给where的数组大小可以不相等，甚至可以是标量值。


```

### 数学和统计方法

```python
arr = np.random.randn(5, 4)
arr.mean() #算数平均数 =>0.06929924304686827
#或np.mean(arr)
arr.sum()
#mean和sum这类的函数可以接受一个axis选项参数，用于计算该轴向上的统计值，最终结果是一个少一维的数组
arr.mean(axis=1) # 1代表按行计算
arr.sum(axis=0) # 0代表列计算
#arr.mean(1)是“计算行的平均值”，arr.sum(0)是“计算每列的和”。
```

### 用于布尔型数组的方法

```python
arr = np.random.randn(100)
(arr > 0).sum() 
#另外还有两个方法any和all，它们对布尔型数组非常有用。any用于测试数组中是否存在一个或多个True，而all则检查数组中所有值是否都是True：
bools = np.array([False, False, True, False])
bools.any()  # True 
bools.all()  # False
#也可以使用 any(bools) all(bools)

In [79]: any([True,False])
Out[79]: True

In [80]: all([True,False])
Out[80]: False

In [81]: not all([True,False])
Out[81]: True
#这两个方法也能用于非布尔型数组，所有非0元素将会被当做True。
#0,None,False,和空字符串会被当成false
In [87]: any([0,0,0])
Out[87]: False

In [88]: any(['','',''])
Out[88]: False

In [89]: any([None,None])
Out[89]: False

In [90]: any([' ',''])
Out[90]: True

```

### 排序

```python
arr = np.random.randn(6)
arr.sort()#原地排序，会更改原数组

#多维数组可以在任何一个轴向上进行排序，只需将轴编号传给sort即可：
In [100]: arr.sort(1) # 1是按行排序

In [101]: arr
Out[101]: 
array([[-1.0245776 , -0.34233689, -0.12781038],
       [-0.29524049,  0.35313465,  1.38354389],
       [-0.23079029,  0.54156   ,  1.81884335],
       [-0.64880147, -0.2903122 ,  0.72493576],
       [-1.37963781,  0.70222274,  1.78041253]])

In [102]: arr.sort(0) # 0 是按列排序

In [103]: arr
Out[103]: 
array([[-1.37963781, -0.34233689, -0.12781038],
       [-1.0245776 , -0.2903122 ,  0.72493576],
       [-0.64880147,  0.35313465,  1.38354389],
       [-0.29524049,  0.54156   ,  1.78041253],
       [-0.23079029,  0.70222274,  1.81884335]])

#顶级方法np.sort返回的是数组的已排序副本，而就地排序则会修改数组本身。计算数组分位数最简单的办法是对其进行排序，然后选取特定位置的值：
In [105]: arr
Out[105]: 
array([[-0.87752799,  0.45110623, -2.38862286],
       [ 0.3294627 , -0.45374959,  1.5054472 ],
       [-0.15681887,  0.63547677,  1.46680779],
       [-0.01788483,  1.4018645 ,  0.72511586],
       [-0.01156455,  1.79538582, -0.18279433]])

In [106]: np.sort(arr)
Out[106]: 
array([[-2.38862286, -0.87752799,  0.45110623],
       [-0.45374959,  0.3294627 ,  1.5054472 ],
       [-0.15681887,  0.63547677,  1.46680779],
       [-0.01788483,  0.72511586,  1.4018645 ],
       [-0.18279433, -0.01156455,  1.79538582]])

In [107]: arr
Out[107]: 
array([[-0.87752799,  0.45110623, -2.38862286],
       [ 0.3294627 , -0.45374959,  1.5054472 ],
       [-0.15681887,  0.63547677,  1.46680779],
       [-0.01788483,  1.4018645 ,  0.72511586],
       [-0.01156455,  1.79538582, -0.18279433]])
```

### 唯一以及其他集合逻辑

```python
In [206]: names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

In [207]: np.unique(names)
Out[207]: 
array(['Bob', 'Joe', 'Will'],
      dtype='<U4')

In [208]: ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])

In [209]: np.unique(ints)
Out[209]: array([1, 2, 3, 4]) #唯一的同时，也排序了
   

#另一个函数np.in1d用于测试一个数组中的值在另一个数组中的成员资格，返回一个布尔型数组：
In [211]: values = np.array([6, 0, 0, 3, 2, 5, 6])

In [212]: np.in1d(values, [2, 3, 6])
Out[212]: array([ True, False, False,  True,  True, False,  True], dtype=bool)
```

### 用于数组的文件输入输出

```python
#NumPy能够读写磁盘上的文本数据或二进制数据。这一小节只讨论NumPy的内置二进制格式，因为更多的用户会使用pandas或其它工具加载文本或表格数据

#np.save和np.load是读写磁盘数组数据的两个主要函数。默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为.npy
In [213]: arr = np.arange(10)

In [214]: np.save('some_array', arr) #生成.npy的二进制文件
    
#压缩数据
In [119]: np.savez('array_archive.npz', a=arr, b=arr)

In [120]: arch = np.load('array_archive.npz')

In [121]: arch['b']
Out[121]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    
```

### 线性代数

```python
x.dot(y)等价于np.dot(x, y)
numpy.linalg中有一组标准的矩阵分解运算以及诸如求逆和行列式之类的东西
from numpy.linalg import inv, qr  # inv 求逆 qr 计算qr分解
X = np.random.randn(5, 5)
mat = X.T.dot(X)
inv(mat)


```

### 伪随机数生成

```python
In [7]: np.random.normal(size=3)
Out[7]: array([ 1.17067743, -0.07798573,  0.52741274])

In [8]: np.random.normal(size=(2,3))
Out[8]: 
array([[-0.10423222,  0.1407669 ,  1.29445369],
       [ 0.09798984, -1.77911919,  0.39819898]])

In [9]: np.random.normal(size=(2,3,4))
Out[9]: 
array([[[ 0.02633349,  1.91440847,  1.08620284,  1.37239362],
        [ 0.45778586,  0.93029752, -0.99105205,  0.61290413],
        [ 0.36780888,  0.31440816, -0.63012229,  1.10068709]],

       [[-0.96357067,  0.30639373, -0.96069977, -0.61771029],
        [-0.39624408,  3.02742541, -0.03841661, -0.2852032 ],
        [-0.46517498,  0.05485674, -1.16887788,  1.53013117]]])
```
# Pandas

## Series

虽然pandas采用了大量的NumPy编码风格，但二者最大的不同是pandas是专门为处理表格和混杂数据设计的。而NumPy更适合处理统一的数值数组数据。 

```python
import pandas as pd
from pandas import Series, DataFrame

#Series是一种类似于一维数组的对象，它由一组数据（各种NumPy数据类型）以及一组与之相关的数据标签（即索引）组成
In [12]: import pandas as pd

In [13]: from pandas import Series, DataFrame

In [14]: obj = pd.Series([4, 7, -5, 3])

In [15]: obj
Out[15]: 
0    4
1    7
2   -5
3    3
dtype: int64

In [16]: obj.values
Out[16]: array([ 4,  7, -5,  3])

In [17]: obj.index
Out[17]: RangeIndex(start=0, stop=4, step=1)

In [18]: obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

In [19]: obj2
Out[19]: 
d    4
b    7
a   -5
c    3
dtype: int64

In [20]: obj2.index
Out[20]: Index(['d', 'b', 'a', 'c'], dtype='object')

In [21]: obj2['a']
Out[21]: -5

In [22]: obj[2]
Out[22]: -5

## 运算
In [23]: obj2[obj2>0]
Out[23]: 
d    4
b    7
c    3
dtype: int64

In [24]: obj2*2
Out[24]: 
d     8
b    14
a   -10
c     6
dtype: int64

In [25]: import numpy as np

In [26]: np.exp(obj2)
Out[26]: 
d      54.598150
b    1096.633158
a       0.006738
c      20.085537
dtype: float64
    
#还可以将Series看成是一个定长的有序字典，因为它是索引值到数据值的一个映射。它可以用在许多原本需要字典参数的函数中：
In [27]: 'b' in obj2
Out[27]: True

In [29]: 7 in obj2.values
Out[29]: True
    
#如果数据被存放在一个Python字典中，也可以直接通过这个字典来创建Series：
In [30]: sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

In [31]: obj3 = pd.Series(sdata)

In [32]: obj3
Out[32]: 
Ohio      35000
Texas     71000
Oregon    16000
Utah       5000
dtype: int64
# 你可以传入排好序的字典的键以改变顺序：
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)

In [31]: obj4
Out[31]: 
California        NaN
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
dtype: float64
#在这个例子中，sdata中跟states索引相匹配的那3个值会被找出来并放到相应的位置上，但由于"California"所对应的sdata值找不到，所以其结果就为NaN（即“非数字”（not a number），在pandas中，它用于表示缺失或NA值）。因为‘Utah’不在states中，它被从结果中除去。    

我将使用缺失（missing）或NA表示缺失数据。pandas的isnull和notnull函数可用于检测缺失数据
In [32]: pd.isnull(obj4)
Out[32]: 
California     True
Ohio          False
Oregon        False
Texas         False
dtype: bool
    
# 实例方法
In [34]: obj4.isnull()


In [37]: obj3 + obj4
Out[37]: 
California         NaN
Ohio           70000.0
Oregon         32000.0
Texas         142000.0
Utah               NaN
dtype: float64    
    
Series对象本身及其索引都有一个name属性，该属性跟pandas其他的关键功能关系非常密切：
In [38]: obj4.name = 'population'

In [39]: obj4.index.name = 'state'

In [40]: obj4
Out[40]: 
state
California        NaN
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
Name: population, dtype: float64
        
#Series的索引可以通过赋值的方式就地修改：
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
```

## DataFrame

DataFrame是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔值等）。DataFrame既有行索引也有列索引，它可以被看做由Series组成的字典（共用同一个索引）。DataFrame中的数据是以一个或多个二维块存放的（而不是列表、字典或别的一维数据结构）

笔记：虽然DataFrame是以二维结构保存数据的，但你仍然可以轻松地将其表示为更高维度的数据

### 创建

```python
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
In [45]: frame
Out[45]: 
   pop   state  year
0  1.5    Ohio  2000
1  1.7    Ohio  2001
2  3.6    Ohio  2002
3  2.4  Nevada  2001
4  2.9  Nevada  2002
5  3.2  Nevada  2003

frame.head()# 选取前五行
pd.DataFrame(data, columns=['year', 'state', 'pop'])#列排序
frame.columns # 显示列名
In [13]: frame['state'] 
Out[13]: 
0      Ohio
1      Ohio
2      Ohio
3    Nevada
4    Nevada
5    Nevada
Name: state, dtype: object
        
#行也可以通过位置或名称的方式进行获取，比如用loc属性
In [18]: frame.loc[1]
Out[18]: 
state    Ohio
year     2001
pop       1.7
Name: 1, dtype: object

frame2['debt'] = 16.5 #批量赋值一列  
frame2['debt'] = np.arange(6) #批量赋值
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val

In [60]: frame2  
Out[60]: 
       year   state  pop  debt
one    2000    Ohio  1.5   NaN
two    2001    Ohio  1.7  -1.2
three  2002    Ohio  3.6   NaN
four   2001  Nevada  2.4  -1.5
five   2002  Nevada  2.9  -1.7
six    2003  Nevada  3.2   NaN

# 不指定就会按顺序处理
In [20]: frame['debt']= pd.Series([-1.2, -1.5, -1.7])
In [21]: frame
Out[21]: 
    state  year  pop  debt
0    Ohio  2000  1.5  -1.2
1    Ohio  2001  1.7  -1.5
2    Ohio  2002  3.6  -1.7
3  Nevada  2001  2.4   NaN
4  Nevada  2002  2.9   NaN
5  Nevada  2003  3.2   NaN

#为不存在的列赋值会创建出一个新列。关键字del用于删除列。
In [61]: frame2['eastern'] = frame2.state == 'Ohio'

In [62]: frame2
Out[62]: 
       year   state  pop  debt  eastern
one    2000    Ohio  1.5   NaN     True
two    2001    Ohio  1.7  -1.2     True
three  2002    Ohio  3.6   NaN     True
four   2001  Nevada  2.4  -1.5    False
five   2002  Nevada  2.9  -1.7    False
six    2003  Nevada  3.2   NaN    False

del frame2['eastern'] # 删除列
#注意：通过索引方式返回的列只是相应数据的视图而已，并不是副本。因此，对返回的Series所做的任何就地修改全都会反映到源DataFrame上。通过Series的copy方法即可指定复制列。


#另一种数据形式是字典
In [65]: pop = {'Nevada': {2001: 2.4, 2002: 2.9},
....:        'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
In [66]: frame3 = pd.DataFrame(pop)

In [67]: frame3
Out[67]: 
      Nevada  Ohio
2000     NaN   1.5
2001     2.4   1.7
2002     2.9   3.6    

### 转置
In [68]: frame3.T
Out[68]: 
        2000  2001  2002
Nevada   NaN   2.4   2.9
Ohio     1.5   1.7   3.6

跟Series一样，values属性也会以二维ndarray的形式返回DataFrame中的数据：
In [74]: frame3.values
Out[74]: 
array([[ nan,  1.5],
       [ 2.4,  1.7],
       [ 2.9,  3.6]])
```

### 索引对象

```python
Index对象是不可变的，因此用户不能对其进行修改：
obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index #=>Index(['a', 'b', 'c'], dtype='object')
index[1:]
index[1] = 'd'  # TypeError
#不可变可以使Index对象在多个数据结构之间安全共享：
#与python的集合不同，pandas的Index可以包含重复的标签：
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
```

### 基本功能

```python
new_obj = obj.drop('c') #根据索引删除行
obj.drop(['d', 'c'])

通过传递axis=1或axis='columns'可以删除列的值：
data.drop('two', axis=1)
data.drop(['two', 'four'], axis='columns')

许多函数，如drop，会修改Series或DataFrame的大小或形状，可以就地修改对象，不会返回新的对象：

# 切片选取和赋值，略 类似numpy

#用loc和iloc进行选取

# 整数索引
ser = pd.Series(np.arange(3))
ser[-1] # key erro

## 非整数索引没问题
In [145]: ser2 = pd.Series(np.arange(3), index=['a', 'b', 'c'])
In [146]: ser2[-1]
Out[146]: 2
    
#为了进行统一，如果轴索引含有整数，数据选取总会使用标签。为了更准确，请使用loc（标签）或iloc（整数）：
ser.iloc[-1]
Out[31]: 2 

In [34]: ser[:-1]
Out[34]: 
0    0
1    1
dtype: int64

In [35]: ser
Out[35]: 
0    0
1    1
2    2
dtype: int64

算术运算和数据对齐
#pandas最重要的一个功能是，它可以对不同索引的对象进行算术运算。在将对象相加时，如果存在不同的索引对，则结果的索引就是该索引对的并集。对于有数据库经验的用户，这就像在索引标签上进行自动外连接。看一个简单的例子：
In [150]: s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])

In [151]: s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1],
   .....:                index=['a', 'c', 'e', 'f', 'g'])

In [152]: s1
Out[152]: 
a    7.3
c   -2.5
d    3.4
e    1.5
dtype: float64

In [153]: s2
Out[153]: 
a   -2.1
c    3.6
e   -1.5
f    4.0
g    3.1
dtype: float64
    
In [40]: s1+s2
Out[40]: 
a    5.2
c    1.1
d    NaN
e    0.0
f    NaN
g    NaN
dtype: float64
    
如果DataFrame对象相加，没有共用的列或行标签，结果都会是空：
In [160]: df1 = pd.DataFrame({'A': [1, 2]})

In [161]: df2 = pd.DataFrame({'B': [3, 4]})

In [162]: df1
Out[162]: 
   A
0  1
1  2

In [163]: df2
Out[163]: 
   B
0  3
1  4

In [164]: df1 - df2
Out[164]: 
    A   B
0 NaN NaN
1 NaN NaN
```

#### 在算数方法中填充值

```python
In [165]: df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
   .....:                    columns=list('abcd'))

In [166]: df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
   .....:                    columns=list('abcde'))

In [167]: df2.loc[1, 'b'] = np.nan

In [168]: df1
Out[168]: 
     a    b     c     d
0  0.0  1.0   2.0   3.0
1  4.0  5.0   6.0   7.0
2  8.0  9.0  10.0  11.0

In [169]: df2
Out[169]: 
      a     b     c     d     e
0   0.0   1.0   2.0   3.0   4.0
1   5.0   NaN   7.0   8.0   9.0
2  10.0  11.0  12.0  13.0  14.0
3  15.0  16.0  17.0  18.0  19.0

#将它们相加时，没有重叠的位置就会产生NA值：
In [170]: df1 + df2
Out[170]: 
      a     b     c     d   e
0   0.0   2.0   4.0   6.0 NaN
1   9.0   NaN  13.0  15.0 NaN
2  18.0  20.0  22.0  24.0 NaN
3   NaN   NaN   NaN   NaN NaN

## 可以使用使用df1的add方法，传入df2以及一个fill_value参数：
In [171]: df1.add(df2, fill_value=0)
Out[171]: 
      a     b     c     d     e
0   0.0   2.0   4.0   6.0   4.0
1   9.0   5.0  13.0  15.0   9.0
2  18.0  20.0  22.0  24.0  14.0
3  15.0  16.0  17.0  18.0  19.0

#与此类似，在对Series或DataFrame重新索引时，也可以指定一个填充值：
In [174]: df1.reindex(columns=df2.columns, fill_value=0)
Out[174]: 
     a    b     c     d  e
0  0.0  1.0   2.0   3.0  0
1  4.0  5.0   6.0   7.0  0
2  8.0  9.0  10.0  11.0  

```

#### DataFrame和Series之间的运算

跟不同维度的NumPy数组一样，DataFrame和Series之间算术运算也是有明确规定的。先来看一个具有启发性的例子，计算一个二维数组与其某行之间的差：

```python
In [175]: arr = np.arange(12.).reshape((3, 4))

In [176]: arr
Out[176]: 
array([[  0.,   1.,   2.,   3.],
       [  4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.]])

In [177]: arr[0]
Out[177]: array([ 0.,  1.,  2.,  3.])

In [178]: arr - arr[0]
Out[178]: 
array([[ 0.,  0.,  0.,  0.],
       [ 4.,  4.,  4.,  4.],
       [ 8.,  8.,  8.,  8.]])
#当我们从arr减去arr[0]，每一行都会执行这个操作。这就叫做广播（broadcasting），附录A将对此进行详细讲解。DataFrame和Series之间的运算差不多也是如此：

In [186]: series3 = frame['d']

In [187]: frame
Out[187]: 
          b     d     e
Utah    0.0   1.0   2.0
Ohio    3.0   4.0   5.0
Texas   6.0   7.0   8.0
Oregon  9.0  10.0  11.0

In [188]: series3
Out[188]: 
Utah       1.0
Ohio       4.0
Texas      7.0
Oregon    10.0
Name: d, dtype: float64

In [189]: frame.sub(series3, axis='index')
Out[189]: 
          b    d    e
Utah   -1.0  0.0  1.0
Ohio   -1.0  0.0  1.0
Texas  -1.0  0.0  1.0
Oregon -1.0  0.0  1.0
#传入的轴号就是希望匹配的轴。在本例中，我们的目的是匹配DataFrame的行索引（axis='index' or axis=0）并进行广播。
```

#### 函数和应用的映射

NumPy的ufuncs（元素级数组方法）也可用于操作pandas对象

```python
In [190]: frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
   .....:                      index=['Utah', 'Ohio', 'Texas', 'Oregon'])

In [51]: frame
Out[51]: 
               b         d         e
Utah   -0.634462 -0.905178 -0.439143
Ohio    1.138959 -0.252519  0.841666
Texas  -0.329807  2.621812 -0.877364
Oregon -0.692714  0.383542  0.021585

In [52]: np.abs(frame)
Out[52]: 
               b         d         e
Utah    0.634462  0.905178  0.439143
Ohio    1.138959  0.252519  0.841666
Texas   0.329807  2.621812  0.877364
Oregon  0.692714  0.383542  0.021585

#另一个常见的操作是，将函数应用到由各列或行所形成的一维数组上。DataFrame的apply方法即可实现此功能：
In [53]: f = lambda x: x.max() - x.min()

In [54]: frame.apply(f) #应用在列行
Out[54]: 
b    1.831673
d    3.526990
e    1.719031
dtype: float64
    
In [195]: frame.apply(f, axis='columns') # 应用在行上。
Out[195]:
Utah      0.998382
Ohio      2.521511
Texas     0.676115
Oregon    2.542656
dtype: float64
    
#许多最为常见的数组统计功能都被实现成DataFrame的方法（如sum和mean），因此无需使用apply方法。
#传递到apply的函数不是必须返回一个标量，还可以返回由多个值组成的Series：
In [196]: def f(x):
   .....:     return pd.Series([x.min(), x.max()], index=['min', 'max'])

In [197]: frame.apply(f)
Out[197]: 
            b         d         e
min -0.555730  0.281746 -1.296221
max  1.246435  1.965781  1.393406

#元素级的Python函数也是可以用的。假如你想得到frame中各个浮点值的格式化字符串，使用applymap即可：
#之所以叫做applymap，是因为Series有一个用于应用元素级函数的map方法：
#DataFrame没有这个方法' object has no attribute 'map'，所以用applymap
In [200]: frame['e'].map(format)
Out[200]: 
Utah      -0.52
Ohio       1.39
Texas      0.77
Oregon    -1.30
Name: e, dtype: object
```

#### 排序和排名

```python
#要对行或列索引进行排序（按字典顺序）sort_index 返回新的排序对象
In [201]: obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])

In [202]: obj.sort_index()
Out[202]:
a    1
b    2
c    3
d    0
dtype: int64

#对于DataFrame，则可以根据任意一个轴上的索引进行排序    
In [203]: frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
   .....:                      index=['three', 'one'],
   .....:                      columns=['d', 'a', 'b', 'c'])

In [204]: frame.sort_index()
Out[204]: 
       d  a  b  c
one    4  5  6  7
three  0  1  2  3

In [205]: frame.sort_index(axis=1)
Out[205]:
       a  b  c  d
three  1  2  3  0
one    5  6  7  4

#数据默认是按升序排序的，但也可以降序排序：
In [206]: frame.sort_index(axis=1, ascending=False)
Out[206]: 
       d  c  b  a
three  0  3  2  1
one    4  7  6  5

#若要按值对Series进行排序，可使用其sort_values方法 
#在排序时，任何缺失值默认都会被放到Series的末尾：

In [209]: obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])

In [210]: obj.sort_values()
Out[210]: 
4   -3.0
5    2.0
0    4.0
2    7.0
1    NaN
3    NaN
dtype: float64

# DataFrame value 排序
frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})


```

