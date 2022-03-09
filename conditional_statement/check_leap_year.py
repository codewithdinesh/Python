# GET input year and check this year is leap year or not

year = int(input("Enter year: "))
if(year % 4):
    print("This is leap year")
elif(year % 400):
    print("This is leap year")
else:
    print("this is not leap year")
