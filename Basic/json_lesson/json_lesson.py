import json

a = {"name":"cheese","sex":None}

#从一个python对象转换成json字符串
b = json.dumps(a,indent=4,sort_keys=True)   #indent=4 格式缩进，按键名排序a-z
print(b)
print(type(b))

#从一个json字符串转换成python字典/列表
c = json.loads(b)
print(c)
print(c["sex"])