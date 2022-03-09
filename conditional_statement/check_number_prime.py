# Check given number is prime or not
# prime number is a number which is only divisible by 1 and itself.


n1 = int(input("Enter 1st number: "))
flag = False

if(n1 > 1):
    for i in range(2, n1):
        if(n1 % i) == 0:
            flag = True
            break

if flag:
    print("Not prime ")

else:
    print("Prime Number ")
