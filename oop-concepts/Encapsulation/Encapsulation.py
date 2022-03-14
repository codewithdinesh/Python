# Encapsulation is preventing access to a data outside the class

# Adding a __ in front of a attribute makes it private

# Getter and Setter methods should be used to access a private attribute

# This is customer class
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount

    def show_balance(self):
        print("The balance is ", self.wallet_balance)


c1 = Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
c1.show_balance()

# But with the way currently it is coded, the data can be accidentally changed by directly assigning a incorrect value to it as shown below:
# Now we are modifiging balance - so its break security - above class


class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount

    def show_balance(self):
        print("The balance is ", self.wallet_balance)


c1 = Customer(100, "Gopal", 24, 1000)
c1.wallet_balance = 10000000000
c1.show_balance()


# To avoid above problems we use Encapsulation
# We can put a lock on that data by adding a double underscore in front of it, as shown below:
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print("The balance is ", self.__wallet_balance)


c1 = Customer(100, "Gopal", 24, 1000)
# print(c1.__wallet_balance)


# Adding a double underscore makes the attribute a private attribute.
# Private attributes are those which are accessible only inside the class.
# This method of restricting access to our data is called Encapsulation.
# If we try to access it will gives errors


# We can access Private Memeber of class like this :-
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print("The balance is ", self.__wallet_balance)


c1 = Customer(100, "Gopal", 24, 1000)
c1._Customer__wallet_balance = 10000000000
c1.show_balance()

""" What is the use of a lock, if a thief can open it?

Any lock can be broken by a determined thief. Similarly, just because you make your code private, does not mean it is not accessible to other developers. When a developer sees a private variable, it’s a gentleman's agreement not to access it directly. It is used to only prevent accidental access.

Thus in python encapsulation is more like a caution sign than a lock. A caution sign is there so that you don’t accidentally break a rule. But if you still want to break it you can, with consequence ;) """
