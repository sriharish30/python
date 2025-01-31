from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        print("area of rectangle=", self.height * self.width)

    def perimeter(self):
        print("perimeter of rectangle:", 2 * (self.height + self.width))
class circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("area of the circle:",3.14*self.radius **2)
    def perimeter(self):
        print("perimeter of the circle:",2*3.14 **2)
r=Rectangle(10,1)
c=circle(8)
c.area()
c.perimeter()
r.area()
r.perimeter()
