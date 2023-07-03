"""Python装饰器"""


def closebag(log):
    """1.闭包"""
    """函数嵌套函数"""
    def openbag(msg):
        print("{0}->{1}".format(log,msg))
        return msg

    return openbag

def close_test(log=10):
    """闭包案例"""
    def open_test(msg):
        nonlocal log
        """nonlocal关键字在闭包内修改外包变量，用nonlocal关键字"""
        log = log + msg
        print(log)
    return open_test


def decorator(fnc):
    """装饰器 另一种闭包"""
    print("111111")
    def inner():
        print("装饰器运行前")
        fnc()
        print("装饰器运行后")
    return inner

@decorator
def inner_function():
    print("装饰器装饰")

"""类装饰器"""
"""
类装饰器这个写法，主要思路就是返回一个增加了新功能的函数对象，只不过这个函数对象是一个类的实例对象。
由于装饰器是可调用对象，所以必须在类里面实现__call__方法，这样由类生成的各种实例加上()就可以运行了。
"""

class DectorClass:
    def __init__(self,fun):
        self.func = fun
        print("初始化")


    def start(self):
        print("start up")


    def end(self):
        print("time out")

    def __call__(self,time):
        self.start()
        self.func(time)
        self.end()
        print("总计{0}秒".format(time))


@DectorClass
def accessmode(time):
    for i in range(1,time+1):
        print("{0}秒。。。".format(i))

if __name__ == '__main__':
    f = closebag("23")
    f1 = f("45")
    print(f1) #输出"23->45 45
    f2 =  f("56")
    print(f2) #输出23->56 56

    f=close_test()
    f1 = f(10) #20
    f2 = f(-5) #15

    inner_function()
    """
    运行结果：
        装饰器运行前
        装饰器装饰
        装饰器运行后
    """

    time = 5
    accessmode(time)




