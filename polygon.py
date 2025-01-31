from abc import ABC,abstractmethod
class polygon():
    def area(self):
        pass
class rectangle(polygon):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area (self):
        print("area of rectangle=",self.length*self.width)
class triangle(polygon):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        print("area of triangle=",0.5 * self.height * self.base)
r=rectangle(5,7)
t=triangle(7,6)
t.area()
r.area()

