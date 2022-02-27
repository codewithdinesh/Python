# Write a python function encode(message)  which performs the run length encoding for a given String and returns the run length encoded String.
# Example: message=AAAABBBBCCCCCCCC  output: 4A4B8C

def encode(message):
    msg = message
    list_of_msg = []
    list2 = {}
    encoded_string = ""
    for i in msg:
        list2.setdefault(i, msg.count(i))

    for key, value in list2.items():
        # print(key,value)
        list_of_msg.append(str(value)+key)

    for items in list_of_msg:
        encoded_string = encoded_string+items

    return encoded_string


msg = input("Enter Normal string: ")
print("Normal String: ", msg)
print("After Encoding: ", encode(msg))
