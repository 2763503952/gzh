"""Python推导式"""

import math
numbers = [i+1 for i in range(0,10) if i%2==0]#输出[1, 3, 5, 7, 9]
"""
列表的推导式为[表达式 for 变量 in 迭代器 if 条件]
*表达式：可以是有返回值的函数  
"""
print(numbers)
numbers2 = [math.sqrt(i) for i in range(0,3)]#[0.0, 1.0, 1.4142135623730951]
print(numbers2)


dictnums = {key*2:key*3 for key in numbers}
"""
字典推导式为{key表达式:value表达式 for key变量,value变量 in 迭代器}
"""
print(dictnums)#{2: 3, 6: 9, 10: 15, 14: 21, 18: 27}


a = {i*2 for i in range(3)}
"""
集合推导式为{表达式 for 变量 in 迭代器 if 条件}
"""
print(a)#{0, 2, 4}

b = (i*2 for i in range(3))
"""
元组的推导式为(表达式 for 变量 in 迭代器 if 条件)
元组推导式返回的是迭代对象，需要把他转化成元组
"""
print(b)#<generator object <genexpr> at 0x000001F1E041FC80>
print(tuple(b))#(0, 2, 4)









