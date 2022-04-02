# -*-coding:utf-8-*-
"""
@File name:字符串的索引和切片.py
@Program IDE:PyCharm
@Create File Time:2022/4/2 16:47
@File Create By Author :echo
"""

# 一个序列是可以对其进行编号，从左往右，从0开始；从右往左，从-1开始，这些情况下，都包含空格
str1 = "python"
str2 = "book"
all = str1 + str2
print(all)
# 索引
print(all[0])
print(all[-2])

# 切片
print(all[1: 9: 1])
# 第三个参数为步长，默认为1，步长为正时，表示从左往右切片，步长为负数时，表示从右往左切片
# 逆序输出
print(all[::-1])

print(all[-10: 8: 2])
print(all[8: -10: -2])

