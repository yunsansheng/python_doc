# erro 初始化时,不要覆盖掉方法。

```python
class Trymis(object):
	def __init__(self):
		self.a=[]
		self.run=self.run()

	def run(self):
		self.a.append(1)
```

# erro 初始化时,变量在使用前赋值。

```python
#这里会出现错误，因为先初始化self.runres时，a还没有初始化。
class Trymis(object):
	def __init__(self):
		self.runres=run()
		self.a=[]

	def run(self):
		self.a.append(1)
```
