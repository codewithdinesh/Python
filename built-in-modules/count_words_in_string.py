# calculate Words present in string

def count_words(string):
    words = string.split()
    return len(words)

text = input("Enter string : ")

print("There are ", count_words(text)," words in string")