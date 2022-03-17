# Print the number in words for Example: 1234 => One Two Three Four

numbers_words = ("Zero", "One", "Two", "Three", "Four", "Five",
           "Six", "Seven", "Eight", "Nine")

n = input("Enter numbers :")

word_number = ""
for i in range(0, len(n)):
    for j in range(0, len(numbers_words)):
        index = int(n[i])
    word_number += numbers_words[index]+" "

print("Numbers into String : ")
print(word_number)
