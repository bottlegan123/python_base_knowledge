print("您好，吃了吗，张三")
print("您好，吃了吗，李四")
print("您好，吃了吗，王五")

greet = "你好，吃了吗"
# 变量命名只能用文字、数字、下划线，变量名不能以数字开头，变量名大小写敏感
print("greet，张三")  # 如果没有其他操作，那么在引号里面识别成了字符串
print("greet，李四")
print("greet，王五")

print(greet + "，张三")
print(greet + "，李四")
print(greet + "，王五")

greet = "你好，吃了吗"
greet_Chinese = greet
greet_English = "Yo what's up"
print(greet_Chinese + "，张三")
print(greet_English + "，张三")
