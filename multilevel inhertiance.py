class sri():
    def laptop(self):
        print("sris laptop")
class hari(sri):
    def charger(self):
        print("haris charger")
class sha(hari):
    def bag(self):
        print("shas bag")
s=sha()
s.bag()
s.charger()
s.laptop()
h=hari()
h.laptop()