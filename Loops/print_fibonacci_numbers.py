n1 = int(input("Enter 1st number: "))

f1 = [0,1]

for i in range(2,n1+1):
    f1.append(f1[i-1]+f1[i-2])

print(f1)
