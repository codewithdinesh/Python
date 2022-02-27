def generate_fibanacci(n):
    fibanacci_list = [0, 1]
    for i in range(2, n+1):
        new_list = fibanacci_list[i-1]+fibanacci_list[i-2]
        fibanacci_list.append(new_list)
        
    return fibanacci_list

n = int(input("Enter number: "))
print("Fibanacci series of first ", n, " is", generate_fibanacci(n))
