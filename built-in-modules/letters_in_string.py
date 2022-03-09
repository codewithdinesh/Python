def count_letters(text):
    count = 0
    t = text

    for char in t:
        if(char != " "):
            count += 1

    return count


text = input("Enter string : ")

# print length
print("There are ", count_letters(text), " letters present in String")
