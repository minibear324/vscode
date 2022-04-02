# -*-coding:utf-8-*-
"""
@File name:字符和字符串.py
@Program IDE:PyCharm
@Create File Time:2022/4/2 16:31
@File Create By Author :echo
"""
import sys

# 使用内置的函数查看字符的ASCII，使用ord()
print(ord('a'))
# 查看字符的二进制,使用bin()
print(bin(97))

# 查看此编程软件是用的编码方式
print(sys.getdefaultencoding())

# 定义字符串
a = "python"
print(type(a))

# 序列及其基本操作
# 字符串有序排列的对象叫序列
# 使用“+”，进行两个字符串进行拼接
str1 = "python"
str2 = "book"
print(str1 + str2)

# 求字符串的长度
print(len(str1))

# 中文的定义及其长度
name = "陈霞"
print(len(name))

