# Write a Python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
# The ticket number should be generated as airline:src:dest:number where

# Consider AL1 as the value for airline

# src and dest should be the first three characters of the source and destination cities.

# number should be auto-generated starting from 101

# The program should return the list of ticket numbers of last five passengers.
# Note: If passenger count is less than 5, then return the list of all generated ticket numbers.

def generate_ticket(src, des, n):
    airline = "AL1"
    ticket_number = airline
    auto_number = 101
    ticket_list = []

    for i in range(0, n):
        ticket_number = airline+":"+src+":"+des+":"+str(auto_number)
        ticket_list.append(ticket_number)
        auto_number = auto_number+1

    if(n < 5):
        return ticket_list
    else:
        return ticket_list[:5]


# Getting Source and Destination Cities
src = input("enter source city: (ex. DEL)")
des = input("Enter destination city: (ex. BOM)")

# getting n for number of ticktes
n = int(input("Enter number of ticket: "))

print("Tickets:", generate_ticket(src, des, n))
