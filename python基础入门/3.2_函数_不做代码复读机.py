# 函数括号，括号里面放想要掉入的参数
# python内置函数：print(), type(), sum()

# 定义一个求扇形面积的函数
def calculate_sector(radius, central_angle):
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print("扇形面积为：" + str(sector_area))


calculate_sector(3, 60)


def calculate_sector(radius, central_angle):
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print(f"扇形面积为：{sector_area}")


calculate_sector(3, 60)


def calculate_sector(radius, central_angle):
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print("扇形面积为：{0}".format(sector_area))


calculate_sector(3, 60)


# 计算出来了但是没有新的变量来储存这些计算结果，要是我们想用这些结果就不方便了
"""
作用域：
函数里面的东西只能在函数里面使用，在函数里面定义的只是局部变量，只作用于函数里面；函数运行某一段代码和直接运行某一段代码是不一样的
函数的结果只能在函数中使用要通过一定方法才能在函数外部使用：return

print()和[1, 4, 3].append(7)是不带返回值的函数，如果你打印这两个函数的结果输出会是None
len()和sum()都是带返回值的函数，如果你打印这两个函数时会有结果输出
"""


def calculate_bmi(height, weight):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        category = "您的BMI分类为：偏廋"
    elif 18.5 < bmi <= 25:
        category = "您的BMI分类为：正常"
    elif 25 < bmi <= 30:
        category = "您的BMI分类为：偏胖"
    else:
        category = "您的BMI分类为：肥胖"
    print("{bmi_category}".format(bmi_category=category))
    return bmi


bmi1 = calculate_bmi(1.7, 47)
print(bmi1)

print(calculate_bmi(1.7, 47))  # 函数后面一定得跟括号为了能输入参数


# 如果不加return就会返回出空值None
def calculate_bmi(height, weight):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        category = "您的BMI分类为：偏廋"
    elif 18.5 < bmi <= 25:
        category = "您的BMI分类为：正常"
    elif 25 < bmi <= 30:
        category = "您的BMI分类为：偏胖"
    else:
        category = "您的BMI分类为：肥胖"
    print("{bmi_category}".format(bmi_category=category))


calculate_bmi1 = calculate_bmi(1.7, 47)
print(calculate_bmi1)