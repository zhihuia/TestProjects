import os

cur_dir = os.path.split(os.path.abspath(__file__))[0]  # 文件的目录和文件的名字分离出来
#  os.path.abspath(__file__) 获取当前文件的所有路径，返回元组

testcase_dir = cur_dir.replace("Common", "TestCases")

testdata_dir = cur_dir.replace("Common", "TestDatas")

htmlreport_dir = cur_dir.replace("Common", "HtmlTestReport")

logs_dir = cur_dir.replace("Common", "Logs")

config_dir = cur_dir.replace("Common", "Config")

