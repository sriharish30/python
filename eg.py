class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("name:",self.name)
        print("regno:",self.regno)
t1=teacher("sri","143")
t2=teacher("sha","7")
t1.display()
t2.display()
        