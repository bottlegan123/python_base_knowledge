a = -1
b = -1
c = 3
# 计算a*x^2+b*x+c=0的根
x_1 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
x_2 = (-b - (b**2 - 4*a*c)**(1/2))/(2*a)
print(x_1)
print(x_2)

delta = (b**2 - 4*a*c)
x_11 = (-b + delta**(1/2))/(2*a)
print(x_11)

# python有自带的一些函数，但是很多其他的都需要导入包才能使用
import math
x1 = (-b + math.sqrt((b**2 - 4*a*c)))/(2*a)
x2 = (-b - math.sqrt((b**2 - 4*a*c)))/(2*a)
print(x1)
print(x2)

# 三个引号多行注释
'''
It fells good to drink iced juice on a hot summer day.
It maybe healthier if you drink bai kai shui.
D you know how to say bai kai shui in English.
The answer is plain boiled water.
Example: I want to drink plain boiled water more than anything else
'''