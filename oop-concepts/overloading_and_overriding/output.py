class Animal:
    property1=True
    property2=True
    def breath(self):
        print("I breathe oxygen")

    def feed(self):
        print("I eat food")

class Harbivorous(Animal):
    def feed(self):
        print("I eat only plants")

h=Harbivorous()
h.feed()
h.breath()