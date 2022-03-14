# WeCare insurance company wants to calculate premium of vehicles.
# Vehicles are of two types – "Two Wheeler" and "Four Wheeler". Each vehicle is identified by vehicle id, type, cost and premium amount.
# Premium amount is 2% of the vehicle cost for two wheeler and 6% of the vehicle cost for four wheeler. Calculate the premium amount and display the vehicle details.

class vehicle:

    def __init__(self, id, type, cost):
        self.id = id
        self.type = type
        self.cost = cost
        self.premium = 0

    def calculate_Premium(self):

        if(self.type == "Two Wheeler"):
            premium = (self.cost * 2)/100
            return premium
        elif(self.type == "Four Wheeler"):
            premium = (self.cost * 6)/100
            return premium
        else:
            return "Vehicle type is invalid"

    def display_Vehicle_details(self):
        print("Vehicle ID : ", self.id)
        print("Vehicle TYPE : ", self.type)
        print("Vehicle Cost :", self.cost)
        print("Vehicle Premium : ", self.calculate_Premium())


vehicle_Obj1 = vehicle(123, "wwo Wheeler", 43000)
# print(vehicle_Obj1.calculate_Premium())
vehicle_Obj1.display_Vehicle_details()
