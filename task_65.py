"""Дан текст. Найти сумму имеющихся в нем цифр."""


import re


def find_sum(text_from_user):
    numbers_as_symbols = re.findall('\d', text_from_user)
    return sum([int(number) for number in numbers_as_symbols])


from_user = input('Введите текст: ')
print(find_sum(from_user))
