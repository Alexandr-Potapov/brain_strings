"""Удалить в строке все цифры."""


import re


def delete_all_numbers(text_from_user):
    return re.sub('\d', '', text_from_user)


from_user = input('Введите текст: ')
print(delete_all_numbers(from_user))
