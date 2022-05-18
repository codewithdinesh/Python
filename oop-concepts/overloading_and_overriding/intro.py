# Overloading : same method name but different parameters and argunments

class College:

    def student(self, roll, name=None):
        if(name is not None):
            self.roll = roll
            self.name = name
        else:
            self.roll = roll

    def print(self):
        print("Roll:", self.roll)

    def print2(self):
        print("Roll:", self.roll)
        print("Name:", self.name)


c1 = College()
c2 = College()
c1.student(23, "Dinesh")
c1.print2()
print()
c2.student(28)
c2.print()
print()


# Overriding
# overide the the parent class method from class
#

class College:
    def students(self, roll):
        self.roll = roll

    def print(self):
        print("Method from parent class")
        print("Roll: ", self.roll)


class School(College):
    def students(self, roll):
        super().students(roll)

    def print(self):
        print("\nMethod from child class")
        print("Roll: ",self.roll)
        #  super().print()

    def area(self, i, c):
        pass


c1 = College()
c1.students(3223)
c1.print()

s1=School()
s1.students(80)
s1.print()
