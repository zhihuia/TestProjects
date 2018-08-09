#Author: Cheese
#Time: 2018/5/28
import unittest
from Common.DoExcel import DoExcel
from Common.MyRequest import send_request
import ddt
from Common import myLogger2
import logging
from Common.myLogger import my_logger
import re

# 获取所有的测试数据
de = DoExcel("/Users/gemii/TestProjects/API_Framework/TestDatas/api_info_1.xlsx")
#de = DoExcel("D:\\PythonStudy\\python6_basic\\API\\TestDatas\\api_info_1.xlsx")
all_case_datas = de.get_all_caseDatas()

@ddt.ddt
class Test_API_V1(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("========start test========")

    @classmethod
    def tearDown(self):
        #在所有测试用例执行完成之后，更新初始化手机号码到excel中，下一次再读取测试数据时为新的手机号码
        de.update_init_phone()
        de.save_data("/Users/gemii/TestProjects/API_Framework/TestDatas/api_info_1.xlsx")



    # def test_register(self):
    #     #调用发送接口请求数据的方法，将所有测试用例的测试数据发送出去
    #     for casedata in self.all_case_datas:
    #         res_obj = send_request(casedata["method"],casedata["url"],casedata["request_data"])
    #     #断言--比对相应结果是否相等
    #     self.assertEqual(casedata["expected_data"],res_obj.text)   #text获取响应体


    @ddt.data(*all_case_datas)
    def test_register(self,casedata):
        #my_logger.info("========开始一个接口测试========")
        logging.info("========开始一个接口测试========")
        logging.info("请求url为：\n{0}".format(casedata["url"]))
        logging.info("请求方法为：{0}".format(casedata["method"]))
        logging.info("请求数据为：\n{0}".format(casedata["request_data"]))
        #调用发送接口请求数据的方法，将所有测试用例的测试数据发送出去
        res_obj = send_request(casedata["method"],casedata["url"],casedata["request_data"])
        logging.info("响应的结果为：\n{0}".format(res_obj.text))
        #断言--比对相应结果是否相等
        try:
            #判断比对方式--来选择比对方法
            if casedata["compare_type"] == 1:
                self.assertIsNotNone(re.search(casedata["expected_data"],res_obj.text))
            else:
                self.assertEqual(casedata["expected_data"],res_obj.text)  # text获取响应体
            logging.info("期望结果与实际结果匹配，用例成功！")
        except Exception as e:
            logging.error("期望结果与实际结果不匹配，用例失败！")
            logging.exception("断言异常：")
            raise e



