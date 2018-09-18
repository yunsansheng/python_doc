## 1. 数据结构和算法

### 1. 解压数据

   ```python
   #*代表多个
   In [76]: name,*mid,last =[1,2,3,4,5,6]
   In [77]: mid
   Out[77]: [2, 3, 4, 5]
       
   #_代表忽略
   name,*_,last =[1,2,3,4,5,6]
   In [74]: _
   Out[74]: [2, 3, 4, 5]
   #这里的_只占位，实际效果和上面一样
   
   ```

### 2. 队列最大最小

   ```python
   #保留最后n个元素
   from collections import deque
   #deque([iterable[, maxlen]])    iteralbe和maxlen都是可选参数
   q=deque()#没有maxlen，就是一个无限队列
   q=deque(maxlen=3)
   q=deque([1,2,3],maxlen=3)
   #每次只能新增或删除一个。
   q.append()
   q.appendleft()
   q.pop()
   q.popleft()
   
   # 查找最大或最小的N个元素
   # 当数组较小时，可以用排序，只有数组比较大时，才有意义。
   # nlargest(n, iterable, key=None)
   import heapq
   ## 数组
   In [81]: heapq.nlargest(3,nums)
   Out[81]: [223, 21, 8]
   
   In [82]: heapq.nsmallest(3,nums)
   Out[82]: [1, 2, 2]
   
   ## 复杂结构
   p_info=[
       {'name':"IBM",'price':2},
       {'name':"Apple",'price':1},
       {'name':"FB",'price':9},
       {'name':"YHOO",'price':10}
   ]
   cheap =heapq.nsmallest(3,p_info,key=lambda s:s['price'])
   
   In [92]: cheap
   Out[92]: 
   [{'name': 'Apple', 'price': 1},
    {'name': 'IBM', 'price': 2},
    {'name': 'FB', 'price': 9}]
   ```

### 3. 字典对应多个值

   ```python
   ## 注意这里用的是append ，而不是直接赋值
   ## 如果是set，就不是append 而是and
   In [109]: from collections import defaultdict
   In [110]: d =defaultdict(list)
   In [111]: d['a'].append(1)
   Out[112]: defaultdict(list, {'a': [1]})
   In [114]: d['a'].append(2)
   Out[115]: defaultdict(list, {'a': [1, 2]})
       
   # 自己实现
   d={}
   for key,value in pairs:
       if key not in d:
           d[key]=[]
       d[key].append(value)
   
   # defaultdict实现
   d =defaultdict(list)
   for key,value in pairs:
       d[key].append(value)
   
   ```

### 4. 有序字典

   ```python
   from collections import OrderedDict
   # OrderedDict 是普通dict大小的两倍，过大的字典，要考虑到性能的问题
   In [125]: d= OrderedDict()
   In [126]: d['foo']=1
   In [127]: d['bar']=2
   
   In [128]: d
   Out[128]: OrderedDict([('foo', 1), ('bar', 2)])
   
   In [129]: for key in d:
        ...:     print(key,d[key])
        ...:     
   foo 1
   bar 2
   
   ```

### 5. 字典的最大，最小，排序

