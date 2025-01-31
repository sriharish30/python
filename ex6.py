class car():
    def model(self):
        self.model=""
    def year(self):
        self.year=""
    def display(self):
        print("model of the car:",self.model)
        print("year of the car:",self.year)
c=car()
c.model="swift"
c.year="2005"
c.display()