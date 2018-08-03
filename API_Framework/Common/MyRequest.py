#Author: Cheese
#Time: 2018/5/28 21:50

#只指定一个方法  用来发送http请求

import requests
import json



def send_request(method,url,request_data=None):
    #将json字符串转换成字典数据。因为requests请求的参数要求是字典类型的数据
    if request_data != None:
        request_data = json.loads(request_data)

    if method.lower() == "get":
        res_obj = requests.request(method,url,params=request_data)
    elif method.lower() == "post":
        res_obj = requests.request(method,url,data=request_data)
    else:
        res_obj = None
    return res_obj




