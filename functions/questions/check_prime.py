def isPrime():
    num = int(input("Enter Number : "))

    if(num > 1):
        prime = True
        for i in range(2, num):
            if(num % i == 0):
                prime = False
        if(prime):
            print("YES PRIME NUMBER")
        else:
            print("NOT PRIME NUMBER")
    else:
        print("Prime is Greater than 1")


isPrime()
