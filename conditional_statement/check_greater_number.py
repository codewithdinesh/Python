# Display Graeter Number from the 3 numbers

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 =int(input("Enter 3rd number: "))

if(n1>n2):
    if(n1>n3):
        print("N1 is greater")

    else:
        print("N3 is greater")     

else:
    if(n2> n3):
        print("N2 is greater")
    else:
        print("N3 is greater")
        

