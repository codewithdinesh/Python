def reverse_num(n):
    reverse = 0
    while(n != 0):
        remainder = n % 10
        reverse = (reverse*10)+remainder
        n //= 10
    return reverse


n = int(input("Enter number: "))
print(reverse_num(n))
