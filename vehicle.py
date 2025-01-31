class vehicle():
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        print("car started")
v1=vehicle()
v1.start()
c1=car()
c1.start()