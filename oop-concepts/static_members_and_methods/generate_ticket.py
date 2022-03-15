#  generate tickets for online bus booking, based on the class diagram given below.
# attributes: name,id,source,destination,counter->static

# methods: __init(name,source,destination)
# validate_source_destination()
# generate_ticket()
# get_ticket_id()
# get_name()
# get_source()
# get_destination()

class Ticket:
    counter = 1

    def __init__(self, passenger_name, source, destination):
        self.passenger_name = passenger_name
        self.source = source
        self.destination = destination
        self.ticket_id = None

    def validate_source_destination(self):
        destination_list = ["mumbai", "pune", "chennai", "kolkata"]
        source_list = "Delhi"

        if(self.source == source_list and (self.destination.lower() == "mumbai" or self.destination.lower() == "pune" or self.destination.lower() == "kolkata" or self.destination.lower() == "chennai")):
            return True
        else:
            return False

    def generate_ticket(self):
        self.ticket_id = self.source[0]+self.destination[0]+str(Ticket.counter)
        Ticket.counter += 1

    def get_ticket_id(self):
        return self.ticket_id

    def get_passanger_name(self):
        return self.passenger_name

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination


Ticket_obj_1 = Ticket("Dinesh", "Delhi", "Mumbai")
Ticket_id = None

print(Ticket_obj_1.validate_source_destination())
if(Ticket_obj_1.validate_source_destination() == True):

    Ticket_obj_1.generate_ticket()
else:

    Ticket_obj_1.ticket_id = None

print("Ticket Details : ")
print("Passanger name : ", Ticket_obj_1.get_passanger_name())
print("Source : ", Ticket_obj_1.get_source())
print("Destination : ", Ticket_obj_1.get_destination())
print("Ticket ID : ", Ticket_obj_1.get_ticket_id())
