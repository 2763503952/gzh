"""Python的设计模式"""

from  factory_test_test import one
from  factory_test_test import Factory
from  abc import abstractmethod,ABCMeta
"""
单例模式：
一个类无论实例化多少次，都只有一个对象，保证一个类只有一个实例，节省内存
"""

obj1 = one
obj2 = one
print(obj1) #输出<factory_test_test.Only_Object object at 0x0000024753F6F640>
print(obj2) #输出<factory_test_test.Only_Object object at 0x0000024753F6F640>

"""
工厂类：大量创建对象的统一入口
"""

one = Factory().get_class(1)
two = Factory().get_class(2)


one = Factory().name_to_class('One')
one.num()
object