import unittest
import os
#导入测试类
from Basic.unittest_lesson.test_myClass import Test_myClass
from Basic.unittest_lesson.test_myClass2 import Test_myClass2
from HTMLTestRunnerNew import HTMLTestRunner

#实例化套件对象
s = unittest.TestSuite()
# #一、调用addTest来加载测试用例----addTest(类名("用例函数名称"))--添加一个测试用例
# s.addTest(Test_myClass("test_add"))
# s.addTest(Test_myClass("test_minus"))
#
# #二、加载多个测试用例--参数为列表-列表当中为测试用例
# #s.addTests([Test_myClass("test_add"),Test_myClass("test_minus")])
#
# #使用TextTestRunner来运行测试用例
# #打开一个文件
# fs = open("test_run_result.txt","w")
# #实例化
# runner = unittest.TextTestRunner(fs)
# #run方法运行测试用例
# runner.run(s)

#三、unittest.TestLoader.discover方法匹配目录下的用例文件
loader = unittest.TestLoader()
s.addTests(loader.discover(os.getcwd()))
fp = open(os.getcwd() + '/autoTest_{0}.html','wb')
runner = HTMLTestRunner(
           stream = fp,
           title = '单元测试报告',
           description = '单元测试报告',
           tester = 'zhihui'
           )
runner.run(s)


