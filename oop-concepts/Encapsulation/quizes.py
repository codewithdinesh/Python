# 1 What should be written in line 12 to get the output as 6?

class Example:
    def __init__(self):
        self.__num = 5

    def set_num(self, num):
        self.__num = num

    def get_num(self):
        return self.__num


obj = Example()
obj.set_num(6)
# line 16


# 2 What should be written in line 9 to get the output in line 13 as 5?
class Example:
    def __init__(self):
        self.__num = None

    def set_num(self, num):
        self.__num = num

    def change_num(self):
        # line 9
        return self.__num


obj = Example()
obj.set_num(10)
print(obj.change_num())

# Jennifer is a python developer who has written the below code:


class Dam:
    def __init__(self, name, length):
        self.name = name
        self.__length = length

    def get_length(self):
        return self.__length


dam1 = Dam("ABC dam", 3.5)
print("Dam name:", dam1.__name)
print("Dam Length", dam1.__length)
# She desires the output to be:
# Dam name: ABC dam
# Dam length: 3.5
# but, she is unable to proceed due to an error. Which of the following steps should she follow to get the desired output?
# YOU MUST CHOOSE TWO OPTIONS.
