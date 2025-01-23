class teacher:
    def __init__(self,name,department,regno):
        self.name=name
        self.department=department
        self.regno=regno
    def display(self):
        print("name:",self.name)
        print("department:",self.department)
        print("regno:",self.regno)
s1=teacher("sri","mca","56")
s2=teacher("sha","mca","55")
s1.display()
s2.display()



