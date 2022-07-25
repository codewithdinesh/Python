def sum_num(n):
    sum = 0
    while(n != 0):
        remainder = n % 10
        sum = sum+remainder
        n //= 10
    return sum


n = int(input("Enter number: "))
print(sum_num(n))
