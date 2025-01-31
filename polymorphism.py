class animal():
    def sound(self):
        print("animal makes a sound")
class dog(animal):
    def sound(self):
        print ("Dog barks")
class bird(animal):
    def sound(self):
        print("bird sings")
b1=bird()
b1.sound()