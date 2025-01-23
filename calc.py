class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add",self.num1+self.num2)
    def sub(self):
        print("sub",self.num1-self.num2)
x1=calculator(12,3)
x1.add()
x2=calculator(12,3)
x2.sub()