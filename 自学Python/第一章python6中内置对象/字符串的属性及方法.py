# -*-coding:utf-8-*-
"""
@File name:字符串的属性及方法.py
@Program IDE:PyCharm
@Create File Time:2022/4/2 17:09
@File Create By Author :echo
"""

# 查看str的属性或者方法
print(dir(str))

# 还可以通过字符串来查看
s = "python"
print(dir(s))

# 查看具体方法的使用
print(help(s.index))

n1 = s.index('n')
print(n1)

a = "I LOVE PYTHON"
# split()分隔符,结果将是列表
list = a.split(" ")
print(list)

# 将所获取的列表进行拼接,使用join
b = "-".join(list)
print(b)

# 字符串格式化输出format
# 对占位符{}的填空，使用format
c = "I like {0} and {1}".format('python', 'JS')
print(c)

# 占位符的格式{0: 10},表示第一个空占10个字符，特别的，{1:>15}：表示第2的空占15个字符，并且要右对齐">"
d = "I like {0:10} and {1:>15}".format('python', 'JS')
print(d)

# 以下{0:4d}表示第一空必须填整数，而且不能超过四位；{1:.1f}表示第二个空填浮点数并只保留一位小数(四舍五入的方式)
e = "She is {0:4d} years old and {1:.1f}m in height".format(28, 1.68)
print(e)
