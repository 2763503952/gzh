#面向对象的网络层Demo
#每一个层包装成以一个对象
import numpy as np


class Layer:
    def __init__(self,num1,num2):
        """
        一层神经网咯的构造函数
        :param num1: 输入这层的参数数量
        :param num2: 这层的神经元数量
        """
        self.wights = np.random.randn(num1,num2) #权重矩阵
        self.offset = np.random.randn(num2) #偏移值
        self.output = None

    def layer_forward(self,inputs):
        sum1 = np.dot(inputs,self.wights)+self.offset
        self.output = self.active_func(sum1)

        return self.output

    def active_func(self,arg1):
        """
        激活函数
        :param arg1:输入值
        :return:
        """
        return np.maximum(0, arg1)

