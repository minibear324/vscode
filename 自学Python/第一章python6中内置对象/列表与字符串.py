# -*-coding:utf-8-*-
"""
@File name:列表与字符串.py
@Program IDE:PyCharm
@Create File Time:2022/4/2 17:51
@File Create By Author :echo
"""

# 异同点：
#     都是序列
#     列表是容器类对象，列表可变
#     字符串不可变
# 列表是可修改的容器
lst = [1, 2, 33, 4]
lst[2] = 100
print(lst)
# 字符串不可以修改

# 字符串与列表的转换
# 字符串变列表，会将字符串中的每一个字母转化为列表的每一个元素
s = "python"
lst1 = list(s)
print(lst1)
# 此时输出的是字符串
print(str(lst1))
# 列表转化成字符串
s = "".join(lst1)
print(s)
print(str(s))

