d1 = {
    "a": 100, "b": 200, "c": 300
}

d2 = {
    "a": 300, "b": 200, "d": 400
}

# d1.update(d2)

for i, iv in d1.items():
    for j, jv in d2.items():
        if(i == j):
            d2[i] = iv+jv
        else:
            pass
print(d2)
