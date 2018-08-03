#Author: Cheese
#Time: 2018/5/28
import unittest
from Common.DoExcel import DoExcel
from Common.MyRequest import send_request
#import ddt


# 获取所有的测试数据
#de = DoExcel("/Users/gemii/TestProjects/API_Framwork/TestDatas/api_info_1.xlsx")
#de = DoExcel("D:\\PythonStudy\\python6_basic\\API\\TestDatas\\api_info_1.xlsx")
#all_case_datas = de.get_all_caseDatas()

class Test_API_V1(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("========start test========")
        # 获取所有的测试数据
        de = DoExcel("/Users/gemii/TestProjects/API_Framwork/TestDatas/api_info_1.xlsx")
        self.all_case_datas = de.get_all_caseDatas()


    def test_register(self):
        #调用发送接口请求数据的方法，将所有测试用例的测试数据发送出去
        for casedata in self.all_case_datas:
            res_obj = send_request(casedata["method"],casedata["url"],casedata["request_data"])
        #断言--比对相应结果是否相等
        self.assertEqual(casedata["expected_data"],res_obj.text)   #text获取响应体











'''
@ddt.ddt
class Test_API_V1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("========start test========")

    @classmethod
    def tearDownClass(cls):
        #在所有测试用例完成之后，更新初始化手机号码到excel中
        #
        de.update_init_phone()
        de.save_data("路径")

        # # 获取所有的测试数据
        # de = DoExcel("D:\\PythonStudy\\python6_basic\\API\\TestDatas\\api_info_1.xlsx")
        # cls.all_case_datas = de.get_all_caseDatas()


    # def test_register(self):
    #     #调用发送接口请求数据的方法，将所有的测试用例的测试数据发送出去
    #     for casedata in self.all_case_datas:
    #         res_obj = send_request(casedata["method"],casedata["url"],casedata["request_data"])
    #         #断言  -比对响应结果是否相等
    #         self.assertEqual(casedata["expected_data"],res_obj.text)

    @ddt.data(*all_case_datas)
    def test_register(self,casedata):
        #调用发送接口请求数据的方法，将所有的测试用例的测试数据发送出去
        res_obj = send_request(casedata["method"],casedata["url"],casedata["request_data"])
        #断言  -比对响应结果是否相等
        self.assertEqual(casedata["expected_data"],res_obj.text)
'''