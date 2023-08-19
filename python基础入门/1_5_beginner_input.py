"""
input里面只能返回字符串

如何把字符串转变为数字呢？
例子：
    s = "666"
    print(int(s))
int()中的字符串只有确实可以转化为整数是才不会报错，比如说如下错误例子
print(int("heterogeneity") 就会报错，因为"heterogeneity"不能转化为数字
类似的float(),str()也能进行类型转化
"""

# print("您现在是20岁，" + "您十年后是" + 30 +"岁。")
# 会报错因为字符串不能和数字相加，那么怎么才能让他们连接再一起呢？
print("您现在是20岁，" + "您十年后是" + str(30) + "岁。")

# BMI = weight / (height ** 2)
'''
user_height = input("您的身高是（单位：m）：")
user_weight = input("您的体重是（单位：kg）：")
BMI = user_weight / (user_height)**2 这里会提示应该把字符串改为数字
怎么做呢？如下:
'''

user_height = float(input("您的身高是（单位：m）："))  # 这里得用浮点数不然身高体重就太不准确了
user_weight = float(input("您的体重是（单位：kg）："))  # 把冒号后面的赋给user_weight
user_BMI = user_weight / user_height**2
print("您的BMI值是：" + str(user_BMI))

# 计算欧式距离
import math
length = float(input("x方向距离："))
width = float(input("y方向距离："))
distance = math.sqrt(length**2 + width**2)
print("距离是：" + str(distance))













