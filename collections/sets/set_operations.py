# perform operations on set: intersection of sets, union of sets, set difference, symmetric difference, clear a set.

number = {10, 20, 30, 40, 50, 60, 70}
number2 = {30, 60, 90, 120, 150, 180, 200}

# intersection:
print("Intersection : ", number & number2)

print("Union : ", number | number2)

print("Difference : ", number - number2)

print("Symmetric Difference : ", number ^ number2)

# clear set
number.clear()

print(number)
