def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

def fibonacci2(n):
    a = 0
    b = 1

    for i in range(0, n):
        print(a)
        c = a+b
        a = b
        b = c



n = int(input("Enter number : "))

for i in range(0, n):
    print(fibonacci(i))


# fibonacci2(n)
