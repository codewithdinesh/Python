# when one object owns another object , but they have independent life cycle
# If class A owns class B, then class A is said to aggregate class B.
# and class A has all access of class B , But it can not access private member directly

# to create aggreation class , pass class object into the methods or constructor as a parameter of another class

class Customer:
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address

    def view_details(self):
        print(self.name, self.age, self.phone_no)
        print(self.address.door_no, self.address.street, self.address.pincode)

    def update_details(self, add):
        self.address = add


class Address:
    def __init__(self, door_no, street, pincode):
        self.door_no = door_no
        self.street = street
        self.pincode = pincode

    def update_address(self):
        pass


add1 = Address(123, "5th Lane", 56001)
add2 = Address(567, "6th Lane", 82006)
cus1 = Customer("Jack", 24, 1234, add1)
cus1.view_details()
cus1.update_details(add2)
cus1.view_details()


# Sometimes a class may depend on another class for some of its use.
# This is not a strict relationship and hence won’t appear in the class diagram.
# For example, in the below code, the Customer class depends on a payment object for purchasing.
# Here payment is a local variable and not an attribute.
# If an object is used only in a method of a class as a local variable then it is called as Association
class Customer:
    def __init__(self, name, age, phone_no):
        self.name = name
        self.age = age
        self.phone_no = phone_no

    def purchase(self, payment):
        if payment.type == "card":
            print("Paying by card")
        elif payment.type == "e-wallet":
            print("Paying by wallet")
        else:
            print("Paying by cash")


class Payment:
    def __init__(self, type):
        self.type = type


payment1 = Payment("card")
c = Customer("Jack", 23, 1234)
c.purchase(payment1)


# inside the methods
# Object creation
class Customer:
    def __init__(self, name, cust_type, bill):
        self.name = name
        self.bill = bill
        self.cust_type = cust_type

    def calulate_bill(self):
        tax1 = Tax(self.cust_type)
        final_bill = self.bill*tax1.tax_details(self.cust_type)
        return final_bill


class Tax:
    def __init__(self, cust_type):
        self.cust_type = cust_type

    def tax_details(self, cust_type):
        if(cust_type == "Student"):
            return 5
        else:
            return 10


cust1 = Customer("Maddy", "Student", 100)
print(cust1.calulate_bill())
