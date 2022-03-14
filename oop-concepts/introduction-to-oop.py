# Objects are real world entities. Anything you can describe in this world is an object

# Classes on the other hand are not real. They are just a concept.

#  A class is a classification of certain objects and it is just a description of the properties and behavior all objects of that classification should possess.

""" Class is a like a recipe and the object is like the cupcake we bake using it. All cupcakes created from a recipe share similar characteristics like shape, sweetness, etc. But they are all unique as well. One cupcake may have strawberry frosting while another might have vanilla. Similarly, objects of a class share similar characteristics but they differ in their values for those characteristics. """

# What does a recipe contain? It contains list of ingredients which make up the cake and the directions. Similarly, a class contains the properties/attributes of the object and the operations/behavior that can be performed on an object.


# A class is defined using the class keyword in python. For example, the below code creates a class called Mobile without any attributes or behavior.

# class Mobile:
#    pass

#  To create an object, we need a class. The syntax for creating an object is "<classname>()", where <classname> is the name of the class.

# Mobile()

# we need variables to access and reuse the objects that we create. Such variables that are used to access objects are called reference variables

# ref_variable=Mobile()

# attributes of mobile is price and brand with no specific attributes

# class Mobile:
#     pass


# mob1 = Mobile()
# mob2 = Mobile()
# mob1.price = 20000
# mob1.brand = "Apple"
# mob1.ios_version = 14
# print(mob1.ios_version)
# mob2.price = 3000
# mob2.brand = "Apple"
# mob2.ios_versio = 13
# print(mob2.ios_versio)


# When we create an object, the special method __init__() inside the class of that object is invoked automatically. This special method is called as a constructor. Try out the below code and observe the output.
# __init__ to create constructor

class Mobile:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price


mob1 = Mobile("Apple", 20000)
print("Mobile 1 has brand", mob1.brand, "and price", mob1.price)
mob2 = Mobile("Samsung", 3000)
print("Mobile 2 has brand", mob2.brand, "and price", mob2.price)


# deconstructor by __del__(self) method
class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        print("Purchases..Creating function inside class")

    def __del__(self):
        print('Deleting the object')


p1 = Mobile(10000, 'Apple')
p2 = Mobile(7000, 'Samsung')

mob1 = Mobile()
# Inbound method invocation, We need not pass the value for self.
mob1.purchase()
# Outbound method invocation, We have to pass the object as the value of self.
Mobile.purchase(mob1)
del p1
