
# 1
dictionary = {'MSBTE': 'Maharashtra State Board of Technical Education',
              'CO': 'Computer Engineering',
              'SEM': 'Sixth'}
del dictionary['CO']
for key, values in dictionary.items():
    print(key)
dictionary.clear()
for key, values in dictionary.items():
    print(key)
del dictionary

# error dictionary not found/present
# for key, values in dictionary.items():
#     print(key)


# 2
dictionary1 = {'Google': 1,
               'Facebook': 2,
               'Microsoft': 3
               }
dictionary2 = {'GFG': 1,
               'Microsoft': 2,
               'Youtube': 3
               }
dictionary1.update(dictionary2)
for key, values in dictionary1.items():
    print(key, values)

# 3
temp = dict()
temp['key1'] = {'key1': 44, 'key2': 566}
temp['key2'] = [1, 2, 3, 4]
for (key, values) in temp.items():
    print(values, end = "")
