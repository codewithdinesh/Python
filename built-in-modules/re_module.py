# Two commonly used methods in the re module are search and sub.
# Search is used to find a pattern and sub is used to perform a substitution.

# importing Regular expresion module
import re

# pattern are searched to be are case sensetive
if(re.search(r"Air", "Airline") != None):
    print("Pattern found")
else:
    print("Pattern not found")


flight_details = "Flight Savana Airlines a2134"
print(flight_details)
print(re.sub(r"Flight", r"Plane", flight_details))
