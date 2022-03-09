# 1010101
#  10101
#   101
#    1 

n = 6
# for i in range(n-1, 0, -1):
#     for j in range(n-i):
#         print(" ", end=" ")

#     for j in range(2*i-1):
#         print(j % 2,end=" ")

#     print()

k = 2*n-2
for i in range(n, -1, -2):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k+1
    for j in range(1, i+2):
        print(j % 2, end=" ")
    print('\r')
