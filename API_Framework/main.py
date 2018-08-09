#Author: Cheese
#Time: 2018/8/7 22:23

import HTMLTestRunnerNew
import unittest
from TestCases import test_api_v1
from Common import dir_config
import time
from Common import myLogger2

s = unittest.TestSuite()
ul = unittest.TestLoader()
s.addTests(ul.loadTestsFromModule(test_api_v1))
curTime = time.strftime("%Y-%m-%d %H%M",time.localtime())
fp = open(dir_config.htmlreport_dir + '/API_autoTest_{0}.html'.format(curTime), 'wb')
runner = HTMLTestRunnerNew.HTMLTestRunner(
            stream=fp,
            title='QCD接口测试报告',
            description='QCD接口测试报告',
            tester="CC"
            )
runner.run(s)
