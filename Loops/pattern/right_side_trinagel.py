size = 5
for i in range(size):
    for j in range(i):
        print(" ", end=" ")

    for k in range(0, size-i):
        print("*", end=" ")
    print()
