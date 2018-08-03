#Author: Cheese
#Time: 2018/5/28 21:14
from openpyxl import load_workbook

class DoExcel:
    '''
    专门用来与excel的数据文件进行交互
    '''

    def __init__(self,filepath):
        self.wb = load_workbook(filepath)
        self.sh = self.wb["case_datas"]
        #self.init_data_sh = self.wb["init_data"]


    #读取所有测试数据
    def get_all_caseDatas(self):
        # 定义一个列表，专门用来存储所有的测试用例。每一个测试用例都是一个字典，有所有的相关数据
        all_caseDatas = []
        for row in range(2,self.sh.max_row+1):
            new_case = {}
            new_case["method"] = self.sh.cell(row,column=5).value
            new_case["url"] = self.sh.cell(row, column=6).value
            new_case["request_data"] = self.sh.cell(row, column=7).value
            new_case["expected_data"] = self.sh.cell(row, column=8).value
            all_caseDatas.append(new_case)
        #print(all_caseDatas)
        return all_caseDatas















'''
    #读取所有测试数据
    def get_all_caseDatas(self):
        #先获取所有的初始化数据
        init_datas = self.get_init_data()
        #定义一个列表，专门用来存储所有的测试用例。每一个测试用例都是一个字典，有所有的相关数据
        all_caseDatas = []
        for row in range(2,self.sh.max_row+1):
            #print(self.sh["E2":"H2"].value
            new_casedata ={}
            new_casedata["method"] = self.sh.cell(row,column=5).value
            new_casedata["url"] = self.sh.cell(row, column=6).value
            new_casedata["expected_data"] = self.sh.cell(row, column=8).value

            #new_casedata["request_data"] = self.sh.cell(row, column=7).value
            #先拿到excel中请求的数据
            temp_request_data = self.sh.cell(row, column=7).value
            #判断一下本条测试数据当中，请求数据是否有需要替换的
            # 遍历所有的初始化值的键名，如果请求数据当中，有某一个键名，则直接替换
            if temp_request_data is not None:
                for item,value in init_datas.items():
                    if temp_request_data.find(item) != -1:
                        request_data = temp_request_data.replace(item,value)
            #替换请求数据
            new_casedata["request_data"] = temp_request_data

            all_caseDatas.append(new_casedata)
            #print(all_caseDatas)
            #print(len(all_caseDatas))
        return all_caseDatas


    def get_init_data(self):
        init_datas = {}
        #读取所有的初始化数据  --第一列为键名，第二列为键值
        for row in range(2,self.init_data_sh.max_row+1):
            key = self.init_data_sh.cell(row,column=1).value
            value = self.init_data_sh.cell(row,column=2).value
            init_datas[key] = value
        #全局手机号码初始化值
        #self.init_phone = init_datas["${phone1}"]
        #对初始化收集号码--进行递增处理，需要4个
        phone2 = int(init_datas["${phone1}"]) + 2
        init_datas["${phone2}"] = str(phone2)
        init_datas["${phone3}}"] = str(phone2 + 2)
        init_datas["${phone4}}"] = str(phone2 + 4)
        init_datas["${phone5}}"] = str(phone2 + 6)
        print("init_datas",init_datas)
        return init_datas

    def update_init_phone(self):
        init_phone = self.init_data_sh.cell(2,1).value
        self.init_data_sh.cell(2,1).value = str(int(init_phone)+9)

    def save_data(self,filepath):
        self.wb.save(filepath)

'''




#de = DoExcel("D:\\PythonStudy\\python6_basic\\API\\TestDatas\\api_info_1.xlsx")
#de = DoExcel("/Users/gemii/TestProjects/API_Framwork/TestDatas/api_info_1.xlsx")
#de.get_all_caseDatas()