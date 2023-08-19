# 在不知道循环进行多少次结束，但值得在什么情况下结束时用while循环
# for更加适用于循环次数明确
# while更加适合于循环次数未知

# 做一个求平均值的计算器，用户会持续输入数字，当用户输入q时计算器要能知道用户把所有数字输入完了
user_n = 0
total = 0
count = 0
while str(user_n) != "q":
    count = count + 1
    total = total + float(user_n)  # 和total += float(user_n)一样
    user_n = input("请输入数字:")
if count == 1:
    print("谢谢您的使用！")
else:
    print("您输入的数字平均值为：" + str(total / (count-1)))

# 以下会存在隐患：如果用户直接输入q那么print那里会出现0/0这是不允许的
print("您好呀！我是一个求平均值的计算器。😁")
user_num = input("请输入您的数字（终止程序请输入q）：")
total = 0
count = 0
while user_num != "q":
    count += 1
    total += float(user_num)
    user_num = input("请输入您的数字（终止程序请输入q）：")
if count == 0:
    print("谢谢您的使用！")
else:
    print("您所输入的数字的平均值为：" + str(total / count))


