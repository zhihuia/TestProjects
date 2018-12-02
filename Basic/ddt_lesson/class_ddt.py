import ddt
import unittest

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]


@ddt.ddt
class TestDdt(unittest.TestCase):
    # 第一种用法
    # @ddt.data(1,2,3,4,5,6,7)
    # def test_print(self,a):
    #     print(a)

    # 第二种用法
    # @ddt.data([1,2,3],[10,11,13])
    # @ddt.unpack
    # def test_add_my(self,a,b,c):   # 有几个值，传几个参数
    #     print(a + b +c)

    # 从一个变量中取值，变量是字典或者列表--表达式：*变量名
    @ddt.data(*data)
    def test_print(self, a):
        print(a)
