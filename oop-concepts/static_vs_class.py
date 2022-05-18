class Sample:
    __a = 10
    b = 20

    def __put(self):
        self.a = Sample.__a
        self.b = Sample.b

    def get(self):
        self.__put()
        print("A= ", self.a)
        print("B= ", self.b)


s = Sample()
s.get()
