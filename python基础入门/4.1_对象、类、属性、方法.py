"""
面向对象编程与面向过程的区别：（他们各有优缺点）
面向过程是把变成过程拆分成一个个步骤
可以这么理解面向过程是编年体，面向对象是纪传体

封装、继承、多态：
封装：写类的人把内部实现细节隐藏起来看不到代码，使用的人只需要通过外部接口来使用
就好像是吧汽车组装起来，你不需要知道汽车里面的部件怎么装，只需要知道那个按钮是干什么的就好

继承：创建有层次的类，创建父类，子类可以继承父类中定义的东西，就不用反复定义了，减少代码的荣冗余

多态：

"""


# 创建一个可爱猫对象
class CuteCat:   # 定义类名时用大写字母分割
    # 构造对象属性的函数必须用__init__
    def __init__(self):  # self表示把属性绑定在对象本身上
        self.name = "Kaffee"


cat1 = CuteCat()  # 要把这个类赋值给某个变量才可以用变量用类的属性和方法
print(cat1.name)


class CuteCat:
    # 定义对象属性
    def __init__(self, cat_name, cat_age, cat_gender):  # 从输入的参数获取name的值
        self.name = cat_name
        self.age = cat_age
        self.gender = cat_gender

    # 定义对象拥有的方法
    def speak(self):  # 这里的self是为了让我们在方法里面去获取和修改对象绑定的属性
        print("喵 " * self.age)
    # 调用方法的语法：对象名.方法，cat2.speak

    # 有更多参数的方法
    def think(self, content):
        print(f"小猫{self.name}正在思考：" + content)


cat2 = CuteCat("kaffee", 3, "male")  # 对对象传入参数
cat2.think("去干嘛呢？")
print(f"小猫的年龄是{cat2.age}，性别是{cat2.gender}")
cat2.speak()  # speak并没有参数所以只要括号就可以了
print("Hi " * cat2.age)  # 字符串 * 数字：表示把字符串重复多少次


# 练习题
# 1. 属性包括学生姓名、学号、以及语数外三科成绩
# 2. 能够设置学生某科目的成绩
# 3. 能够打印出学生所有科目的成绩
class Student:
    def __init__(self, name, stu_id):  # 这里不能输入字典作为参数吧？
        self.name = name
        self.id = stu_id
        self.grade = {"语文": 0, "数学": 0, "英语": 0}

    def set_grade(self, course, grade):
        if course in self.grade.keys():
            self.grade[course] = grade  # 如果字典中有course这个键那么会改变这个键所对应的值

    def print_grade(self):
        print(f"学生{self.name}（学号：{self.id}）的成绩为：")
        for course in self.grade:
            print(f"{course}：{self.grade[course]}")


# 有了对象才能对对象进行操作
zheng = Student("郑", "100234")  # 把属性给一个对象
print(zheng.grade)
chen = Student("陈", "100235")
print(chen.name)

zheng.set_grade("语文", 96)
print(zheng.grade)

zheng.set_grade("语文", 92)
zheng.set_grade("数学", 96)
zheng.print_grade()
