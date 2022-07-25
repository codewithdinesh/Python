f1=open("file-handling\data.txt","r+")
f2=open("file-handling\sample.txt","r")

f1.write(f2.read())
# f1.seek(0)
# print(f1.read())
f1.close()
f2.close()