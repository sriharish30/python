class dad():
    def money(self):
        print ("dads money")
class land():
    def important(self):
        print("land is important")
class son1(dad):
    pass
class son2(dad,land):
    pass
class son3(dad):
    pass
s2=son2()
s2.money()
l1=land()
l1.important()

