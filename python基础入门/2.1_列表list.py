# 为什么要用列表呢？比如说，你要对十个东西进行赋值如果一个一个赋值就太麻烦了
# item1 = 1
# item2 = 2.......这个时候用列表就容易许多
# 列表就是把相似的东西放在一块，python里面的列表可以放不同类型的数据很灵活
list_shop = ["item1", "item2", "item3"]


# 如何往定义好地列表表里面加东西？针对·列表的方法（方法和函数有点像）
# 方法一般在操作对象后面加点.list_shop.append()，对象.方法名()；函数是在函数后面加括号len("")，函数(对象)
"""注意使用append时一次只能加一个元素否则会报错"""
t = ["item1", "item2", "item3", "item4"]
t1 = t.append("item5")  # 这里只会操作t.append("item5")
# 列表不能重名不然无法识别是哪一个，就好像所有列表都占有自己的地位不会被替代

"""
列表是能可以直接对其进行操作的不需要重新命名；
而str、int、float、bool是不可变的不能往里面添加元素也不能删除里面的元素，
比如说如果你有一个浮点数 s = 0.9，这是你想要一个新的浮点数但是不需要0.9了，
你该怎么做呢？可以 s = 0.8这个时候你是对s重新赋予值不是对s进行变化操作
"""
print(t1)  # 会打印出None，因为方法是对原来列表进行操作的过程没有生成列表

t.append("item5")  # .append()是直接对原来的t进行操作
t1 = t
print(t1)  # 这个时候就可以输出['item1', 'item2', 'item3', 'item4', 'item5']
# 或者不用重新赋值
t.append("item6")
print(t)

# 如何移除定义好地列表表里面加东西？
t.remove("item5")  # 用remove时必须要这个列表也是存在才不会报错
print(t)

# 列表和其他数据类据(str bool int float)不同之处：列表可变，数据不可变
# 数据不可变例子
s = "Hello"
print(s.upper())  # 把字母变成全部大写字母的方法
print(s)  # 这里仍然输出Hello
# 怎么让打印出来的s是新的s呢？
s = "Hello"
print(s.upper())
s = s.upper()
print(s)

# 列表可变例子
t.append("item7")  # 正确
t = t.append("item7")  # 错误


# 列表可以用len求长度，长度是列表里面元素多少；可以索引，索引和字符串类似
lb = [1, "hello", True, 1.3]
len(lb)
lb[0] = 2  # 将列表里面的元素重新赋值
print(lb)

num_list = [1, 2, 4, 6, 9]
print(max(num_list))
print(min(num_list))
print(sorted(num_list))  # 打印排序后的列表，sorted和sort是不同的类型
print(sum(num_list))
print(sum(num_list) / len(num_list))  # python没有直接求平均值的只能另寻他法
# 以上都会返回值或者新列表
max_num_list = max(num_list)
sorted_num_list = sorted(num_list)



