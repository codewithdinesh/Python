# combine two dictionary adding values for common keys

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# before combine
print(d1)

d1.update(d2)

# after combine
print(d1)
