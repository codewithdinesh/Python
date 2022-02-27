# strong number is a number which is the sum of factorial of each digit of number = given number

def check_strong_number(num):
    temp = num
    factorial_sum = 0
    for i in str(temp):
        factorial_sum = factorial_sum+factorial(int(i))

    if(factorial_sum == num):
        return "Strong"
    else:
        return "Not Strong"


def factorial(num):
    temp = 1
    for i in range(1, num+1):
        temp = temp*i
    return temp


n = int(input("Enter number : "))

print(n, " is ", check_strong_number(n))
