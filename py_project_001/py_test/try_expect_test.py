"""Python异常处理"""
"""
try:
    需要执行的代码
except:
    发生异常时执行的代码
else:
    没有异常时的执行代码
finally:
    不管有没有异常都会执行代码
"""
"""
抛出异常：rasie
"""
"""
try语句发生错误时，匹配expect后的错误类型
"""
while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except IOError:
        print("您输入的不是数字，请再次尝试输入！")
    except Exception as e:
        print("{0}输入不合法") #发生错误走这个expect
        print(e)
        print(type(e))
        print(Exception)

"""with关键字"""
"""
with 关键字自动执行类的__enter__ 和 __exit__
"""


class With_Test:
    def __init__(self,test):
        print("执行构造函数")
        self.test = test
    def __enter__(self):
        print("执行enter")
        return self.test
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("执行exit")



if __name__ == '__main__':
    with With_Test(100) as tw:
        print(tw)
    """
    运行结果:
        执行构造函数
        执行enter
        100
        执行exit
    """
    import json
