from abc import ABC, abstractmethod
class car(ABC):
    def __init__(self,name,model,year):
        self._name=name
        self._model=model
        self._year=year
    abstractmethod
    def name(self):
        pass
    def model(self):
        pass
    def year(self):
        pass
class bmw(car):
    def name(self):
        print("name:",self._name)
    def model(self):
        print("model",self._model)
    def year(self):
        print("year:",self._year)
class benzzzzz(car):
    def name(self):
        print("name:",self._name)
    def model(self):
        print("model",self._model)
    def year(self):
        print("year:",self._year)
b=bmw("bmw","200","2026")
b1=benzzzzz("benz","390","2024")
b.name()
b.model()
b.year()
b1.name()
b1.model()
b1.year()