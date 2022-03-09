# takes the marks of 5 subjects and displays the grade.
# Get total marks of 5 subjects

sub_marks = []
Total_marks=0
print("Enter 5 subjects marks: ")

for i in range(0,5):
    print("Enter Subject ",i+1, " marks : ",end=" ")
    marks=int(input())
    sub_marks.append(marks)

for i in sub_marks:
    Total_marks+=i

print("Total Mraks: ",Total_marks)

grade = Total_marks/5

if(grade >= 75 and grade <= 100):
    print("A grade")
elif(grade >= 60 and grade < 75):
    print("B grade")
elif(grade >= 35 and grade < 60):
    print("C grade")
elif(grade >= 0 and grade < 35):
    print("D grade - Fail")
