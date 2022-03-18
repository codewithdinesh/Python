# To create an inheritance relationship between the classes, mention the name of the parent class in brackets:
# the attributes and behaviors get inherited
# private member not inherited

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class FeaturePhone(Phone):
    pass


class SmartPhone(Phone):
    def check(self):
        # trying to access private member of parent class, it gives error
        # print(self.__price)

        # access other element
        print(self.brand)


s = SmartPhone(20000, "Apple", 13)
s.check()


# accessessing private members
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class FeaturePhone(Phone):
    pass


class SmartPhone(Phone):
    def check(self):
        print(self.get_price())


s = SmartPhone(20000, "Apple", 13)
s.check()


# When the child has a method with the same name as that of the parent, it is said to override the parent’s method. This is called as Method Overriding. Method overriding is also called as Polymorphism
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class FeaturePhone(Phone):
    pass


class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")

        # even oveeriding parent method we can still use it in child by: super().method_name()
        super().buy()


s = SmartPhone(20000, "Apple", 13)
s.buy()

# we can also overide childs constructors

# 4 type of inheritance
# 1) Single level : parent - child
# 2) Multi level - parent - child - grandchild
# 3) Hierarchical - one parent multi child
# 4) multiple - multiple parent single child

# Multi level :


class Product:
    def review(self):
        print("Product customer review")


class Phone(Product):
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class SmartPhone(Phone):
    pass


s = SmartPhone(20000, "Apple", 12)
s.buy()
s.review()


# multiple inberitance
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class Product:
    def review(self):
        print("Customer review")


class SmartPhone(Phone, Product):
    pass


s = SmartPhone(20000, "Apple", 12)
s.buy()
s.review()

