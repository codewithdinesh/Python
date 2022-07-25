file = open("sample.txt", "r")

contents = file.read()
words = contents.split(" ")
lines = contents.split("\n")


print("Words:", len(words))
print("lines:", len(lines))
print("Characters: ",len(contents))
