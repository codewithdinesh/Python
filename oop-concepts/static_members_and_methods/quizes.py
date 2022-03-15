# Q1 of 3
# What is the output of the following code snippet?

class Table:
    def __init__(self):
        self.no_of_legs = 4
        self.__glass_top = None
        self.__wooden_top = None

    def assign_data(self, glass_top, wooden_top):
        self.__glass_top = glass_top
        self.__wooden_top = wooden_top

    def identify_rate(self, glass_top, wooden_top):
        self.assign_data(glass_top, wooden_top)
        if(self.__glass_top == True):
            rate = 20000
        elif(self.__wooden_top == True):
            rate = 30000
        else:
            rate = 0
        return rate


dining_table = Table()
rate = dining_table.identify_rate(True, False)
print(rate)

# Q2 of 3
# What will be the output of the following snippet?


class Example:
    num = 10

    @staticmethod
    def add(num1, num2):
        result = (num1+num2)*Example.num
        return result


print(Example.add(100, 200))

# Q3 of 3
# Choose the statements which are INCORRECT with regard to the below code.


class Lion:
    __water_source = "well in the circus"

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def drink_water(self):
        print(self.__name, "drinks water from the", Lion.__water_source)


simba = Lion("Simba", "Male")
nala = Lion("Nala", "Female")
simba.drink_water()
nala.drink_water()


# There will be only one __water_source variable created for both simba and nala objects
# There will be two separate __water_source variables created for both simba and nala objects
# drink_water() cannot access __water_source variable
# __water_source should be always accessed using self in a method of the same class
# __water_source can be accessed using Lion in a method of the same class
