
dictionary1 = {'Google': 10, 'Facebook': 200, 'Microsoft': 30}

# sort by value
print("sorted: ")
print(sorted(dictionary1.items(), key=lambda item: item[1]))
print("Reverse Sort:")

# sort by key
print(sorted(dictionary1, reverse=True))
