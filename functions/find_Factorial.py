# Write a Python function factorial(num) which returns the factorial of a given number.

def factorial(num):
    temp = 1
    for i in range(1, num+1):
        temp = temp*i
    return temp


n = int(input("Enter Number to find factorial : "))
print("Factorial of ", n, " is : ", factorial(n))
