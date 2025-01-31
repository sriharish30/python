class dad():
    def money(self):
        print("dads moeny")
class mom():
    def mbl(self):
        print("moms mbl")
class son(mom,dad):
    def bike(self):
        print("sons bike")
hari=son()
hari.bike()
hari.mbl()
hari.money()