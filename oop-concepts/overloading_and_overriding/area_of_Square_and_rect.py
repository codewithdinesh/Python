class Area:
    def area(self, s1, s2=None):
        if(s2 is not None):
            print("Area of Reactangle =", s1*s2)
        else:
            print("Area of Square: ", s1*s1)


a1 = Area()
a1.area(5)
a1.area(5, 4)
