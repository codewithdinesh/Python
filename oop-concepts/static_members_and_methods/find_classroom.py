#  Write a python program to find out if a given classroom is present in the left wing of a university building. Implement the class, Classroom given below.

# Method/Attribute description:

# classroom_list: Static list which store the name of the class rooms in the left wing

# search_classroom(class_room): Static method which search for the given class room in the classroom_list. If found, return "Found". Else, return -1

# Note: Perform case insensitive string comparison

class classroom:
    classroom_list = ["classroom_1", "classroom_2",
                      "classroom_3", "classroom_4"]

    def search_classroom(self, class_room):
        for _class in classroom.classroom_list:
            if(_class.lower() == class_room.lower()):
                return "Found"
            else:
                return "Not Found"


class1 = classroom()
print(class1.search_classroom("Classroom_1"))
