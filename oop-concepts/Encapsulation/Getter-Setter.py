# Getters and setters are used to protect your data, particularly when creating classes.

# Getter and Setter methods should be used to access a private attribute

# Getter is used to return the data

# Setter is used to take inputs or passing inputs

# All setter methods must accept the value to be updated as a parameter and all getter methods must not have any parameter and they must return the value.


class Customer:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def set_wallet_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance = amount

    def get_wallet_balance(self):
        return self.__wallet_balance


c1 = Customer(100, "Gopal", 23)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())
