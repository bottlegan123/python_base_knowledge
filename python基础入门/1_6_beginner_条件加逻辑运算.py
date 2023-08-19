weather_index = int(input("今天外面气温："))
if weather_index >= 30:
    print("今天不适合出去运动，在寝室学习")
else:  # weather_index < 30
    print("今天天气不错出去运动")



# 这里面是一段有错误的代码
""" 
weather_index = int(input("今天外面气温："))
if weather_index >= 30:
    print("今天不适合出去运动，在寝室学习")
print("今天很快乐！")  # 这里没有缩进说明条件语句结束了，所以下面会报错
else:  # weather_index < 30   # else不能独立于if存在的
    print("今天天气不错出去运动")
"""




user_height = float(input("您的身高是（单位：m）："))  # 这里得用浮点数不然身高体重就太不准确了
user_weight = float(input("您的体重是（单位：kg）："))
user_BMI = user_weight / user_height**2
print("您的BMI值是：" + str(user_BMI))

# 偏廋：user_BMI <= 18.5
# 正常：18.5 < user_BMI <=25
# 偏胖：25 < user_BMI
# 肥胖：30 < user_BMI
if user_BMI <= 18.5:
    print("此BMI属于偏廋范围")
elif 18.5 < user_BMI <= 25:
    print("此BMI属于正常范围")
elif 25 < user_BMI <= 30:
    print("此BMI属于偏胖范围")
else:
    print("此BMI属于肥胖范围")


# 条件语句嵌套
user_gender = input("您的性别是：")
if user_gender == "男":
    user_gender = 1
else:
    user_gender = 0

user_weight = float(input("您的体重是（单位：kg）："))
user_height = float(input("您的身高是是（单位：m）："))
user_BMI = user_weight / user_height**2

if user_gender == 1:
    if user_BMI < 18.5:
        print("先生您的BMI属于偏廋范围。")
    elif 18.5 < user_BMI <= 25:
        print("先生您的BMI属于正常范围。")
    elif 25 < user_BMI <= 30:
        print("先生您的BMI属于偏胖范围。")
    else:
        print("先生您的BMI属于肥胖范围")
else:
    if user_BMI < 18.5:
        print("女士您的BMI属于偏廋范围。")
    elif 18.5 < user_BMI <= 25:
        print("女士您的BMI属于正常范围。")
    elif 25 < user_BMI <= 30:
        print("女士您的BMI属于偏胖范围。")
    else:
        print("女士您的BMI属于肥胖范围")


# python的逻辑运算符有三个: and or not（与 或 非）
# 运算优先级为 not or and
# 举个例子：只有气温合适并且外面没有下雨的情况下才能出去运动
temperature = float(input("今天的气温是："))
weather = input("今天的天气是：")
if temperature <= 30 and (weather != "下雨" and weather != "下雪"):
    print("今天可以出去玩")
else:
    print("呆在寝室学习吧！")







