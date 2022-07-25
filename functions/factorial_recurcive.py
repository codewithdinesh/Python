def f(n):
    if(n>0):
        return n*f(n-1)

    else:
        return 1


fact=f(3)
print(fact)