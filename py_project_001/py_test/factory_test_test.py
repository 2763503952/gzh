

class Only_Object:
    pass




one = Only_Object()


class One():
    def num(self):
        print(1)

class Two():
    def num(self):
        print(2)

class Three():
    def num(self):
        print(3)


class Factory:
    def get_class(self,flag):
        if flag == 1:
            return One()
        elif flag == 2:
            return Two()
        elif flag == 3:
            return Three()
    def name_to_class(self,obj_type):
        """eval方法作用：把字符串转化为相应的类"""
        return eval(obj_type)()