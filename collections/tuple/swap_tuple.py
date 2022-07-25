t1 = tuple()
n = int(input("Total number of values in first tuple"))
for i in range(n):
    a = input("enter elements")
    t1 = t1+(a,)

t2 = tuple()

m = int(input("Total number of values in second tuple"))
for i in range(m):
    a = input("enter elements")
    t2 = t2+(a,)

print("Before SWAPPING")
print("First Tuple", t1)
print("Second Tuple", t2)

t1, t2 = t2, t1
print("AFTER SWAPPING")
print("First Tuple", t1)
print("Second Tuple", t2)
