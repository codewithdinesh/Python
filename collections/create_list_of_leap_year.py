# generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list.

def leap_year(year):
    leap_year_list=[]
    for i in range(year,year+15):
        if(i%4==0):
            leap_year_list.append(i)
        elif(i%400==0):
            leap_year_list.append(i)
    
    return leap_year_list

n = int(input("Enter year : "))
print("Next 15 years leap years are ",leap_year(n))


