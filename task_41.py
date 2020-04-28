"""

Дана строка. Если ее длина больше 10, то оставить в строке только первые 6 символов, иначе дополнить
строку символами 'o' до длины 12.

"""


def string_transformation(text_from_user):
    if len(text_from_user) > 10:
        return text_from_user[:6]
    else:
        return '{:o<12}'.format(text_from_user)


from_user = input('Введите текст: ')
print(string_transformation(from_user))
