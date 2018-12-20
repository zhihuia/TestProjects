import requests
import json


def send_request(method, url, request_data=None, headers=None):
    # 将json字符串转换成字典数据。因为requests请求的参数要求是字典类型的数据
    if request_data is not None:
        request_data = json.loads(request_data)
    if str(method).lower() == "get":
        res_obj = requests.request(method, url, params=request_data, headers=headers)
    elif str(method).lower() == "post":
        res_obj = requests.request(method, url, data=request_data, headers=headers)
    else:
        res_obj = None
    return res_obj
