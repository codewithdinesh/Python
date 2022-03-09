# check palindrome  Number or not
n = int(input("Enter number: "))
s = 0
temp = n
while n != 0:
    rem = n % 10
    s = (s*10)+rem
    n //= 10

if(temp == s):
    print("Palindrome Number")
else:
    print("Not palindrome number")
