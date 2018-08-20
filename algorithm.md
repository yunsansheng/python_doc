# 1. 桶排序

- 排序对象必须已知
- 桶排序可以应用在排列考试成绩等等的场景里面
- 排序较快，但是浪费空间，对小数的排序也非常的麻烦
- 用O表示时间复杂度,同排序时间复杂度是O(m+n+m+n)即O(2*(m+n))。

> 我们在说时间复杂度的时候可以忽略较小的常数，最终桶排序的时间复杂度为O(m+n)。

## 代码示例
```python
lst=[5,3,5,1,8]

def bucket_sort(lst):
    buckets = [0] * ((max(lst) - min(lst)) + 1)
    for i in range(len(lst)):
        buckets[lst[i] - min(lst)] += 1
    res=[]


    for i in range(len(buckets)):
        if buckets[i] != 0:
            #num*count
            res+=([i+min(lst)]*buckets[i])
    return res

#bucketsort(lst)


#冒泡(每次比较相邻的两个数)
#复杂度是O(N**2)。时间复杂度非常高
def bubble_sort(lst):
    count=len(lst)
    #每一趟只能将一个数归位, 如果有n个数进行排序,只需将n-1个数归位，循环n-1次
    for i in range(count-1):
        #完成一次完整交换
        for j in range(count-i-1):
            if lst[j] <lst[j+1]:
                #change
                lst[j],lst[j+1] =lst[j+1],lst[j]

    return lst

#bubble_sort(lst)
```


# 2. 快速排序(最常用的排序)
- 快速排序的最差时间复杂度和
- 冒泡排序是一样的，都是O(N2)，它的平均时间复杂度为O (NlogN)。
- 快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。

## 步骤
- 从数列中挑出一个元素，称为”基准”（pivot），
- 重新排序数列，所有元素比基准值小的摆放在基准前面，
- 所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
- 在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
- 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

## 代码示例
```python
def quick_sort(list):
    less=[]
    pivot_lst =[]
    more =[]

    #递归出口
    if len(list)<=1:
        return list
    else:
        #将第一个数作为基准
        pivot= list[0]
        for i in list:
            #将比基准小的数放到less数列
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot_lst.append(i)
        less=quick_sort(less)
        more =quick_sort(more)
        return less +pivot_lst+more

quick_sort(lst)
```

```
#queue 队列  先进先出，头出 尾进

#stack 栈   先进后出

#堆  heap
```