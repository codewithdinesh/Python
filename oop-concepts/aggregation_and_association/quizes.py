# Q1 of 3
# What is the output of the following code snippet?

class Mobile:
    def __init__(self,brand,case):
        self.brand=brand
        self.case=case
    def display(self):
        print(self.case.color)

class Case:
    def __init__(self,color):
        self.color=color
c1=Case("Black")
c2=Case("White")
m1=Mobile("Hony",c1)
c1.color="Green"
m1.display()

# Q2 of 3
# What is the output of the following code snippet?

class Customer:
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
class Mobile:
    def __init__(self,brand):
        self.brand=brand
    def unlock(self,cover):
        print(cover.color)
class Cover:
    def __init__(self):
        self.__color="red"
Customer("Cus1",Mobile("Apple")).mobile.unlock(Cover())

# Q3 of 3
# What is the output of the following code snippet?

class Customer:
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
class Mobile:
    def __init__(self,brand):
        self.brand=brand
    def unlock(self,cover):
        cover.color="yellow"
class Cover:
    def __init__(self):
        self.color="red"
Customer("Cus1",Mobile("Apple")).mobile.unlock(Cover())
print(Cover().color)
 