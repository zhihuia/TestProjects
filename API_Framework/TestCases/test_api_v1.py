#Author: Cheese
#Time: 2018/5/28
import unittest
from Common.DoExcel import DoExcel
from Common.MyRequest import send_request
import ddt


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
        #调用发送接口请求数据的方法，将所有测试用例的测试数据发送出去
        res_obj = send_request(casedata["method"],casedata["url"],casedata["request_data"])
        #断言--比对相应结果是否相等
        self.assertEqual(casedata["expected_data"],res_obj.text)   #text获取响应体


