from abc import ABC,abstractmethod
class sri():
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def age(self):
        pass
    @abstractmethod
    def dep(self):
        pass
class hari(sri):
    def __init__(self,name,age,dep):
        self._name=name
        self._age=age
        self._dep=dep
    def name(self):
        print("name:",self._name)
    def age(self):
        print("age:",self._age)
    def dep(self):
        print("department:",self._dep)
class shaaaaa(sri):
    def __init__(self,place,clg,spec):
        self._place=place
        self._clg=clg
        self._spec=spec
    def place(self):
        print("place:",self._place)
    def clg(self):
        print("college:",self._clg)
    def spec(self):
        print("specs:",self._spec)
h=hari("sriharish","23","mca")
s=shaaaaa("nagercoil","noorul islam","with specs")
h.name()
h.age()
h.dep()
s.place()
s.clg()
s.spec()
