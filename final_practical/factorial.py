import math


def factorial(n):
    # if(n <= 1):
    #     return n
    # else:
    #     return n * factorial(n-1)

    # total = 1
    # for i in range(1, n+1):
    #     total = total*i

    # return total

    return math.factorial(n)


num = int(input("Enter Number: "))

print(factorial(num))
