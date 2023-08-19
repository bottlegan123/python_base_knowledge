# 子类会继承父类的属性和方法
# 子类有自己的属性或者方法时会先调用自己的，没有的话才会用父类的 语法是：class Cat(Mammal):
"""
如果子类里面有属性那么调用时只能用到子类的属性不能去找到父类的属性，
解决这个问题的方法是在定义的属性下面加 super().__init__()
"""

"""
小技巧：什么时候可以用继承呢？
当可以说成 什么什么是什么什么的时候可以用继承：
A是B  class A(B)
比如，人类和猫是动物，就可以把动物的属性和方法作为父类的
     新能源车和油车都是车，就可以把车作为父类
"""

# 类继承练习：人类系统
# - 员工分为两类：全职员工FullTimeEmployee，兼职员工PrtTimeEmployee
# - 全职员工与兼职员工都有"姓名 name"，"工号 id"属性
#   都具有打印信息 print_info （打印姓名和工号）的方法
# - 全职有"月薪属性 month_salary"
#   兼职有"日新属性 daily_salary"，"每月工作天数 work_days"
# - 全职和兼职都有"计算月薪的方法 calculate_month_salary"，但计算工程不同


class Employee:
    def __init__(self, name, id_number):
        self.name = name
        self.id = id_number

    def print_info(self):
        print(f"员工{self.name}的工号是{self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id_number, month_salary):
        super().__init__(name, id_number)  # 这一行表示继承父类，如果没有这一行而且子类也有自己的属性就会只用到子类的属性
        self.month_salary = month_salary

    # class FullTimeEmployee(Employee):
    #     def __init__(self, name, id_number, month_salary):
    #         self.month_salary = month_salary  这样子会直接掉调用子类的构造函数不会找父类了

    def calculate_month_salary(self):  # 如果子类有自己的方法就用自己的方法如果没有就用父类的
        return self.month_salary  # 这是唯一返还的值，打印也就只会打印这个


class PartTimeEmployee(Employee):
    def __init__(self, name, id_number, daily_salary, work_days):
        super().__init__(name, id_number)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_month_salary(self):
        return self.daily_salary * self.work_days  # 这个函数会返还这个结果


employee1 = FullTimeEmployee("小黄", "10012", 5000)
employee1.print_info()
# print(employee1())  # 这行代码运行不出来
print(employee1.calculate_month_salary())  # 函数里面返还的值要用这个函数计算之后才会有

employee2 = PartTimeEmployee("小黑", "10011", 120, 20)
employee2.print_info()
print(employee2.calculate_month_salary())

