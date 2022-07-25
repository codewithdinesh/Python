marks = list()

for i in range(0, 5):
    state = "Enter marks of subject "+str(i)+" : "
    a = int(input(state))
    marks.append(a)

total = 0
for i in range(0, len(marks)):
    total = total+marks[i]

grade = total/500 * 100

if(grade >= 80 and grade <= 100):
    print("Grade A ")

elif (grade >= 60 and grade < 80):
    print("Grade B")

elif(grade >= 50 and grade < 60):
    print("Grade C")

elif (grade >= 40 and grade < 50):
    print("Grade D")

else:
    print("Fail")
