# find common items from two lists
list1=["Dinesh",100,80,89]
list2=["Hey",100,90,"Dinesh"]

for i in list1:
    for j in list2:
        if(i==j):
            print(i)

            