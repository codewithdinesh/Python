# Initialize counter variable to 198 in Freight class

# All validate methods should return true, if validation succeeds. Else it should return false

# validate_customer_id(): Customer id should be 6 digits and should begin with digit 1

# validate_weight(): Weight should be a multiple of 5

# validate_distance(): Distance should be between 500kms and 5000kms (both inclusive)

# forward_cargo()

# Validate from_customer.customer_id, recipient_customer.customer_id, distance and weight of the freight

# If valid,

# auto-generate freight_id starting from 200 and initialize it. freight_id should be even

# calculate freight_charge based on weight (Rs.150/kg) and distance (Rs.60/km)

# Else, set freight_charge to 0


class Freight:
    counter = 198

    def __init__(self, recipent_customer, from_customer, weight, distance):
        self.recipient_customer = recipent_customer
        self.from_customer = from_customer
        self.weight = weight
        self.distance = distance
        self.freight_charge = None
        self.freight_id = None

    def validate_weight(self):
        if(self.weight % 5 == 0):
            return True
        else:
            return False

    def validate_distance(self):
        if(self.distance >= 500 and self.distance <= 5000):
            return True
        else:
            return False

    def forward_cargo(self):

        if(self.from_customer.validate_customer_id() == True and self.recipient_customer.validate_customer_id() == True and self.validate_distance() == True and self.validate_weight() == True):
            # GENERATE ID
            self.freight_id = Freight.counter+2

            # considering per kg weight = 150 rupees and per km distance = 60 rupees
            self.freight_charge = (self.weight*150) + (self.distance*60)

        else:
            self.freight_charge = 0

    def get_freight_charge(self):
        return self.freight_charge

    def get_frieght_id(self):
        return self.freight_id

    def get_recipient_customer(self):
        return self.recipient_customer.get_customer_id()

    def get_from_customer(self):
        return self.from_customer.get_customer_id()

    def get_weight(self):
        return self.weight

    def get_distance(self):
        return self.distance


class Customer:
    def __init__(self, customer_id, customer_name, address):
        self.customer_id = (str(customer_id))
        self.customer_name = customer_name
        self.address = address

    def validate_customer_id(self):
        if(self.customer_id[0] == "1" and len(self.customer_id) == 6):
            return True
        else:
            return False

    def get_customer_id(self):
        return self.customer_id

    def get_customer_name(self):
        return self.customer_name

    def get_address(self):
        return self.address


cust_1 = Customer(100001, "Dinesh", "Mumbai")
cust_2 = Customer(100002, "XYZ", "Delhi")

freight = Freight(cust_1, cust_2, 50, 600)
freight.forward_cargo()
print("Recipient: ", freight.get_recipient_customer())
print("From: ", freight.get_from_customer())
print("Weight : ", freight.get_weight())
print("Distance : ", freight.get_distance())
print("freight ID : ", freight.get_frieght_id())
print("Freight Charges: ", freight.get_freight_charge())
