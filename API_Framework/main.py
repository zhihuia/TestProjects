# Author: Cheese
# Time: 2018/8/7 22:23

import HTMLTestRunnerNew
import unittest
from API_Framework.TestCases import test_api_v1
from API_Framework.Common import dir_config
import time


s = unittest.TestSuite()
ul = unittest.TestLoader()
s.addTests(ul.loadTestsFromModule(test_api_v1))
curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
fp = open(dir_config.htmlreport_dir + '/API_autoTest_{0}.html'.format(curTime), 'wb')
runner = HTMLTestRunnerNew.HTMLTestRunner(
            stream=fp,
            title='接口测试报告',
            description='接口测试报告',
            tester="zhihui"
            )
runner.run(s)
