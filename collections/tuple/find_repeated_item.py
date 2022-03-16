# Display Repeated tuple elements

tuple = (10, 990, 300, 200, 10)

for i in range(0, len(tuple)):
    for j in range(i+1, len(tuple)):
        if(tuple[i] == tuple[j]):
            print(tuple[j])
