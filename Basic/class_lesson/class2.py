class Father:
    def __init__(self,id,name,sex,age):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self, food):
        print("eat:", food)

    def earnMoney(self, money):
        print("Father earn money:", money)


class Mother:

    def sing(self):
        print("XXXXXXX")

    def earnMoney(self, money):
        print("Mother earn money:", money)


class Son(Father, Mother):

    def eat(self, food):
        print("eat",food)
        print("faster!")

    def dance(self):
        print("XXXXXXXX")

#子类没有定义初始化方法，但是父类定义了初始化方法
#则子类实例化时会调用父类的初始化方法


Cheese = Son(123, "Cheese", "female", 25)
Cheese.eat("apple")  #只调用子类的eat方法
Cheese.earnMoney(2000)


CheeseBB = Father(111, "BB", "male", 56)
CheeseBB.eat("orange")