```python
In [136]: prices ={
     ...: 'ACME':45.23,
     ...: 'AAPL':612.78,
     ...: 'IBM':205.55}

In [137]: min_price =min(zip(prices.values(),prices.keys()))
In [138]: min_price
Out[138]: (45.23, 'ACME')
 
# 排序
In [139]: prices_sorted =sorted(zip(prices.values(),prices.keys()))
In [140]: prices_sorted
Out[140]: [(45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]
    
zip函数创建的是一个只能访问一次的迭 代器。
prices_and_names=zip(prices.values(),prices.keys())
min_price = min(prices_and_names)
max_price = max(prices_and_names)#报错

# 通过key(不能同时拿到key和value)
In [141]: min(prices,key = lambda k: prices[k])
Out[141]: 'ACME'
 
# 如果最大最小值value重复，那么会根据key的大小返回
In [145]: prices={"AAA":45.23,"ZZZ":45.23}

In [146]: min(zip(prices.values(),prices.keys()))
Out[146]: (45.23, 'AAA')

In [147]: max(zip(prices.values(),prices.keys()))
Out[147]: (45.23, 'ZZZ')
    
## 序列中字典的排序
rows =[{'frnme':"B",'lname':'J'},
       {'frnme':"1B",'lname':'3J'},
       {'frnme':"2B",'lname':'J1'}]
from operator import itemgetter
In [222]: rows=[{'frnme':"B",'lname':'J'},{'frnme':"1B",'lname':'3J'},{'frnme':"
     ...: 2B",'lname':'J1'}]

In [223]: sorted(rows,key=itemgetter('frnme'))
Out[223]: 
[{'frnme': '1B', 'lname': '3J'},
 {'frnme': '2B', 'lname': 'J1'},
 {'frnme': 'B', 'lname': 'J'}]

# 支持多个key排序                                                                       
In [224]: sorted(rows,key=itemgetter('frnme','lname'))
Out[224]: 
[{'frnme': '1B', 'lname': '3J'},
 {'frnme': '2B', 'lname': 'J1'},
 {'frnme': 'B', 'lname': 'J'}]
#上面两个方法可以替换成,不过itemgetter更快
sorted(rows,key=lambda k: k["frnme"])
sorted(rows,key=lambda k: (k["frnme"],k["lname"]))     
                                                                      
#同样适用于max和min函数
min(rows,key=itemgetter("blabla"))                                                                       
                                                                       
                                                                       
# 在对象中，key
user =[User(23),User(11),User(10)]
sorted(user,key= lambda u:u.userid)
# 或
from operator import attrgetter
sorted(user,key= attrgetter(userid))
                                                                       
```

### 6. 字典的运算

```python
In [148]: a={'x':1,'y':2,'z':3}
In [149]: b={'w':10,'x':11,'y':2}

In [150]: a.keys()&b.keys()
Out[150]: {'x', 'y'}

In [151]: a.keys()-b.keys()
Out[151]: {'z'}

In [152]: a.items()&b.items()
Out[152]: {('y', 2)}
 
# 可以用来过滤字典的key
In [155]: {key:a[key] for key in a.keys() -{'z','w'}}
Out[155]: {'x': 1, 'y': 2}

#value 并不支持上面的方法，因为value 可能会有重复
```

### 7. 删除序列重复值并保持顺序

```python
#如果序列上的值都是hashable
def dedupe(items):
    seen =set()#这个只是用来判断，不返回
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a=[1,5,2,1,9,1,5,10]

list(dedupe(a))
[1,5,2,9,10]

# 如果字典去重,key和value都相同
def dedupe(items,key=None):
    seen =set()
    for item in items:
        val = item if key is None else key(item) # 兼容hashable
        if val not in seen:
            yield item #返回的是item
            seen.add(val) # 增加的是拼接的value
a=[{"x":1,"y":2},{"x":1,"y":2},{"x":2,"y":3}]
list(dedupe(a,key =lambda d: (d['x'],d['y'])))  # 这里传入的是key和value的tuple

[{'x': 1, 'y': 2}, {'x': 2, 'y': 3}]


```

### 8. 命名切片

```python
In [202]: shares = slice（20，23）
Out[202]: slice(20, 23, None)

In [203]: cost =recoder[shares]

In [203]: shares.start
Out[203]: 20
In [204]: shares.stop
Out[204]: 23
In [205]: shares.step

#这个indices相当于stop的位置,只要是大于之前的stop索引，按之前的来，否则就取小索引
In [206]: print(shares.indices(100))
(20, 23, 1)
In [207]: print(shares.indices(10))
(10, 10, 1)


```

### 9. 计数

```python
In [208]: from collections import Counter

In [209]: word=['a','b','c','b','d','e','c','c']

In [210]: Counter(word)
Out[210]: Counter({'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 1})

# top3
In [211]: Counter(word).most_common(3)
Out[211]: [('c', 3), ('b', 2), ('a', 1)]

# sepical
In [212]: Counter(word)['a']
Out[212]: 1

# update
In [213]: word_ct =Counter({'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 1})
In [214]: moreword =['d','a']

In [215]: word_ct.update(moreword)
Out[216]: Counter({'a': 2, 'b': 2, 'c': 3, 'd': 2, 'e': 1})

# combine
word_ct1+word_ct2
word_ct1-word_ct2

```

