# 基本语法
- return关键字只能用到函数中
- break 只能用在loop中
- 位置参数，关键词参数（给了初始值就是位置参数）
- 易混淆
  - / 除
  - //整除
  - % 取余
  - \ 这个不是运算符，是转义符
  - is 和 in
    - is（id,value,type）
    - in (exists or not)

# 编码

由于Python的字符串类型是`str`，在内存中以Unicode表示

如果要在网络上传输，或者保存到磁盘上，就需要把`str`变为以字节为单位的`bytes`。

以Unicode表示的`str`通过`encode()`方法可以编码为指定的`bytes`

在`bytes`中，无法显示为ASCII字符的字节，用`\x##`显示



## 数据类型
- number （不可变）
  - int
  - float
  - complex
  - bool(继承自int)
- string （不可变）
- list （可变）
- tuple（不可变）
- set（可变）
- dictonary（可变）


```python
常用的两种类型判断方法 
1. type()继承
2. isinstance() 可判断继承关系
type（1） => int
type(True) => bool

isinstance(True,int) => True

```

## 数据结构比较

- list,tuple 序列(sequence) 
- dict,set 映射(mapping) 

| list       |        tuple         | dict                | set               |
| ---------- | :------------------: | ------------------- | ----------------- |
| []         |          ()          | {key:value}         | {1,2}，set({1,2}) |
| 可变       | **不可变**(元素可变) | key不可变，不能重复 | 可变，排重        |
| 可以是引用 |      可以是引用      | key**不能**是引用   | **不能**是引用    |
| 有序       |         有序         | 无序                | 无序              |


- set可变，但是不能放入可变对象，比如 list或者其他的set
- **直接赋值空{},将会是dict类型，如果要创建set类型，必须set{[]}**
- **如果赋值{1,2,3},将是set类型**
- set可以进行集合运算

# 匿名函数 lambda

```python
lambda x: x * x #没有函数名,不用写return，注意冒号
#same as
def f(x):
	return x*x 
```
# 装饰器
```python
@log
def now():
	pass
#=>same as
now = log(now)

#两层嵌套函数
import functools
def log(func):
    @functools.wraps(func)#用于将wrapper函数指向原本的function name
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
#为什么需要两层嵌套？
 #1.fun1传入的必定是fun2函数
 #2.需要一个嵌套函数，来接受所有的参数，这样才能返回原来的函数。   
 #3.如果希望，函数前后，都可以调用一个方法，可以不写return，直接执行方法func(*args, **kw)，但是函数将没有返回值。
    
#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数。
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
#这个3层嵌套的decorator用法如下：
@log('execute')
def now():
    print('2015-3-25')
#now = log('execute')(now)
    
```

# 常用函数
- 字符串格式化

  ```python
  'Age: %s. Gender: %s' % (25, True)
  'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
  ```

- open（）

  +  参数file
  +  参数mode（默认r）

- sorted(list,reverse=False)

- zip(seq1,seq2,...) =>[(),()]
  ```python
  questions = ['name', 'quest', 'favorite color']
  answers = ['lancelot', 'the holy grail', 'blue']
  for q, a in zip(questions, answers):
  	print('What is your {0}?  It is {1}.'.format(q, a))
  ```

- enumerate
  ```python
  for i, v in enumerate(['tic', 'tac', 'toe']):
  	print(i,v)
  ```



# 高级用法
- 列表生成式
  - [i for i in range(1,11)]

  - [i for i in range(1,11) if i%2==0]

  - [(i,i+2) **for** i **in** range(1,11) **if** i%2==0]

  - same as 

    ```python
    def list_comprehension()
    	lst=[]
    	for i in range(1,11):
    		lst.append(i)
    	return lst
    ```

  - 优势是性能快，简洁

- 字典生成式
  - {i:i+1 for i in range(4)}
  - {i:i+1 for i in range(10) if i%2==0}
  - 性能占优

- 生成式
  - (i for i in range(4))


|列表生成式|字典生成式|生成器（generator）|迭代器（iterator）|
|---|---|---|---|
|[v function]|{k:v function}|(function), 带yield的函数|可以被`next()`函数调用并不断返回下一个值的对象称为迭代器|
|返回list|返回dict|可以使用next(),for 迭代|`list`、`tuple`、`dict`、`set`、`str`等是iterable，但不是iterator|

```python
from collections import Iterable
from collections import Iterator
isinstance([], Iterable) #==>True
isinstance([], Iterator) #==>False
```

- @classmethod @staticmethod

  - @classmethod,第一个传入类,cls（不需要穿入self）能直接调用类的属性和方法
  - @staticmethod,不需要传入self和类


