t1 = (10, 20, 30, 40, "Hello")
t2 = (90, 89, 45, 70, "Welcome")

print("Before Swapping: ")
print("Tuple 1", t1)
print("Tuple 2", t2)

t1, t2 = t2, t1

print("After Swapping: ")
print("Tuple 1", t1)
print("Tuple 2", t2)