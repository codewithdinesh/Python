# sum of proper diviser of number 1 is = number 2 
# and sum of proper diviser of number 2 is = number 1
# are the amicable number

def check_amicable_numbers(n1, n2):
    sum = 0
    sum2 = 0
    temp1 = n1
    temp2 = n2

    for i in range(1, temp1):
        if(temp1 % i == 0):
            sum = sum + i
        else:
            sum = sum

    for i in range(1, temp2):
        if(temp2 % i == 0):
            sum2 += i

    if(sum == n2 and sum2 == n1):
        return "amicable"
    else:
        return "not amicable"


n =int(input("Enter number 1:"))
n1 = int(input("Enter number 2: "))

print(n," and ",n1," are ",check_amicable_numbers(n, n1))
