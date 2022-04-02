# -*-coding:utf-8-*-
"""
@File name:列表的方法.py
@Program IDE:PyCharm
@Create File Time:2022/4/2 17:51
@File Create By Author :echo
"""

# 修改列表内容
lst = [1, 2, 33, 4]
lst[2] = 100
print(lst)

# 给列表追加元素,append(),增加元素并不改变该列表的存储单元
lst.append("python")
print(lst)

# 给列表插入元素,insert(0,100)在索引为0的前面插入元素100
lst.insert(0, 100)
print(lst)

# 可迭代对象：字符串、列表
# 将一个可迭代的对象的元素添加至列表中extend()
lst2 = ['a', 'b']
lst.extend(lst2)
print(lst)

# 添加可迭代对象的元素特点
lst.extend("book")
print(lst)

# 删除列表元素
# 默认删除最后一个元素
print(lst.pop())
print(lst)

# 删除指定元素，根据索引
print(lst.pop(0))
print(lst)

# 删除指定元素，根据列表元素，并且默认删除遇到的第一个元素,remove()
print(lst.remove('b'))
print(lst)

# 清空列表clear()
print(lst2.clear())
print(lst2)

# 对列表内容的元素进行排序sort(),这时列表只能是同一类型才能排序
help(lst.sort)
lst3 = [1, 2, 4, 676, 4, 3, 3]
lst3.sort()
# 默认为升序
print(lst3)
# 改成降序
lst3.sort(reverse=True)
print(lst3)

# 通过切片的方式，再将lst3改成升序排列
print(lst3[::-1])
print(lst3)

# 列表排序之reverse()方法
lst3.reverse()
print(lst3)

# sorted()函数进行排序,会生成一个新的对象，并且对原来的列表不改变
lst3.append(5)
print(lst3)
lst4 = sorted(lst3)
print(lst3)
print(lst4)

# reversed()函数进行排序,会生成一个新的对象，并且对原来的列表不改变
lst5 = reversed(lst3)
# 会产生一个迭代器对象，这个结果并不会显示我们想要的
print(lst5)
# 我们可以按照以下的规则，将里面的元素读入内存里面，再显示到显示屏上
list(reversed(lst3))
# 下列不行，不知道为什么
# list(lst5)



