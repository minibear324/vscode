# -*-coding:utf-8-*-
"""
@File name:force.py
@Program IDE:PyCharm
@Create File Time:2022/4/2 16:24
@File Create By Author :echo
"""
# 求两力之和
import math
f1 = 20
f2 = 10
alpha = math.pi / 3

x_force = f1 + f2 * math.sin(alpha)
y_force = f2 * math.cos(alpha)

force = math.sqrt(x_force * x_force + y_force ** 2)

print("This result is: ", round(force, 2), 'N')
