#神经网络Demo

import numpy as np


inputs = np.random.randint(0,10,(4,3)) #随机生成4x3且在（0，10）范围内的矩阵
# print(inputs)
# wights = np.random.randint(0,5,(3,2))
# print(wights)


# b1 = np.array([0.22,0.32])

#激活函数
def active_func(arg1):
    return np.maximum(0,arg1)

#随机生成权重函数
def make_wights(num1,num2):
    """
    :param num1:参数数量
    :param num2: 神经元数量
    :return: 矩阵
    """
    result = np.random.randn(num1,num2)
    return result
#随机生成偏移值
def make_offset(num1):
    """
    :param num1:神经元个数
    :return: 一维矩阵
    """
    return np.random.randn(1,num1)

wights = make_wights(3,2)
b1 = make_offset(2)
sum1 = np.dot(inputs,wights) + b1
print(active_func(sum1))
# print(make_wights(3,2))