### 10. 通过字段将序列分组

```python
## 要先排序，后分组	
row=[{'rs':'A','date':'07/01/2017'},{'rs':'B','date':'07/01/2017'},...]
from operator import itemgetter
from itertools import groupby

row.sort(key=itemgetter('date'))
row
Out[11]: 
[{'rs': 'A', 'date': '07/01/2017'},
 {'rs': 'B', 'date': '07/01/2017'},
 {'rs': 'C', 'date': '07/02/2017'},
 {'rs': 'D', 'date': '08/01/2017'}]
     
groupby(row,key=itemgetter('date'))
Out[12]: <itertools.groupby at 0x106bb8d00>
     
list(groupby(row,key=itemgetter('date')))
Out[13]: 
[('07/01/2017', <itertools._grouper at 0x106bc96d8>),
 ('07/02/2017', <itertools._grouper at 0x106bc9438>),
 ('08/01/2017', <itertools._grouper at 0x106bc9320>)]

for date,items in groupby(row,key=itemgetter('date')):
    print(date)
    for i in items:
        print(" ",i)
        
07/01/2017
  {'rs': 'A', 'date': '07/01/2017'}
  {'rs': 'B', 'date': '07/01/2017'}
07/02/2017
  {'rs': 'C', 'date': '07/02/2017'}
08/01/2017
  {'rs': 'D', 'date': '08/01/2017'}
## 还有一种方法是,这种不用事先排序，性能更快一点
from collections import defaultdict
row_by_data = defaultdict(list)
for row in rows:
    row_by_data[row["date"]].append(row)
   
```

### 11. 过滤序列元素

```python
mylst =[1,2,4,5,2,21,2]
[n for n in mylst if n >3]
(n for n in mylst if n >3)

filter()
def is_int(val):
    try:
        x= int(val)
        return True
    except ValueError:
        return False
list(filter(is_int,mylst))

def is_odd(n):
    return n % 2 == 1
# 也能在转换时，转化数据
import math
[math.sqrt(n) for n in mylst if n >3]

# 替换不符合条件的数据
In [226]: mylst =[1,2,4,5,2,21,2]

In [227]: [n if n >3 else 0 for n in mylst]
Out[227]: [0, 0, 4, 5, 0, 21, 0]

# 使用compress
rs=[
    'rs1',
    'rs2',
    'rs3'
    ]
counts =[2,1,3]

from itertools import compress
bigthen1 =[n>1 for n in counts ]#=>[True,False,True]

list(compress(rs,bigthen1))

```



### 12. 从字典提取子集

```python 
1. 字典推导式
{key:val for key,val in prices.items() if value >200 or key in ..}

```

### 13. 映射名称到序列元素

```python
from collections import namedtuple
Subdesc =  namedtuple("Sub_des",['addr',"joined"])  # __main__.Sub_des                     
sub=Subdesc("adee","2018")  #Sub_des(addr='adee', joined='2018')
sub.addr  #'adee'
## 支持元组操作和解压
len(sub) #2
addr,joined = sub

## 用途时从下标解放出来，通过name访问
## 代替字典，节省空间
## 命名元素是不可更改的
## 可以用_replace方法
sub._replace(addr="123")

## 如果是很多实例的搞笑数据结构，建议用类实现。包含__slots__的类

```

### 14. 转换并同时计算数据

```python 
s= sum(( x for x in nums)) #equal to
s= sum(x for x in nums)

## 传递key 有时候很有用
In [3]: min(p['price'] for p in p_info)
Out[3]: 1

In [4]: min(p_info,key=lambda s:s["price"])
Out[4]: {'name': 'Apple', 'price': 1}
```

### 15. 在字典中分别查找

```python
a={'x':1,'z':3}
b={'y':2,'z':4}
#firstly find in a, then in b
from collections import ChainMap
c=ChainMap(a,b)  # the sequence is important
print(c["x"]) # from a
print(c["y"]) # from b
print(c["z"]) # from a
c.get("y")
c.keys()
c.values()

# the update is alway to the first dict
del c['y'] # erro "Key not found in the first mapping: 'y'"

#only read update. can't del

## also can used is this way
values =ChainMap()
values['x']= 1

values=values.new_child() # 重新赋值
values['x']= 2

values['x']  # 2
values.parents['x'] # 1
## chainMap use the origin dict and will update when the origin dict is updated.
dita.update(dctb) # this will create a new dict and no relationship with the origin

```

