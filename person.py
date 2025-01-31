class person():
    def __init__(self,name):
        self.name=name 
class student(person): 
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def display(self):
        print("name:",self.name)
        print("grade:",self.grade)
s1=student("sri","2")
s1.display()       