# 面向对象编程（oop）

- 把对象当成程序的基本单元，一个对象包含了数据和操作数据的函数。
- python所有数据类型都可以视为对象，自定义对象就是class（类）的概念。
- 面向对象的设计思想是抽象出Class，根据Class创建Instance。
- 面向对象的三大特点：
  - 数据封装（对外部隐藏有关对象工作原理的细节。 ）
  - 继承 可基于通用类创建出专用类。 
  - 多态 可对不同类型的对象执行相同的操作，而这些操作就像“被施了魔法”一样能够 正常运行。 

# 类和实例

- `self`就指向创建的实例本身。

- 使用`__init__`方法给实例绑定属性

- 各个实例拥有的数据都互相独立，互不影响

- 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

- 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。（数据封装）

- 实例可以绑定自己的属性

## 类属性和实例属性

- 在Python中，实例的变量名如果以`__`开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
- 如果以`_`开头，可以访问，但是建议不要访问
- 如果类和实例的属性，同名，那么实例属性会覆盖类属性。实例属性不存在，会去类属性中寻找。


## 继承和多态

### 继承

- 子类可以继承父类的方法，子类可以覆盖父类的方法。
- 继承顺序，只有新式类有 `__mro__`属性，告诉查找顺序是怎样的
  - 深度优先
  - 广度优先（python3 新式类）

### 多态

- 多态的好处就是，当我们需要传入`Dog`、`Cat`、`Tortoise`……时，我们只需要接收`Animal`类型就可以了

### 静态语言 vs 动态语言

- 对于静态语言（例如Java）来说，如果需要传入`Animal`类型，则传入的对象必须是`Animal`类型或者它的子类，否则，将无法调用`run()`方法。
- 对于Python这样的动态语言来说，则不一定需要传入`Animal`类型。我们只需要保证传入的对象有一个`run()`方法就可以了：
- 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

# 面向对象高级

- `__slots__`用于限制绑定属性 ，对继承不起作用

- `@property` 属性装饰器，简化属性的读写

  ```python
  class Student(object):
      
      def __init__(self,birth):
          self._birth = birth
  
      @property
      def birth(self):
          return self._birth
  
      @birth.setter
      def birth(self, value):
          self._birth = value
  
      @property
      def age(self):
          return 2015 - self._birth
  ```

- 多重继承（可以继承多个类，MixIn设计，java是不允许多继承的）

- 定制类

  - `__str__`

  - `__iter__`
  - `__getitem__`
  - `__getattr__`只有在没有找到属性的情况下，才调用
  - `__call__`

- 枚举类 
  - Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
  - value属性则是自动赋给成员的int常量，默认从1开始计数。
```python
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
Month.Jan #=> <Month.Jan: 1>
Month.Jan.value #=> 1
```

```python
from enum import Enum, unique
#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
```


- 元类(metaclass)

  - 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

- 超类（super）

  ```python
  class SongBird(Bird):
  	def __init__(self):
  		super().__init__()  #当你访 问它的属性时，它将在所有的超类(以及超类的超类，等等)中查找，直到找到指定的属性或 引发AttributeError异常。
    		self.sound = 'Squawk!' 
    	def sing(self):
  		print(self.sound)
  ```

- staticmethod & classmethod
   - staticmethod无须传入，self，classmethod传入cls.
   - 定义这些方法后，就可像下面这样使用它们(无需实例化类):
    ```python
    MyClass.smeth()
    MyClass.cmeth()
    ```
   - 主要用于工厂函数

# 调试

1. pycharm自带的调试功能
   - 首先要设置断点
   - 常用操作
     - step into 步进（会进入函数）
     - step into my code
     - step out 
     - step over 
     - run to cursor
2. logging
```python
logging.debug(u"a")
logging.info(u"b")
logging.warning(u"c")
logging.error(u"d")
logging.critical(u"e")
```
   - CRITICAL > ERROR > WARNING > INFO > DEBUG
   - 不设置级别，默认值显示warning,error,critical.
   - logging.basicConfig(level=logging.NOTSET)  # 设置日志级别(无级别全显示)
        - 可选参数为上面五个（注意大写）


3. 

# 内置库
- deque
> list #是类似堆栈，先进后出，用append 和 pop，如果要先进先出，也可以实现，但是速度相对较慢，可用下面这种。
```python
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  
queue.popleft()

```

