year = int(input("Enter Year : "))

if((year % 400 == 0) and (year % 100 == 0)):
    print(year, " is Leap year")

elif((year % 4 == 0) and (year % 100 != 0)):
    print(year, " is leap year")

else:
    print(year, " is not leap year.")
