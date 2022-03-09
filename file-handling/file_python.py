
# open file and print its content

file = open("sample.txt", "r")
line1 = file.readline()
all_contents = file.read()

# Print only line 1
print(line1)

# print all lines
print(all_contents)

# print(file.read())
file.close()


#  Iterating through file object read the content line by line:
fhr = open("sample.txt", "r")
for line in fhr:
    print(line, end="")
fhr.close()

# Edit file content - write operation
file1 = open("sample.txt", "w")
file1.write("Hey This file is edited")
file1.close()

# Print file
file2 = open("sample.txt", "r")
print(file2.read())
file2.close()


fhr = open("data.txt", "r")
data = fhr.read()
print("Before writing:")
print(data)
fhr.close()

# Open file with append mode
fhw = open("data.txt", "a")
num = fhw.write("\nthis new first line written\n")
num1 = fhw.write("this new second line written\n")
print("num:", num)
print("num1:", num1)
fhw.close()
fhr = open("data.txt", "r")
data = fhr.read()
print("After writing:")
print(data)
fhr.close()


# tell() method to get current position which is pointed by file object within the file.

fhr = open("data.txt", "r")
cur_pos = fhr.tell()
print(cur_pos)
data = fhr.readline()
print(data)
cur_pos = fhr.tell()
print(cur_pos)
data = fhr.readline()
print(data)
fhr.close()


# seek() function to navigate the file object pointer to the required position specified.
# file_object.seek(offset,[whence])
fhr = open("data.txt", "rb+")
print(fhr.tell())
fhr.seek(12)  # navigates to 12th position from beginning of the file
print(fhr.tell())
# navigates to 3rd position from current position of the file object position
fhr.seek(3, 1)
print(fhr.tell())
# navigates to 3rd position from end of the file in backward direction
fhr.seek(-3, 2)
print(fhr.tell())
fhr.close()


# File object attributes
# file_object.closed: closed attribute returns true if the file is closed else it will return false.

# file_object.mode: mode attribute returns mode in which the file has been opened.

# file_object.name: name attribute returns the name of the file opened.

fhr=open("data.txt","rb+")
print("file name:",fhr.name)
print("access mode:",fhr.mode)
print("closed?",fhr.closed)
fhr.close()
print("after closing the file closed?",fhr.closed)
