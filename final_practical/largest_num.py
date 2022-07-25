n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
n3 = int(input("Enter number 3 : "))

if(n1>n2):
    if(n1>n3):
        print(n1," is largest number")
    else:
        print(n3," is largest number")

else:
    if(n2>n3):
        print(n2," is largest number")
    else:
        print(n3," is largest number")