# 其他
- round
```python
round函数，不是真正意义上的四舍五入
#1.Round(1.5) =2   Round(2.5)也等于2,这是因为Python3更改了特性，向偶数取整。
#2.The behavior of round() for floats can be surprising: 
#for example, round(2.675, 2) gives 2.67instead of the expected 2.68. 
#This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float.

math.ceil "Return the ceiling of x as an Integral."
math.floor "the floor of x as an Integral."	math.trunc(-1.5)= -2
math.trunc "Truncates x to the nearest Integral toward 0 " math.trunc(-1.5)= -1
```
- sort and sorted
```python
	sort是数组的排序，sorted是针对所有可迭代对象的排序
```

- math and cmath

  CMATH 用于科学计算。

- time
```python
time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
```

- `__future__`

  对于Python当前不 支持，但未来将成为标准组成部分的功能，你可从这个模块进行导入。 

- #!/usr/bin/env python 

  不管Python库位于什么地方，这都将让你能够像运行普通程序一样运行脚本。 

  - 添加#!/usr/bin/env python

  - $ chmod a+x hello.py 

  -  $ hello.py （包含在执行路径中），./hello.py （未包含在执行路径中 ）（即是否在path中）

    

-  find

  方法find在字符串中查找子串。如果找到，就返回子串的第一个字符的索引，否则返回-1。 

- yield
  - 可迭代
  - 只能读取==**一次**==
  - 实时生成数据，不全存内存中

- zip

  ```python
  obj =zip([1,2,3],['a','b','c'])
  #<zip object at 0x104c1d5c8>
  
  list(zip([1,2,3],['a','b','c']))
  #[(1, 'a'), (2, 'b'), (3, 'c')]
  
  dict(zip([1,2,3],['a','b','c']))
  #{1: 'a', 2: 'b', 3: 'c'}
  
  tuple(zip(*obj)) #=>解压zip
  #((1, 2, 3), ('a', 'b', 'c'))
  
  ```


# 作用域

如果有一个局部 变量或参数与你要访问的全局变量同名，就无法直接访问全局变量，因为它被局部变量遮 住了，可使用函数globals来访问全局变量 。

  在Python中，当引用一个变量的时候，对这个变量的搜索是按找本地作用域(Local)、嵌套作用域(Enclosing function locals)、全局作用域(Global)、内置作用域(builtins模块)的顺序来进行的，即所谓的LEGB规则。

当在函数中给一个变量名赋值是(而不是在一个表达式中对其进行引用)，Python总是创建或改变本地作用域的变量名，除非它已经在那个函数中被声明为全局变量. ”

- 如果只是想读取这种变量的值 (不重新关联它)，通常不会有任何问题。 

  ```python
  def combine(parameter): 
      print(parameter + external)
  external = 'berry'
  combine('Shrub')
  
  #像这样访问全局变量是众多bug的根源。务必慎用全局变量。
  
  def combine(parameter):
      print(parameter + globals()['parameter'])
  parameter = 'berry'
  
  #重新关联全局变量(使其指向新值)是另一码事。在函数内部给变量赋值时，该变量默认为 局部变量，除非你明确地告诉Python它是全局变量。那么如何将这一点告知Python呢?
  x = 1
  def change_global():
      global x 
      x=x+1
  change_global() 
  #x=>2
  
  nonlocal x 
  
  ```

  | global                       | nonlocal           |
  | ---------------------------- | ------------------ |
  | `global`的变量之前可以不存在 | nonlocal一定要存在 |
  | 用于任何位置 | 只能用于嵌套函数中 |
  | 找全局变量 | 找上层函数 |

# 正则表达式

- 在线调试 http://tool.oschina.net/regex

| syntax     | desc                                                         | e.g.           |
| ---------- | ------------------------------------------------------------ | -------------- |
| re1\|re2   | re1 or re2                                                   | foo\|bar       |
| .          | 匹配除\n外的任何字符                                         | b.b            |
| ^          | 匹配字符串的起始                                             |                |
| $          | 匹配终止部分                                                 |                |
| *          | 0或多次前面的字符或表达式                                    |                |
| +          | 1或多次                                                      |                |
| ？         | 0或1次， 非贪婪方式                                          |                |
| {n}        | 匹配前面的字符或表达式n次                                    | [0-9]{3}       |
| {m,n}      | 匹配前面的字符或表达式m到n次                                 |                |
| [.....]    | 匹配来自字符集的任意 `单一`字符                              | [aeiou]        |
| [..x-y..]  | 匹配来自字符集x-y的任意 `单一`字符                           | [0-9],[A-Za-z] |
| [^..x-y..] | 非字符集内的单一字符                                         |                |
| re?        | 非贪婪匹配（直接在表达式后）                                 | .*?[a-z]       |
| (...)      | 匹配封闭的正则表达式，然后另存为子组                         |                |
| \d         | 十进制数字（等于[0-9]).  大写相反                            |                |
| \w         | 任何字母或数字和下划线（等于[a-zA-Z0-9_]）大写相反           |                |
| \s         | 任何空格字符[\n\t\r\v\f] 大写相反                            |                |
| \N         | n=int,匹配子组的第N个                                        |                |
| \          | 特殊字符转义                                                 | `\\`           |
| (?:)       | 表示一个匹配不用保存的分组                                   |                |
| (?=.com)   | 如果一个字符串后面跟着“.com”才做匹配操作，并不使用任何目标字符串 |                |
| (?iLmsux)  | 在正则表达式中嵌入一个或者多个特殊“标记”参数(或者通过函数/方法) | (?x)，(?im)    |

