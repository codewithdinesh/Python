# Output:
""" 

*
* *
* * *
* * * * 

"""

n = 4

# using for loop
for i in range(0, n):

    for j in range(0, i+1):
        print("*", end=" ")

    print("")

print("")
print("****BREAK***")
print("")
# using while loop:
i = 0
while(i < n):
    j = 0
    while(j <= i):
        print("*", end=" ")
        j+=1
    print("")
    i+=1
