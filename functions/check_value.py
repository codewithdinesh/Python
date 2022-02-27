def check_value(message, num):
    # trim above part of number
    msg = message[:num]
    return len(msg)


# line 4:function call statement
result = check_value('Infosys', 4)
print("Result:", result)
