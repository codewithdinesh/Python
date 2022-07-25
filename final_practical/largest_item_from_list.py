def largestItem(list):
    largest = 0
    for i in list:
        if(i >= largest):
            largest = i

    print(largest)


list = [10, 20, 30, 90, 50, 10]
largestItem(list)
