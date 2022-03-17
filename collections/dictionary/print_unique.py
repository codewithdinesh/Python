# print all unique values in a dictionary.

list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

print("Original List: ",list)

# using set ,because set contains unique items
unique_values = set()

for dis in list:
    for j in dis.values():
        unique_values.add(j)

print("\nUnique Values: ", unique_values, "\n")
