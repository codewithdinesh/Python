# find the highest 3 values in a dictionary

# way 1 : by counter
from collections import Counter

dict = {1: 200, 2: 3000, 3: 100, 4: 5000, 5: 702}

k = Counter(dict)

high = k.most_common(3)

print("Dictionary with 3 height values : ")
for i in high:
    print(i[0], " : ", i[1])

# way 2
my_keys = sorted(dict.items(), key=lambda item: item[1], reverse=True)[:3]
print(my_keys)
