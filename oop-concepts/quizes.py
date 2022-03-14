# 1
class Employee:
    def __init__(self):
        self.employee_id = None
    def check_eligibility(self):
        if(self.employee_id>=9000 and self.employee_id<=10000):
            print("The employee is eligible for special benefits")
        else:
            print("The employee is not eligible for special benefits")
emp1=Employee()
emp1.employee_id=10000
emp1.check_eligibility()
emp2=Employee()
emp2.employee_id=4500
emp2.check_eligibility()


# 2
class Example:
    def __init__(self,num):
        self.num=num

    def set_num(self,num):
        self.num=num

    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())

# 3
class Example:
    def __init__(self,num):
        self.num=num

    def set_num(self,num):
        num=num

    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())

# 4
class Customer:
    def __init__(self):
        self.cust_id = 100

c1=Customer()
print(c1.cust_id)