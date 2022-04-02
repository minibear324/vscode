# -*-coding:utf-8-*-
"""
@File name:标准库中的math.py
@Program IDE:PyCharm
@Create File Time:2022/4/2 16:12
@File Create By Author :echo
"""

import math
import decimal

# 查看math模块中的所有函数dir()
print(dir(math))

# 使用math中的pi值(圆周率)
print(math.pi)

# 使用math中的pow(指数函数)
print(math.pow(2, 3))

# 查看pow如何使用
print(help(math.pow))

# 指数的普通使用方法
print(2**3)

# 确保两浮点数相加的值为精确值
# 此时要添加decimal模块
numb1 = decimal.Decimal('0.1')
numb2 = decimal.Decimal('0.2')
print(numb1 + numb2)

# 要注意数值溢出的问题，以下是极限
print(2 ** 1000)
# 再增加一位小数
print(2 ** 1000 * 0.1)