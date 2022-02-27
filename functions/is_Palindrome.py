# check the given number is palindrome or not
# palindrome number is a number that is same after reverse

def is_Palindrome(num):
    temp = num
    sum = 0
    while(temp > 0):
        rm = temp % 10
        sum = sum * 10 + rm
        temp = temp//10
    
    if sum == num:
        return "Palindrome number"
    else:
        return "not Palindrome number"


n = int(input("Enter number : "))
print("This number ", n," is ", is_Palindrome(n))

