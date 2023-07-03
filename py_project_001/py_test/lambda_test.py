"""lambda表达式"""
test001 = lambda x:x+10
test002 = lambda a,b:a+b
def test003(n:int):
    return lambda a:a+n






if __name__ == '__main__':
    print(test001(100)) #输出110
    print(test002(100,10)) #输出110
    print(type(test003(100)))  #输出<class 'function'>
    print(test003(100)) #<function test003.<locals>.<lambda> at 0x0000014CF57C6678>
    print(test003(100)(10)) #输出110


