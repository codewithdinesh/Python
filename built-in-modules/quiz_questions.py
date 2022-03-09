# Predict the output of the following code snippet.
# 1)

import math
import re
song = "JINGLE Bells jingle Bells Jingle All The Way"
song.upper()
song_words = song.split()
count = 0
for word in song_words:
    if(word.startswith("jingle")):
        count = count+1
print(count)


# 2)
sample_dict = {'a': 1, 'b': 2}
sample_dict.update({'b': 5, 'c': 10})
print(sample_dict.get('a'), sample_dict.get('b'), sample_dict.get('c'))


# 3)
word = "New Airlines4"
if(re.search(r"^N", word) and re.search(r"e$", word)):
    print(re.sub(r"New", r"Old", word))
else:
    print(re.sub(r"s(\d{1})", r"S\1", word))


# 4)
num_list = [100.5, 30.465, -1.22, 20.15]
num_list.insert(1, -100.5)
num_list.pop(0)
num_list.sort()
print(math.ceil(math.fabs(num_list[0])))
