# In the Athlete class given below,
# a. make all the attributes private and
# b. add the necessary accessor and mutator methods
# Represent Maria, the runner and make her run.

class Athlete:

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def running(self):
        if(self.__gender == "girl"):
            print("150 Mtr. running")
        else:
            print("200 Mtr. running")


# athlete1
athlete1 = Athlete()
athlete1.set_name("Maria")
athlete1.set_gender("girl")
athlete1.running()

# athlete2
athlete2 = Athlete()
athlete2.set_name("Dinesh")
athlete2.set_gender("boy")
athlete2.running()