## 2. 字符串和文本

### 1. re.split()

```python
line="asdf fjdk; afed, fjek,asdk, foo"
import re
re.split('[;,\s]\s*',line)
#Out[54]: ['asdf', 'fjdk', 'afed', 'fjek', 'asdk', 'foo']
# 和str.split 区别是可以传正则表达式
## 保留分割符
In [56]: re.split('(;|,|\s)\s*',line)
Out[56]: ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdk', ',', 'foo']
## (?:..) 非捕获分组
In [57]: re.split('(?:;|,|\s)\s*',line)
Out[57]: ['asdf', 'fjdk', 'afed', 'fjek', 'asdk', 'foo']
    
```

### 2. endswith()

```python
find starswith endswith
# 内建方法
In [58]: filename ='spam.txt'

In [59]: filename.endswith('.txt')
Out[59]: True

In [60]: filename.startswith('file.')
Out[60]: False

# 只接受tuple，如果是其他iter，需要先转化
In [61]: filename.endswith(('.c','.k','.txt'))
Out[61]: True

[name for name in filenames in name.endswith(('.c','.h'))]
any(name.endswith('.py') for name in filenames)  # find one return True

# 或者用正则实现
re.match('http:|https:|ftp:',url)

In [65]: "aind".find('a')
Out[65]: 0

In [66]: "aind".find('d')
Out[66]: 3

In [67]: "aind".find('in')
Out[67]: 1

```

### 3. 通配符匹配字符串

```python
from fnmatch import fnmatch,fnmatchcase
# 适用于简单的通配符能完成的操作时
In [63]: fnmatch('foo.txt','*.txt')
Out[63]: True
# 根据不同的系统，大小写匹配规则不一样
fnmatchcase('foo.txt','*.txt')# 这个匹配大小写

# 文件名匹配也可以用glob模块

```

### 4. 字符串匹配和搜索

```python
re.match(r'\d+/\d+/\d+',text1)
re.match(r'\d+/\d+/\d+',text2)

# 如果需要同一个模式匹配多次，为什么后续修改的方便，可以预编译为模式对象
# 预编译可以提升性能
datepat = re.compile(r'\d+/\d+/\d+')
datepat.match(text1)

# match 总是从开头匹配，如果要匹配，模式出现的任意位置用findall
# match 并不限制结尾
depepat.findall(text1)

# findall 是以列表返回，如果想以迭代方式返回用finditer()

## 替换
text.replace('yeah','yep')
## 复杂模式
import re
re.sub(r'\d+/\d+/\d+',r'\3-\1-\2',text)
#\n代表的是组号
# 也可以预编译
datepat.sub(r'\3-\1-\2',text)

# 也可以传递一个函数
from calendar import month_abbr
def change_data(m):
    mon_name= month_abbr[int(m.group(1))]
    #'{year} {month} {day}'.format(year='2019',month='09',day='01')
    return '{} {} {}'.format(m.group(2),mon_name,m.group(1))

datepat.sub(change_data,text)

# subn 除了替换，还返回替换的个数
new,n = datepat.sub(r'\3-\1-\2',text)

## 大小写忽略可以用flags =re.IGNORECASE
## 但是 sub替换不会保留原来的case

```

### 5. 清理文本字符串

```python
In [86]: intab ='aeiou'
In [87]: outtab='12345'

# 单个替换，assci  还是建议用replace
In [89]: trantab = str.maketrans(intab,outtab)
Out[90]: {97: 49, 101: 50, 105: 51, 111: 52, 117: 53}

str = "this is string example....wow!!!";
str.translate(trantab)  
```

## 3. 数字 日期和时间

### 1. 数字精度

```python
x =1.223232
format(x,'0.2f')
'value is {:0.3f}'.format(x)

# 精确的浮点数运算 decimal
# 更加精确意味着一定的性能损耗

from decimal import Decimal
## 注意传的是字符串
a= Decimal('4.2')
b= Decimal('2.1')

a+b == Decimal('6.3')  #True
a+b =6.3 #false


```

