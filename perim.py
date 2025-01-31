from abc import ABC,abstractmethod
class polygon():
    def area(self):
        pass
    def perimeter(self):
        pass
class rectangle(polygon):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area (self):
        print("area of rectangle=",self.length*self.width)
    def perimeter(self):
        print("perimetr of rectangle=",self.length * self.width * 2)
class triangle(polygon):
    def __init__(self,base,height,a):
        self.base=base
        self.height=height
        self.a=a
    def area(self):
        print("area of triangle=",0.5 * self.height * self.base)
    def perimeter(self):
        print("perimetr of triangle=",self.height + self.base  + self.a)
r=rectangle(5,7)
t=triangle(7,4,6)
t.area()
r.area()
t.perimeter()
r.perimeter()

