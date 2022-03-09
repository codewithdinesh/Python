
# Write a python function find_common_characters(msg1,msg2) to display all the common characters between given two strings. Return -1 if there are no matching characters.

import re


def find_common_character(s1, s2):
    common_words = []
    for i in s1:

        for j in s2:
            if(i == j and i != " "):
                print(j,end=" ")
               


s1 = "I like python"
s2 = "Java is a very popular language"
find_common_character(s1, s2)
