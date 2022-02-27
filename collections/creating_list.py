list_of_airlines = ["AL1", "AL2", "AL3"]

print("Iterating the list using range()")

# print all the list items by the given index in loop
for index in range(0, len(list_of_airlines)):
    print(list_of_airlines[index])

print("Iterating the list using keyword in")

# print all the list items
for airline in list_of_airlines:
    print(airline)

# print list
print(list_of_airlines)

## finding element in List
airline = "AL3"
if airline in list_of_airlines:
    print("Airline found")
else:
    print("Airline not found")

## List - slicing
name_list = ["Dinesh", "Alex", "Omkar", "Sanket", "Vedant", "Rohit"]
print("Original list: ", name_list)

# print element from index 1 to 4
print("After slicing list: ", name_list[1:4])


for x, y in zip(name_list, name_list[1:]):
    print(x, y)