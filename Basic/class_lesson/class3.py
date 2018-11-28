#Author: Cheese
#Time: 2018/11/28 22:48

class MyClass:

    def __init__(self):
        self._private_data1 = "私有方式一"
        self.__private_data2 = "私有方式二"
        pass

    def _pri_func(self):
        print("私有行为一")

    def __pri_func2(self):
        print("私有行为2")

# ①任何以单下划线_开头的名字都应该是内部实现
# 即不希望通过实例名称.变量名/方法名来调用
# 但python并不会真的阻止别人访问内部名称，只是一种约定
mc = MyClass()
mc._pri_func()

# ②以双下划线__开头的名字，仅类自己可以访问
# 继承----这种属性通过继承是无法被覆盖的

