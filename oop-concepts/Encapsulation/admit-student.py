# A university wants to automate their admission process. Students are admitted based on marks scored in a qualifying exam.
# A student is identified by student id, age and marks in qualifying exam. Data are valid, if:

#   a. Age is greater than 20

#   b. Marks is between 0 and 100 (both inclusive)

# A student qualifies for admission, if

#   a. Age and marks are valid and

#   b. Marks is 65 or more

# Write a python program to represent the students seeking admission in the university.

class Student:
    def __init__(self):
        self.__student_id = None
        self.__age = None
        self.__marks = None

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_age(self, age):
        self.__age = age

    def set_marks(self, marks):
        self.__marks = marks

    def get_student_id(self):
        return self.__student_id

    def get_age(self):
        return self.__age

    def get_marks(self):
        return self.__marks

    def validate_age(self):
        if(self.__age > 20):
            return True
        else:
            return False

    def validate_marks(self):
        if(self.__marks >= 65):
            return True
        else:
            return False

    def check_qualification(self):
        if(self.__age > 20):
            if(self.__marks >= 65):
                return True
            else:
                return False
        else:
            return False


student1 = Student()
student1.set_student_id(101)
student1.set_age(21)
student1.set_marks(75)
print("Student Details:\nID: ", student1.get_student_id(), "\nAge:",
      student1.get_age(), "\nMarks: ", student1.get_marks())
print("Student Qualified: ", student1.check_qualification())
