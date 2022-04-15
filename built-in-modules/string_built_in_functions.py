from distutils.filelist import translate_pattern


str = " hello, my name is dinesh "

print("Original String: ", str)

print("After capitalize()  ", str.capitalize())

print("After count('e') ", str.count("e"))

print("After endswith('h')  ", str.endswith('h'))

print("After index('o')  ", str.index('o'))

print("After isalnum()  ", str.isalnum())

print("After isalpha()  ", str.isalpha())

print("After split(' ')  ", str.split(" "))

print("After isdigit()  ", str.isdigit())

print("After islower()  ", str.islower())

print("After isupper()  ", str.isupper())

print("After lower()  ", str.lower())

print("After Strip() ", str.strip())

print("After startswith('x')  ", str.startswith(' h'))

print("After title()  ", str.title())

translate_dictionary = {97: 98, 101: 99}

print("After translate()  ", str.translate(translate_dictionary))
