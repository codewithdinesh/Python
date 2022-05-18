class students:
    def put(self, name, roll):
        self.name = name
        self.roll = roll


class studentInfo(students):
    def get(self):
        print("Name: ", self.name)
        print("Roll :", self.roll)


s = studentInfo()
s.put("Dinesh", 23)
s.get()
