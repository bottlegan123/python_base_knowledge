# 函数后面加括号()就会是函数的执行结果

def square_calculate(num):
    return num * num


def tri_calculate(num):
    return num ** 3
# 这样子算计次方很麻烦，要是我要计算从一到十此方怎么办呢，定义是个函数吗？


def calculate(num, exponential):
    result = num ** exponential
    print(f"""
| 数字参数 | {num} |
| 函数形式 ｜ {exponential} |
| 计算结果 ｜ {result} |"""
          )
calculate(2, 3)


# 如果还要一个加十的运算呢？
def plus_10(num):
    return num + 10

def calculate_square(num):
    return num ** 2

# 高阶函数：把函数传入函数；不带括号是函数本身，带括号是函数返回的结果
def calculate_and_print(num, function):
    result = function(num)
    print(f"""
| 数字参数 | {num} |
| 函数形式 ｜ {function} |
| 计算结果 ｜ {result} |
""")

calculate_and_print(2, plus_10)

# 有时我们传给高阶函数的函数不是很常用，你们每次都定义一下略嫌麻烦
# 匿名函数可以解决这个总是重复定义的麻烦，匿名函数只能用一次
# 匿名函数的样子： lambda 变量名（传给匿名函数的参数）: 变量名的运算形式（会直接又返回结果，不需要return）
# lambda num: num * 2; lambda num1, num2: num1 * num2
# 匿名函数定义好之后的调用方式 (lambda num: num * 2)(参数)，匿名函数要括号括住表示一个整体
# 匿名函数只能用于简单的返回值的运算，多个语句/表达式或者涉及循环递归的都不能使用匿名函数
def calculate_print_2(num):
    result = (lambda num: num+10)(num)
    print(f"""
| 数字参数 | {num} |
| 计算结果 ｜ {result} |
    """)
calculate_print_2(2)
