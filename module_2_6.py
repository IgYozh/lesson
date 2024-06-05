# Задача("Однокоренные"):

def single_root_words(root_word, *other_words):
    same_words = []

    for i in other_words:
        if i.upper() in root_word.upper()  or root_word.upper() in i.upper():
            same_words.append(i)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

# list1 = ['red', 'green', 'blue', 'orange', 'green', 'gray', 'green']
# color_count = list1.count('green')
# print('The count of color: green is ', color_count)
