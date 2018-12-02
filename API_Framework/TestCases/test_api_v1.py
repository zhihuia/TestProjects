#Author: Cheese
#Time: 2018/5/28

import unittest
from API_Framework.Common.DoExcel import DoExcel
from API_Framework.Common.MyRequest import send_request
import ddt
from API_Framework.Common import myLogger2
from API_Framework.Common import myLogger
import logging
import re

# 获取所有的测试数据
de = DoExcel("/Users/gemii/TestProjects/API_Framework/TestDatas/api_info_1.xlsx")
# de = DoExcel("D:\\PythonStudy\\python6_basic\\API\\TestDatas\\api_info_1.xlsx")
all_case_datas = de.get_all_caseDatas()

# 全局变量 - 接口关联时提取的数据
global_var = {}


@ddt.ddt
class Test_API_V1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("========start test========")

    @classmethod
    def tearDown(cls):
        # 在所有测试用例执行完成之后，更新初始化手机号码到excel中，下一次再读取测试数据时为新的手机号码
        de.update_init_phone()
        de.save_data("/Users/gemii/TestProjects/API_Framework/TestDatas/api_info_1.xlsx")

    @ddt.data(*all_case_datas)
    def test_register(self, casedata):
        global global_var
        logging.info("========开始一个接口测试========")
        logging.info("请求url为：\n{0}".format(casedata["url"]))
        logging.info("请求方法为：{0}".format(casedata["method"]))
        logging.info("请求数据为：\n{0}".format(casedata["request_data"]))
        # 动态的替换请求数据或者url的值（如果url涉及到了）
        if len(global_var) > 0 and casedata["request_data"] is not None:
            for key, value in global_var.items():
                if casedata["request_data"].find(key) != -1:
                    casedata["request_data"] = casedata["request_data"].replace(key, value)
                    logging.info("请求数据需要更新，更新后的结果为：{0}".format(casedata["request_data"]))

        # 调用发送接口请求数据的方法，将所有测试用例的测试数据发送出去
        res_obj = send_request(casedata["method"], casedata["url"], casedata["request_data"])
        logging.info("响应的结果为：\n{0}".format(res_obj.text))
        # 判断一下，测试数据中是否有expression键名，有则标识需要从响应结果中提取对应的数据
        if "expression" in casedata.keys():
            # 根据=号分隔expression字段的数据。第一个值为键名，第二个值为提取的正则表达式
            temp = casedata["expression"].split("=", 1)
            # temp[0]就是键名，temp[1]是提取正则表达式
            reg_result = re.findall(temp[1], res_obj.text)  # findall方法返回的是列表
            global_var[temp[0]] = reg_result[0]

        # 断言--比对相应结果是否相等
        try:
            # 判断比对方式--来选择比对方法
            if casedata["compare_type"] == 1:
                self.assertIsNotNone(re.search(casedata["expected_data"], res_obj.text))  # 正则匹配
            else:
                self.assertEqual(casedata["expected_data"], res_obj.text)  # text获取响应体
            logging.info("期望结果与实际结果匹配，用例成功！")
        except Exception as e:
            logging.error("期望结果与实际结果不匹配，用例失败！")
            logging.exception("断言异常：")
            raise e



