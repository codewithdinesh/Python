n1 = int(input("Enter number: "))

# f1 = [0,1]

# for i in range(2,n1):
#     f1.append(f1[i-1]+f1[i-2])

# print(f1)

f1 = 0
f2 = 1
series=0

for i in range(1, n1+1):
    print(f1,end=" ")
    series = f1+f2
    f1 = f2
    f2 = series
