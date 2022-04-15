# What is the output of the following program?
# 1
def myfunc(text, num):
    while num > 0:
        print(text)
        num = num - 1


myfunc('Hello', 4)


# 2
num = 1


def func():
    num = 3
    print(num)


func()
print(num)
