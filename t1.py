class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.registernum=reg
    def display(self):
        print("name:",self.name)
        print("register num:",self.registernum)
t1=teacher("sri","123")
t2=teacher("hari","786")
t1.display()
t2.display()