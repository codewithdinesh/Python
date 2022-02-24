# Display "ZIP" if given number is divisible by 3
# Display "Zap" if number is divisible by 5
# Display "Zoom" if given number is divisible by 5 and 3 both
# if number does not match any condition then Display "Invalid"

n = int(input("Enter Number"))
if(n/3):
    print("ZIp")
elif(n/5):
    print("Zap")
elif(n/5 and n/3):
    print("Zoom")
else:
    print("Invalid")
