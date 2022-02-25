# There are 4 type of function argunment passing
# 1) Positional - normal function
def func(num):
    return num*num


print("Square : ", func(20))

# 2) keyword


def keyword(n1, n2):
    return n1*n2


print("Multiplication: ", keyword(n2=10, n1=20))

# 3) Default


def default(n1, n2=15):
    return n1+n2


print("Multiplication: ", default(10))

# 4) Variable argunment count

def argFunction(n1, n2, *n3):
    sum = n1+n2
    temp = 0
    for i in n3:
        temp = i+temp
    return sum+temp


print("Sum =: ", argFunction(10, 20, 30, 40, 50))
