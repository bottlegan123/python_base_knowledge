# 代码测试
# 用于test的文件还得以test开头
import unittest
from my_calculator import my_adder


class TestMyAdder(unittest.TestCase):
    def test_positive_with_positive(self):  # 这里必须以test开头命名，因为unittest只是别这种
        self.assertEqual(my_adder(3, 5), 8)

    def test_positive_with_negative(self):
        self.assertEqual(my_adder(1, -2), -1)

# unittest 要在终端输入python -m unittest才能运行


# assert 断言做判断 assert len("Hi") == 2
# 如果 assert 后面为true则无事发生继续运行后面的代码
# assert 1+2 > 6  # AssertError提醒不符合续期
# 一旦出现 AssertError 就会终止程序，不会运行后面的代码了
# 面对这种情况可以用专门做测试的库，可以一次性跑多个测试，并且会展示那些测试通过了那些没有
# unittest 单元测试，对最小可测试单元进行测试，python自带
# 测试代码毁于实现代码放在不同的文件中

# unittest.TestCase类的常见测试方法
"""
assertEqual(A, B)     -->  assert A==B
assertTure(A)         -->  assert A is Ture
assertIn(A, B)        -->  assert A in B

assertNotEqual(A, B)  -->  assert A != B
assertFalse(A)        -->  assert A is False
assertNotIn(A, B)     -->  assert A not in B  

assertTure 可以表示上面所以方法
assertTure(A == B)  assertTure(A != B)
assertTure(A in B)  assertTure(A not in B)

"""



