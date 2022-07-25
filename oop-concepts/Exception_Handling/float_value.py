# raise error if value is float

try:
    n=int(input("Enter number: "))
    # print(type(n))

    if(isinstance(n,float)):
        raise

except:
    print("Float Value Occured")