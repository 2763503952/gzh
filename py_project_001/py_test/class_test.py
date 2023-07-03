class Test:
    x=5

class Test001:
    x = 5
    def __init__(self,x):
        self.x = 20
        self.y = 10

    def xxx(self,x):
        self.x = x+self.x
        return self.x
    def printx(self):
        print("x,y:",self.x,self.y)
class Test002(Test001,Test):
    x = 10
    def __init__(self,x):
        self.x = x
class Test003(Test001,Test):
    x = 10
    def __init__(self,x):
        super().__init__(x)
        print("Test003的x",self.x)
class Test004:
    def __init__(self,x):
        self.x = x
    def print_self(self):
        print("self:",self.x,self)
        return self















if __name__ == '__main__':
    test = Test() #实例化
    test1 = Test()
    print("test:",test,"test1:",test1)#test: <__main__.Test object at 0x0000018454C90548> test1: <__main__.Test object at 0x0000018454C9F988>
    print("test:",id(test),"test1:",id(test1))#test: 1667869771080 test1: 1667869833608
    print(type(test))#<class '__main__.Test'>
    print(test.x) #输出5

    """如果不带括号本质上是给类对象起了一个别名，
    类似C语言中的typedef关键字，而并不会创建一个实例。"""
    a = Test
    print(a,":",Test) #输出相等

    test2 = Test001(3)
    print(test2.x) #输出3
    print(test2.xxx(3))#输出6
    print(test2.x)#输出6

    test3 = Test002(10)
    print(test3)#<__main__.Test002 object at 0x000001F765284E08>
    print(test3.x)#输出10
    # test3.printx()#抛出错误 Test002里没有y属性

    test4 = Test003(10)
    test4.printx() #输出x,y: 20 10

    test5 = Test004(10)
    test5.print_self()#self: 10 <__main__.Test004 object at 0x00000207197CC5C8>
    print(test5.print_self().x)#10
    print(test5)#<__main__.Test004 object at 0x00000207197CC5C8>
    """
    return self:返回实例化的对象
    """











