# 常用

## 读取／写入

### load_workbook("filename")

```python
import openpyxl
wb =openpyxl.load_workbood("filename")

wb.sheetnames
#['test', '12', '23']

wb.active 
#<Worksheet "test"> 当前激活的sheet

sheet=wb['test']
#<Worksheet "test">

sheet.title
#'test'

## 访问单元格
c=sheet["A1"] #=><Cell Sheet1.A1>
c.value #=> value
c.row  # row number  1
c.column # colum name A
C.coordinate # A1

##获取多个单元格，用切片的形式，可以行，列或矩形
sheet["A1":"A3"]  #一列三行
#((<Cell 'test'.A1>,), (<Cell 'test'.A2>,), (<Cell 'test'.A3>,))
sheet["A1":"C1"]  #一行三列
#((<Cell 'test'.A1>, <Cell 'test'.B1>, <Cell 'test'.C1>),)
sheet["A1":"C3"] # 三行三列，迭代需要用两个for循环
'''
(
    (<Cell 'test'.A1>, <Cell 'test'.B1>, <Cell 'test'.C1>), 
	(<Cell 'test'.A2>, <Cell 'test'.B2>, <Cell 'test'.C2>), 
    (<Cell 'test'.A3>, <Cell 'test'.B3>, <Cell 'test'.C3>)
)
#！返回的是generator,可以用tuple输出为元组
'''


## cell
sheet.cell(row=1,column =2)  #<Cell Sheet1.B1>

## row column
sheet.max_row
sheet.max_column
tuple(sheet.rows)[1]
#(<Cell 'test'.A2>, <Cell 'test'.B2>, <Cell 'test'.C2>, <Cell 'test'.D2>, <Cell 'test'.E2>, <Cell 'test'.F2>, <Cell 'test'.G2>, <Cell 'test'.H2>)
tuple(sheet.columns)[1]
#(<Cell 'test'.B1>, <Cell 'test'.B2>, <Cell 'test'.B3>, <Cell 'test'.B4>, <Cell 'test'.B5>, <Cell 'test'.B6>, <Cell 'test'.B7>, <Cell 'test'.B8>, <Cell 'test'.B9>, <Cell 'test'.B10>, <Cell 'test'.B11>)
sheet.column_dimensions["B"] #Col
sheet.row_dimensions[1]  # ROW
#col.font = Font(bold=True)

from openpyxl.cell.cell import get_column_letter,column_index_from_string
from openpyxl.utils import get_column_letter,column_index_from_string
get_column_letter(1) #=> 'A'
column_index_from_string('A') #=>1




```



### Workbook()

```python
import openpyxl
wb =openpyxl.Workbook()
wb.save('example_copy.xlsx')
#当修改Workbook 对象或它的工作表和单元格时，电子表格文件不会保存，除非你调save()方法

#不管新文件还是旧文件，想保存，一定要用save
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_active_sheet()
sheet.title = 'Spam Spam Spam'
wb.save('example_copy.xlsx')



## create sheet
wb.create_sheet(index,title)
wb.create_sheet(index=0, title='First Sheet')

## remove sheet
wb.remove_sheet(wb["sheet1"])
#remove_sheet()方法接受一个 Worksheet 对象作为其参数，而不是工作表名称的字符串。在添加或删除工作表之后，记得调用 save()方法来保存变更


##写入单元格
sheet['A1'] = 'Hello world!'
sheet['A1'].value = 'Hello world!' #最好是用.value属性，来防止冲突


```



### style

```python
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
'Alignment', 'Border', 'Color', 'DEFAULT_FONT', 'Fill', 'Font', 'GradientFill', 'NamedStyle', 'NumberFormatDescriptor', 'PatternFill', 'Protection', 'Side'

'absolute_import', 'alignment', 'borders', 'builtins', 'cell_style', 'colors', 'differential', 'fills', 'fonts', 'is_builtin', 'is_date_format', 'named_styles', 'numbers', 'protection', 'proxy', 'styleable', 'stylesheet', 'table'

#https://openpyxl.readthedocs.io/en/stable/styles.html

```



### 公式

```python

```



如果你希望看到该公式的计算结果，而不是原来的公式，就必须将 load_workbook()的 data_only 关键字参
数设置为 True。这意味着 Workbook 对象要么显示公式，要么显示公式的结果，不
能兼得（但是针对一个电子表格文件，可以加载多个 Workbook 对象）



### 设置行高和列宽

```python
 sheet.row_dimensions[1].height = 70 # 行高
 sheet.column_dimensions['B'].width = 20 #列宽
```



### 合并和拆分单元格

```python
sheet.merge_cells('A1:D3')
sheet.unmerge_cells('A1:D3')
```



