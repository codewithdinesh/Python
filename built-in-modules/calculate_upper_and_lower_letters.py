from matplotlib.style import use


user_string = input("Enter Your String: ")

lower_letters = 0
upper_letters = 0


for i in user_string:
    if(i.isupper()):
        upper_letters += 1

    if(i.islower()):
        lower_letters += 1

print("Your String : ", user_string)

print("Lower Letters Present in String: ", lower_letters)

print("Upper Letters Present in String: ", upper_letters)
