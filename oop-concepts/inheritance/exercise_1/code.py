
class Apparel:
    counter = 100

    def __init__(self, price, item_type):
        Apparel.counter += 1
        self.price = price
        self.item_type = item_type
        self.item_id = None

        # if(self.item_type.lower() == "cotton"):
        #     self.item_id = "C"+str(Apparel.counter)
        # elif(self.item_type.lower() == "silk"):
        #     self.item_id = "S"+str(Apparel.counter)

    def calculate_price(self):
        self.price = (self.price*5)/100

    def get_item_id(self):
        return self.item_id

    def get_price(self):
        return self.price

    def get_item_type(self):
        return self.item_type

    def set_price(self, price):
        self.price = price


class Cotton(Apparel):
    def __init__(self, price, discount):
        self.price = price
        self.discount = discount
        self.item_type = "Cotton"
        self.discount_price = None
        super().calculate_price()

    def calculate_price(self):
        self.discount_price = (self.price*self.discount)/100
        self.temp_price = (self.price - self.discount_price) * 5 / 100
        self.price = self.temp_price

    def get_discount(self):
        return self.discount_price


class Silk(Apparel):
    def __init__(self, price):
        self.price = price
        self.item_type = "Silk"
        super().calculate_price()
        self.point = None

    def calculate_price(self):
        if(self.price > 10000):
            self.point = 10
        else:
            self.point = 3

    def get_point(self):
        return self.point


OBJ1 = Apparel(20000, "Silk")
print(OBJ1.get_item_id)
print(OBJ1.get_price)

print('')
OBJ2 = Silk(30000)
print(OBJ2.get_point())
