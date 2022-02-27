# shift  given number by n towards right 

def right_shift(num, n):
    res = num >> n
    return res


num = int(input("Enter number : "))
n = int(input("Enter number to shift towards right : "))

print("Before Shifting : ", num)
print("After Shifting :")
print("towards rights by ", n, " : ", right_shift(num, n))
