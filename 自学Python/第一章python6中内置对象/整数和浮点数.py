# -*-coding:utf-8-*-
"""
@File name:整数和浮点数.py
@Program IDE:PyCharm
@Create File Time:2022/4/2 15:48
@File Create By Author :echo
"""
# 查看类型type()
print(type(2))
print(type(3.14))

# 对整数和浮点数进行转化
# 浮点数转化成整数
print(int(3.14))
# 整数转化成浮点数
print(float(2))

# 查看每一个对象在计算机中的内存地址
print(id(3))
print(id(3.0))
# 以上两个对象肯定是不一样的内存地址，因为一个是整形的3，而另一个是浮点数3.0

# python中的一个内置函数用来做除法
print(divmod(5, 2))

# 浮点数的加法在python中，会因为进制转化时而出现问题
print(0.1 + 0.2)
# 结果并非是0.3而是0.30000000000000004
# 使用round()函数能解决绝大部分这样的问题
a = round(0.1 + 0.2, 2)
print(a)
# 当然还可以采用科学记数法的方式，也可以有效地解决这一部分的问题

# 使用help()查看函数的使用
help(round)

