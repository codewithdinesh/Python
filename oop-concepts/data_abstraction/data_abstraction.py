# hiding data or infomation
class data:

    counter=0
    
    def put(self,name):
        self.name=name
    
    def get(self):
        print("Name : ",self.name)


d1=data()
d1.put("DINESH")
print(d1.name)
print(data.counter)