## 核心函数和方法

- match()

   ```python
     a='{1}{2}{3}{4}'
     m=re.match('({.*})',a)
     m.groups()  #=>('{1}{2}{3}{4}',) 贪婪匹配
   ```

  a='{1}{2}{3}{4}'
  m=re.match('({.*?})',a)
  m.groups()  #=>('{1}',) 非贪婪匹配

  line = "Cats are smarter than dogs";
  matchObj = re.match( r'dogs', line, re.M|re.I)
   ```

  

  ### 常用修饰符（flags）

  | 修饰符 | 描述                                                         | 解释          |
  | ------ | ------------------------------------------------------------ | ------------- |
  | re.I   | 使匹配对大小写不敏感（大写I）                                | re.IGNORECASE |
  | re.M   | 多行匹配， ^和$分别匹配目标字符串中行的起始和结尾，而不是严格匹配整个字符串本身的起始 和结尾 | re.MULTILINE  |
  | re.S   | 使 . 匹配包括换行在内的所有字符                              |               |

   ```python
  #也可以写在表达式中，用小写代替
  #(?i...)
  #(?im)
  a='HELLO'
  m =re.match('hello',a) #=>None
  m =re.match('(?i)hello',a) #=>'HELLO'
  #等同于
  m=re.match('hello',a,re.I) 
   ```

  

- search()

  和match的区别是，match是从头匹配，而这个是从第一个匹配的字符开始，不一定是最开始。

- complie()

- group() groups()区别  

| 情况           | group()                   | groups()           |
| -------------- | ------------------------- | ------------------ |
| 匹配，无子组： | `group()返回整个匹配对象` | 返回空元组`()`     |
| 匹配，有子组   | `group(1)..返回特定子组`  | 返回所有子组的元组 |
| 不匹配         | ` AttributeError `        | ` AttributeError ` |

- findall(),  finditer()

  - findall()总是返回一个列表 
  - finditer()返回的是迭代对象

- sub()和subn()

  - subn()和 sub()一样，但 subn() 还返回一个表示替换的总数

  - **sub**(pattern, repl, string, count=0, flags=0) 

    将*string*中最左侧非重叠出现的*pattern*替换为*repl*，返回所获得的字符串。如果未找到该模式，则*字符串*将保持不变。*repl* 可以是一个字符串或一个函数；如果是一个字符串, 则会处理每个反斜杠转义。即，`\n`被转换为单个换行符，`\r`被转换为回车符，依此类推。

    ```python
    phone = "2004-959-559 # 这是一个电话号码"
    
    # 删除注释
    num = re.sub(r'#.*$', "", phone)  #=>'2004-959-559 '
    num = re.subn(r'#.*$', "", phone)  #=>('2004-959-559 ', 1)
    # 移除非数字
    num = re.sub(r'\D', "", phone) #=> '2004959559'
    num = re.subn(r'\D', "", phone) #=> ('2004959559', 13)
    ```

- re.split()

  - 如果给定分隔符不是使用特殊符号来匹配多重模式的正则表达式，那么 re.split()与 str.split()的工作方式相同 `re.split(':', 'str1:str2:str3') `

  - 复杂的例子

    ```python
    DATA=(
        'Moutain View, CA 94040',
        'Sunnyvale, CA',
        'Los Altos, 94023',
        'Cupertino 95014',
        'Palo Alto CA'
    )
    for datum in DATA:
        print(re.split(', |(?= (?:\d{5}|[A-Z]{2}))',datum))
        
    ###
    ['Moutain View', 'CA', ' 94040']
    ['Sunnyvale', 'CA']
    ['Los Altos', '94023']
    ['Cupertino', ' 95014']
    ['Palo Alto', ' CA']
    ###
    ```
