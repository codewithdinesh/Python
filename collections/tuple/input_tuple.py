list = []

l = int(input("Enter lenght of list: "))
for i in range(0, l-1):
    ink= int(input("Enter number"))
    list.append(ink)

t= tuple(list)
print(t)