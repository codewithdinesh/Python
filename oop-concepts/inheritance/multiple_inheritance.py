class College:
    def setCollege(self,name):
        self.cName=name
    
class Department:
    def setDepartment(self,name):
        self.dName=name

class Lecture(College,Department):
    def setLecture(self,name):
        self.lName=name
    
    def getInfo(self):
        print("College : ",self.cName)
        print("Department : ",self.dName)
        print("Lecture : ",self.lName)

l1=Lecture()
l1.setCollege("GPR")
l1.setDepartment("Computer")
l1.setLecture("Python")
l1.getInfo()

