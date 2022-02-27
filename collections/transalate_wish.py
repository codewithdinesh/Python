# translate wish english to swedish, use dictionary of words.
# return translated wish

def translate(b_dict, list_words):
    wish_word = list_words.split()
    translatted = []
    translated_string = ""

    for key, value in b_dict.items():
        for item in wish_word:
            if(item == key):
                # translatted.append(value)
                translated_string = translated_string+" "+value

    # for item in translatted:
    #     translated_string = translated_string+" "+item

    return translated_string.strip()+" !"


wish = input("Enter your english wish: ")


words_dictionary = {"merry": "god", "christmas": "jul",
                    "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}

print("In English: ", wish)
print("In swedish: ", translate(words_dictionary, wish))
