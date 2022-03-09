def invert_tringles(n):

    for i in range(0, n, 1):
        for j in range(i, n):
            print(" ", end=" ")

        for j in range(1, i*2):
            print("*", end=" ")

        print("")

    for i in range(n, 0, -1):

        for j in range(n-i):
            print(" ", end=" ")

        for j in range(2*i-1):
            print("*", end=" ")

        print()


n = 4
invert_tringles(n)


