# We can create shared attributes by placing them directly inside the class and not inside the constructor. And since this attribute is not owned by any one object, we don’t need the self to create this attribute. Such variables which are created at a class level are called static variables. Here discount is a static variable.

class Mobile:
    discount = 50

    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    # static variables are accessed by class name not by Object name
    def print(self):
        return Mobile.discount


mobile_obj = Mobile(1000, "apple")
print(mobile_obj.print())

# we can update static variables ,alse we can create getter setter of static varibles, we can also declare static variable as private variable .
