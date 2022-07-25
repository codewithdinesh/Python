# Write a Python function factorial(num) which returns the factorial of a given number.

from re import I


def factorial(num):
    temp = 1
    # for i in range(1, num+1):
    #     temp = temp*i

    # with while loop
    i = 1
    while(i < n+1):
        temp = temp*i
        i = i+1

    return temp


n = int(input("Enter Number to find factorial : "))

if(n > 1):
    print("Factorial of ", n, " is : ", factorial(n))
else:
    print("Factorial number can not be negative")
