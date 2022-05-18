class Error(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))


try:
    pas = input("Enter password: ")

    if(len(pas) < 8):
        raise Error("Password Expection Occured.., Password should be greater than 8 digit")
    else:
        print("Password is ok")

except Error as e:
    print(e.value)
