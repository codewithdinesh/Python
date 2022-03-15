# reverse a list 

num_list = [90, 10, 67, 89, 20]
for i in range(len(num_list)-1, -1, -1):
    print(num_list[i])
num_list.reverse()
print(num_list)
