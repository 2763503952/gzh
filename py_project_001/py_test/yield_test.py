"""生成器"""
"""有yield关键字的函数，为生成器函数，yield 变量 将变量加入迭代器"""

def yield_test(num:int):
    a,i = 0,0
    while(i<num):
        yield a
        a = a+1
        i = i+1

f = yield_test(10)
print(f) #返回了一个生成器对象<generator object yield_test at 0x000001CE1E17CA50>
for i in f:
    print(i) #打印a

