mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
"""iter获取迭代器"""
# print(next(myit))
# print(next(myit))
# print(next(myit))
"""
输出：
apple
banana
cherry
"""

mystr = "banana"
myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
"""
输出：
b
a
n
a
n
a
"""

mystr = "banana"
# for x in mystr:
#   print(x)
"""for 循环实际上创建了一个迭代器对象，并为每个循环执行 next() 方法。"""
"""
输出：
b
a
n
a
n
a
"""

class MyNumbers:
  def __iter__(self):
    """返回迭代器本身"""
    self.a = 1
    return self

  def __next__(self):
    """迭代器主要方法"""
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration #stopIteration是用于终止迭代器的


class MyDict:
    def __init__(self,dict):
        self.maxlen = len(dict)
        self.dict = dict
        self.dictkey = list(dict.keys())
    def __iter__(self):
        self.length = 0
        return self
    def __next__(self):
        if self.length<=self.maxlen:
            self.length += 1
            return {
                self.dictkey[self.length-1]:self.dict[self.dictkey[self.length-1]],
            }
        else:
            raise StopIteration



if __name__ == '__main__':
    # test1 = MyNumbers()
    # iter_test1 = iter(test1)
    # for i in iter_test1:
    #     print(i)

    dict={'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    # dict = MyDict(dict)
    dictitor=iter(dict)
    print(next(dictitor))
    print(next(dictitor))
    print(next(dictitor))
