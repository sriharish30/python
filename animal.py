class animal():
    def __init__(self,animal,specis):
        self.name=animal
        self.specis=specis
    def display(self):
        print("Animal:",self.name)
        print("Specis:",self.specis)
pet=animal("dog","herbi")
pet.display()

