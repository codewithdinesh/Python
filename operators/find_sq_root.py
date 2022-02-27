# get input and find square root

import math
n = int(input("Enter number : "))

# by formula
square_root = int(n**(1/2))

print("square root of ", n, "is ", square_root)

# by method
square_root = math.sqrt(n)

print("square root of ", n, "is ", square_root)
