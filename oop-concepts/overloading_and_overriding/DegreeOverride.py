class degree:
    def getDegree(self):
        print("I got a degree")


class Undergraduate(degree):
    def getDegree(self):
        print("I am a undergraduate")


class Postgraduate(degree):
    def getDegree(self):
        print("I am a PostGraduate")


d = degree()
uD = Undergraduate()
pD = Postgraduate()

d.getDegree()
uD.getDegree()
pD.getDegree()
