# 程序错误类型
# a = ["s", 9, "f"]
# print(a[4])  # 索引错误，索引超过了列表长度

# IndexError  索引错误
# zeroDivisionError  除零错误
# FileNotFound  打开的文件不存在
# TypeError  类型错误，比如两个字符串做乘法
# IndentationError  缩进错误
# ImportError  倒入模块错误
# KeyError  键错误
# AttributeError  属性错误
# SyntaxError  语法错误
# ValueError

# try except else finally

# 错误不仅仅会来自程序本身，而且可能来自用户的使用
try:
    user_height = float(input("您的身高是（单位：m）："))
    user_weight = float(input("您的体重是（单位：kg）："))
    user_BMI = user_weight / user_height ** 2
# 传入的是不能转换为数字的那么就会出现ValueError
except ValueError:
    print("您输入的不是合理数字，请重新运行程序输入正确的数字类型")
# 用户误把自己的身高输入为0
except ZeroDivisionError:
    print("您输入的身高不合理，请重新运行程序输入正确的身高")
# 有时候并不能预测所有错误，以下会捕捉所以错误
except:
    print("发声未知错误，请您重新运行程序")
# try except执行语句从上往下执行，只有第一个符合条件的except分支会运行
else:  # else后面缩紧放正确时会执行的语句
    print("您的BMI值是：" + str(user_BMI))
finally:  # finally后面缩进放无论正确与否都会执行的
    print("感谢您的使用！")

# 代码测试完了整个程序就结束了，也不会往下面运行了
