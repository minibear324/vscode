# -*-coding:utf-8-*-
"""
@File name:列表.py
@Program IDE:PyCharm
@Create File Time:2022/4/2 17:34
@File Create By Author :echo
"""

# 列表的定义
lst = []
print(type(lst))

# 元素特点
# 顺口溜：列表是个框，什么都能装（python中各种类型的对象，包括自己定义的对象）
a_lst = [2, 3, 3.14, "python lesson", []]
b_lst = [3, 2, 3.14, "python lesson", []]
# 列表是有顺序的，这两个列表的元素都一样，但是他们的存储单元不相同
print(id(a_lst), id(b_lst))

# 索引和切片
# 跟字符串的索引和切片差不多
print(a_lst[0])
print(a_lst[-3])
print(a_lst[::-1])

# 基本操作
# 更改列表中的某个值
a_lst[0] = 100
print(a_lst)

# 求列表长度
print(len(a_lst))

# 检验某个字符是否在列表中
print(100 in a_lst)
print(1 not in a_lst)

# 列表的乘法
print(a_lst * 2)

# 列表的加法
print(a_lst + b_lst)
