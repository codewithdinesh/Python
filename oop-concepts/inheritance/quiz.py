class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num


class Child(Parent):
    def __init__(self, num, val):
        super().__init__(num)
        self.__val = val

    def get_val(self):
        return self.__val


son = Child(100, 200)
print(son.get_num())
print(son.get_val())

# What is the output of the following code snippet?


class Parent:
    def __init__(self):
        self.num = 100


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var = 200

    def show(self):
        print(self.num)
        print(self.var)


son = Child()
son.show()

# Consider the following python function for representing the customers of a retail store.
# Objective of the code is to record the details of the customers.


def customer_record(customer_type, name, discount, points_earned, membership_card_type):
    if(customer_type == "Regular"):
        record = "Record Regular Customer:"+name+" "+(str)(discount)
    elif(customer_type == "Privileged"):
        record = "Record Privileged Customer:"+name+" "+(str)(points_earned)
    elif(customer_type == "Elite"):
        record = "Record Elite Customer:"+name+" "+membership_card_type
    print(record)
# What will be the optimal class structure if this has to be re-written in Object oriented programming?
