class area:
    def calculate(self, s, b=None):
        if(b is not None):
            print("Area of Rectangle : ", s*b)
        else:
            print("Area of Square: ", s*s)


a = area()
a.calculate(10,5)
