class Example:
    def student(self,name, roll=None):
        if(roll is not None):
            print("Name: ", name)
            print("Roll no: ", roll)
        else:
            print("Name : ", name)


e1 = Example()
e1.student("Dinesh", 23)

print("")
e1.student(23)

e2 = Example()
e2.student(23, "Dinesh")
