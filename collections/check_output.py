# 2) Which among the following statements may result in an error?

# Assume that the statements are executed in the order in which it is written.

list1 = [5, 10, 15, 20, 25]
print(len(list1))
print(list1[4])
# print(list1[5])
print(list1[4:5])
list1[2] = 12
print(list1)
list1 = list1+[8, 9]


# 2) Predict the output of the below code snippet.

my_list = [0]*5
for index in range(1, 5):
    my_list[index] = (index-1)*10
print(my_list)


# 3)Which among the following statements will cause execution to stop as a result of an error?

# Assume that the statements are executed in the order in which it is written.

tuple1 = (5, 10, 15, 20, 25)
print(len(tuple1))
# tuple1[2] = 100
# print(tuple1[5])
tuple1 = tuple1+(8, 9, "h")

# 4) Consider the following list of pan card numbers:

pancard_list = ["AABGT6715H", "UFFAC4352T",
                "IFSBD9163K", "JOOEC1225H", "RWXAFE187B"]

# What is the output of the below two print statements?

print(pancard_list[3][6], end=" ")
print(pancard_list[4][3:])


# 5) Predict the output of the below code snippet.

message = "welcome to Mysore"
word = message[-7:]
if(word == "Mysore"):
    print("got it")
else:
    message = message[3:14]
    print(message)

# cancat:

l1 =[10,20,90,70,"Dinesh","Omkar"]
l2=["Rohit","Sanket","vedant",90]

l3= l1+l2
print(l3)