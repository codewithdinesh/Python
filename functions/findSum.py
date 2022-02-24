def find_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i

    return sum

num = int(input("Enter N Number : "))

result = find_sum(num)

print("Sum of first ",num ," is : ",result )
