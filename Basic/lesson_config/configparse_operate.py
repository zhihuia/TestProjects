from configparser import ConfigParser

#初始化类
cp = ConfigParser()
cp.read("db.cfg",encoding="utf-8")
sec_list = cp.sections()  # section() 得到所有的section，并以列表的形式返回
print(cp.options(sec_list[0]))  # 得到该section的所有option(key值)

print(cp.items(sec_list[0]))   # items(section) 得到该section的所有键值对

print(cp.get(sec_list[0],"db"))   # get(section,option) 得到section中option的值，返回为string类型，指定标签下面的key对应的value值
print(cp.get(sec_list[0],"port")) # 返回为int类型

