"""python的静态方法和类方法"""

class Static:
    """
    静态方法：不调用其他实例方法和实例属性;
    用@staticmethod装饰器，装饰的为静态方法;
    静态方法在类里，不需要传self参数;
    """
    var = "调用类里的常量"
    @staticmethod
    def static(var):
        print(var)
        print("静态方法")

    @staticmethod
    def static_method():
        print("调用类里的静态方法")

    @classmethod
    def clsmethod(cls):
        """cls代表类本身，self代表实例化的对象"""
        cls.static_method()
        print(cls.var)
        """
        cls()相当于实例化
        """
        print(cls)
        print(cls())
        cls().damicmethod(3)
    def damicmethod(self,a):
        print("调用动态方法和"+"参数：",a)



if __name__ == '__main__':
    obj = Static
    obj1 = Static()
    print(obj)
    print(obj1)
    obj.static("静态方法可以传递参数")
    """
    输出：
    <class '__main__.Static'>
    <__main__.Static object at 0x000001F002698CD0>
    静态方法可以传递参数
    静态方法
    说明obj是一个类，obj1是一个实例对象，静态方法不用实例化对象就可以调用  
    """

    obj.clsmethod()
    """
    输出：
    调用类里的静态方法
    调用类里的常量
    
    <class '__main__.Static'>
    <__main__.Static object at 0x0000027940CC8D60>
    调用动态方法和参数： 3
    说明cls()实例化的对象，cls是类
    """


















