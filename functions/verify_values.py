def verify(num1, num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return 1
    else:
        return num2


def display(arg1, arg2):
    if(verify(arg1, arg2) == arg1):
        print("A")
    elif(verify(arg1, arg2) == 1):
        print("C")
    else:
        print("B")


display(1000, 3500)

# find sum
result = 0


def find_sum(num1, num2):
    if(num1 != num2):
        result = num1+num2
    else:
        result = 2*(num1+num2)


find_sum(3, 4)
print(result)
find_sum(5, 5)
print(result)

# find avg

result_avg = 0


def find_avg(list_num):
    result_sum = 0
    for num in list_num:
        result_sum += num
    result_avg = result_sum/len(list_num)


find_avg([5, 8, 5])
print(result_avg)
