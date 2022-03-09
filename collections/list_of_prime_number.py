# write a Python function to return the list of prime numbers present in it.

# input:[7,9,11,13,15,20,23] output:[7,11,13,23]


def list_prime(n):

    list_number = []

    for n1 in n:
        prime = True
        for i in range(2, n1):
            if(n1 % i) == 0:
                prime = False
        if prime:
            list_number.append(n1)
    return list_number



n = [7, 9, 11, 13, 15, 20, 23]
print(list_prime(n))