### 2. 随机选择

```python
import random

values=[1,2,23,21,22]
# 从values中选一个
random.choice(values)

# 选择多个
random.sample(values,2)

# 打乱顺序
random.shuffle(values)

# 生成随机整数
random.randint(0,100)

# 0到1内的浮点数
random.random()
#0.032386039843224634

#random函数不能用于密码学的相关程序中，可以用ssl模块来实现

```

### 3. 日期和时间

```python
from datetime import timedelta

In [11]: a= timedelta(days=2,hours=6)
#datetime.timedelta(days=2, seconds=21600)

In [13]: b=timedelta(hours=4.5) #自动转化成了秒
#datetime.timedelta(seconds=16200)

In [15]: c=a+b
In [17]: c.days #2
    
In [19]: c.seconds 
Out[19]: 37800
In [20]: c.seconds/3600
Out[20]: 10.5
In [21]: c.total_seconds()/3600
Out[21]: 58.5

from datetime import datetime
In [24]: a= datetime(2012,9,23)

In [25]: a+timedelta(days=10)
Out[25]: datetime.datetime(2012, 10, 3, 0, 0)

In [26]: b=datetime(2012,12,21)

In [27]: b-a
Out[27]: datetime.timedelta(days=89)

In [28]: (b-a).days
Out[28]: 89

In [29]: now= datetime.today()

In [30]: now
Out[30]: datetime.datetime(2018, 9, 13, 17, 16, 41, 45710)

In [31]: now+timedelta(minutes=10)
Out[31]: datetime.datetime(2018, 9, 13, 17, 26, 41, 45710)
    
## 复杂日期计算，包括节假日 dateutil不是内建函数
class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)  #这个最多支持weeks级别

# pip3 install python-dateutil
In [41]: from dateutil.relativedelta import relativedelta

In [42]: a
Out[42]: datetime.datetime(2012, 9, 23, 0, 0)

In [43]: a+ relativedelta(months=+1)
Out[43]: datetime.datetime(2012, 10, 23, 0, 0)

In [44]: a+ relativedelta(months=+4)
Out[44]: datetime.datetime(2013, 1, 23, 0, 0)

In [45]: b
Out[45]: datetime.datetime(2012, 12, 21, 0, 0)

In [46]: a
Out[46]: datetime.datetime(2012, 9, 23, 0, 0)

In [47]: d= relativedelta(b,a)

In [48]: d
Out[48]: relativedelta(months=+2, days=+28)

In [49]: d.months
Out[49]: 2

In [50]: d.day

    
In [58]: from dateutil.rrule import FR
# next friday
In [59]: d+ relativedelta(weekday=FR)
#Out[59]: relativedelta(months=+2, days=+28, weekday=FR)

# priv firday
#d+ relativedelta(weekday=FR(-1))

In [65]: a+ relativedelta(weekday=FR)
Out[65]: datetime.datetime(2012, 9, 28, 0, 0)

In [66]: a+ relativedelta(weekday=FR(-1))
Out[66]: datetime.datetime(2012, 9, 21, 0, 0)

## 字符串转为日期  ## 这个方法很慢，如果大量使用，要注意性能
text='2012-09-20'
y = datetime.strptime(text,'%Y-%m-%d')
datetime.datetime(2012, 9, 20, 0, 0)
```

## 4. 迭代器和生成器

### 1. 不用for迭代

```python
with open('file') as f:
    while True:
        line =next(f,None) # 指定结尾为None,否则报错
        if None is None:
            break
        print(line,end='')

```

### 2. 代理迭代

```python
In [1]: class Std_score(object):
   ...:     def __init__(self,fst,mid,lst):
   ...:         self._score = (fst,mid,lst)
   ...:     def __iter__(self):
   ...:         return iter(self._score)
   ...:     

In [2]: st1 =Std_score(99,98,100)

In [3]: st1
Out[3]: <__main__.Std_score at 0x108fe5f60>

In [4]: next(st1)#不能使用next
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-752f107f3ee9> in <module>()
----> 1 next(st1)

TypeError: 'Std_score' object is not an iterator

In [5]: for ch in st1:
   ...:     print(ch)
   ...:     
99
98
100

```

