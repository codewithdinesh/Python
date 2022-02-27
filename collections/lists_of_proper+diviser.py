# Write a Python function proper_divisors(num) which returns a list of all the proper divisors of given number.

# Example: Proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110

def proper_divisors(num):
    proper_divisor_list = []

    for i in range(1, num):
        if(num % i == 0):
            proper_divisor_list.append(i)

    return proper_divisor_list


n = int(input("Enter number: "))
print("Proper divisors of ", n, " are ", proper_divisors(n))
