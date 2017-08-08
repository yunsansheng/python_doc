>>> 3 * 'un' + 'ium'  #代表重复*
'unununium'

#lambda
前面是参数，后面是公式。
lambda a, b: a+b
(lambda a=1 :a+1)()
(lambda a=1 :a+1)(2)

list #是类似堆栈，先进后出，用append 和 pop，如果要先进先出，也可以实现，但是速度相对较慢，可用下面这种。
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  
queue.popleft()

在序列中循环时，索引位置和对应值可以使用 enumerate() 函数同时得到:
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe

同时循环两个或更多的序列，可以使用 zip() 整体打包:
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.