# 替换一串字当中的一部分

contacts = ["小白", "小黄", "小黑", "小粉", "小拉"]
for name in contacts:
    massage1 = name + ",你好！" \
                     "你妈妈拿了两罐旺仔牛奶，" \
                     "在教务处等着你。"
    print(massage1)

# \n是打印出来的往下挪一行，\是写代码是代码往下挪一行但仍然看作是一起的

"""
律回春渐，心愿早起；
新岁甫至，福气东来；
金牛贺岁，欢乐祥瑞；
金牛敲门，五福临门；
给小白及家人们拜年啦！
新春快乐，牛年大吉！
"""
# 我想把上面祝福语中的属相换一下
animal = ["鼠", "牛", "虎", "兔"]
for animal in animal:
    massage2 = """律回春渐，心愿早起；
新岁甫至，福气东来；
金""" + animal + """贺岁，欢乐祥瑞；
金""" + animal + """敲门，五福临门；
给小白及家人们拜年啦！
新春快乐，""" + animal + """年大吉！"""  # 这样很不美观，怎么办呢？

massage3 = """律回春渐，心愿早起；
新岁甫至，福气东来；
金{0}贺岁，欢乐祥瑞；
金{0}敲门，五福临门；  
给{1}及家人们拜年啦！
新春快乐，牛年大吉！""".format("animal", "name")
# 大括号里的数字表示会用format里面的第几个进行替换
# {0}会被animal替换，{1}会被name替换
print(massage3)

massage3 = """律回春渐，心愿早起；
新岁甫至，福气东来；
金{current_animal}贺岁，欢乐祥瑞；
金{current_animal}敲门，五福临门；  
给{current_name}及家人们拜年啦！
新春快乐，牛年大吉！""".format(current_animal="兔", current_name="小白")
# 也可以根据关键词进行替换，这个时候顺序就不太重要了

# f-字符串
animal = "虎"
name = "小粉"
massage4 = f"""律回春渐，心愿早起；
新岁甫至，福气东来；
金{animal}贺岁，欢乐祥瑞；
金{animal}敲门，五福临门；  
给{name}及家人们拜年啦！
新春快乐，牛年大吉！"""
# 可以把大括号及里面的东西替换成先前定义的

gpa_dict = {"小黄": 3.56, "小白": 4.32, "小黑": 4.12}
for name, gpa in gpa_dict.items():  # 遍历字典的键和值对
    print(name + "的gpa是" + str(gpa))

for name, gpa in gpa_dict.items():
    print("{0}的当前绩点是：{1}".format(name, gpa))

for name, gpa in gpa_dict.items():
    stud_name = name
    stud_gpa = gpa
    text = f"{stud_name}你的当前绩点为：{stud_gpa:.1f}"  # :.1f表示保留小数点后一位
    print(text)

for name, gpa in gpa_dict.items():
    stud_name = name
    stud_gpa = gpa
    print(f"{stud_name}你的当前绩点为：{stud_gpa:.1f}")
# 那还要换名字怎么办呢？











