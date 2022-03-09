num =int(input("ENter number: "))
sum=0
while num!=0:
    rem = num%10
    sum =sum+rem
    num//=10

print(sum)