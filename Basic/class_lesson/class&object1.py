#Author: Cheese
#Time: 2018/11/28 0:45

#定义类
class Friend:

    def __init__(self,age,sex,height):
        self.age = age    #在函数内部添加属性不需要单独声明，直接self.属性名
        self.sex = sex
        self.height = height
        #做一些什么前期事情+逻辑处理




    #定义功能 - 会做饭
    def canCook(self,can=True):
        if can==True:
            print("我会做饭")
        else:
            print("我不会做饭")

    def canEarnMoney(self):
        print("我会赚钱")

    def setAge(self,age):
        self.age = age
        print("年龄为：",self.age)

    def setHeight(self,height):
        self.height = height
        print("身高为：",self.height)

    def setWeight(self,weight):
        self.weight = weight
        print("体重为：",self.weight)

    def setMoney(self,money):
        self.money = money
        print("资产为：",self.money)



#对象一：身高180、会做饭、会赚钱、有200万资产，29岁
#实例化：类名()
goudan = Friend()
print(goudan.age)
print(goudan.money)
goudan.canCook()
#如何实现狗蛋只会做蛋炒饭

print("========================")
#对象二：身高175，不会做饭，年龄25岁，资产5万块
laowang = Friend()
#改变对象的属性
laowang.setAge(25)
print(laowang.age)
laowang.setHeight(175)
print(laowang.height)
laowang.canCook(False)

#对象三
xiaogou = Friend(26,"男",178)
xixi = Friend(18,"女",160)
