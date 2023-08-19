# 求字符串长度
s = "hello world!"  # 引号包住是字符串
len(s)  # 什么都不会出现，字符串长度是数
print(len(s))  # print之后才会有值输出

# len()函数可以用于str、列表、字典、元组

# 获取字符串中的单个字符
print(s[0])
print(s[11])
print(s[len(s)-1])

# bool
b1 = True
b2 = False

# None 空值
n = None

print(type(s))
print(type(b1))
print(type(n))
print(type(0.5))

print(len(b1))  # 会报错，因为函数和数据类型对应错误了
# 数据类型都有自己对应的函数可以使用，对应错误时运行就会报错
