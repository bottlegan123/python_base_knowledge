# for循环对str（遍历每个字符）、list、tuple、dictionary进行操作；但不仅仅限制于对他们进行操作
"""
for循环的形式：
for 变量名 in 可叠代对象:  # 这里变量名是任意的他只是代表迭代对象里的每一个东西，但要前后对应
    你要进行的操作
"""

# 找出不正常的体温
body_temperature = [37, 37.6, 38.5, 19.0, 36.8]
# body_temperature = (37, 37.6, 38.5, 19.0, 36.8)替换成元组也是可以的
count = 0
for temperature in body_temperature:
    if temperature >= 38:
        print("危险！危险！危险！")
        count += 1
    else:
        print("安全！")
# 如果想知道有多少个人危险，怎么办?
print("危险的人有：" + str(count) + "个")

# 那么这个样子我们不知道是谁危险是谁安全呀！要解决这个问题就得用到字典了。
"""
字典里的循环有三个方法：
for i in 字典名.keys():  # 所以键
for j in 字典名.values():  # 所有值
for i, j in 字典名.items():  # 所有键:值对
"""
dict1 = {"100": "37", "101": "37.6", "102": "38.5", "103": "19.0", "104": "36.8"}
for staff_id, temperature in dict1.items():
    if float(temperature) >= 38:
        print(staff_id + "很危险")
    else:
        print(staff_id + "很安全")

# 上面写法和如下一样，字典每一个键:值对都可以看作是一个元组
for temperature_tuple in dict1.items():
    staff_id = temperature_tuple[0]
    temperature = temperature_tuple[1]
    if float(temperature) >= 38:
        print(staff_id + "很危险")
    else:
        print(staff_id + "很安全")


# for循环和range的联合使用
# range用来生成整数数列
# range(s1, sn, d)第一个为数列第一个元素，第二个为数列最后一个元素，d为步长
# range(s1, sn)是左闭右开的
total = 0
for a in range(1, 101, 1):
    total = total + a
print("总和为：" + str(total))








