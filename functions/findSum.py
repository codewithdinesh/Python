# Function for return sum of n digit 
# if n =3 then Sum = 0+1+2+3

def find_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i

    return sum

num = int(input("Enter N Number : "))

result = find_sum(num)

print("Sum of first ",num ," is : ",result )
