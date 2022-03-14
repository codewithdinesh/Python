# Static methods are those methods which can be accessed without an object. They are accessed using the class name.

# 2 ways :

# The methods should not have self

# @staticmethod must be written on top of it
class Mobile:

    @staticmethod
    def get_discount():
        return Mobile.__discount

    @staticmethod
    def set_discount(discount):
        Mobile.__discount = discount


# access static method
Mobile.set_discount(100)
print(Mobile.get_discount())
