import unittest

from my import bmi_calculate


class TestMy(unittest.TestCase):  # 括号前面的TestMyCalculate是类名（是可以随便取的），括号里面的unittest.TestCase是继承的父类
    # 2.定义测试用例
    def test(self):
        self.assertNotEqual(bmi_calculate(60, 1.7), 20)  # 断言不等于
