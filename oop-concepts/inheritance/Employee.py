from re import S


class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary

    def getInfo(self):
        print("Name: ",self.name)
        print("Department : ",self.department)
        print("Salary: ",self.salary)

emp=Employee("Dinesh","Marketing",85000)
emp.getInfo()
        