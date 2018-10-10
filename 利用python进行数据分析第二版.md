引入惯例

```
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm
```

# numpy

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

## 4.