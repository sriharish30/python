from abc import ABC, abstractmethod
class lambo():
    def __init__(self,name,color,speed):
        self._name=name
        self._speed=speed
        self._color=color
    @abstractmethod
    def name(self):
        pass
    def sub(self):
        pass
    def request(self):
        pass
class polo(lambo):
    def name(self) :
        print("name:",self._name)
    def color(self):
        print("color:",self._color)  
    def speed(self):
        print("speed:",self._speed)     
class audi(lambo):
    def name(self):
        print("name:",self._name)
    def color(self):
        print("color:",self._color)
    def speed(self):
        print("speed:",self._speed)
p=polo("walswogan","whhite","120")
a=audi("audiiiii","red","230")
p.name()
p.color()
p.speed()
a.name()
a.color()
a.speed() 
