#多层神经网络Demo

import numpy as np




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


#第一层
inputs_1 = np.random.randint(0,10,(3,2))
print("输入：",inputs_1)

wights_1 = make_wights(2,3)
b_1 = make_offset(3)
#第二层
wights_2 = make_wights(3,3)
b_2 = make_offset(3)
#第三层
wights_3 = make_wights(3,2)
b_3 = make_offset(2)

#第一层运算
sum1 = np.dot(inputs_1,wights_1)+b_1
print("-----第一层-----")
print("权重：",wights_1)
print("偏移：",b_1)
print("求和：",sum1)
#第二层运算
sum2 = np.dot(sum1,wights_2)+b_2
print("-----第二层-----")
print("权重：",wights_2)
print("偏移：",b_2)
print("求和：",sum2)
#第三层
sum3 = np.dot(sum2,wights_3)+b_3
print("-----第三层-----")
print("权重：",wights_3)
print("偏移：",b_3)
print("求和：",sum3)

