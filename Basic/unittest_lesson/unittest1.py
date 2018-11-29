#Author: Cheese
#Time: 2018/11/28 23:23

import unittest

class Test_Math(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("在所有测试用例执行之前，只执行一次=====")

    @classmethod
    def tearDownClass(cls):
        print("在所有测试用例执行之后，只运行一次的环境清理函数====")

    # def setUp(self):
    #     print("测试用例运行之前，初始化操作====")  #每一个测试用例执行之前，都会执行一次
    #
    # def tearDown(self):
    #     print("测试用例运行完成之后，收尾操作====")

    def test_addTwoNum(self):
        print(5 + 7)

    def test_minusTwoNum(self):
        print(10 - 2)


if __name__ == "__main__":
    unittest.main()