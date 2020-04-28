"""

Дана строка. Вывести первые три символа и последниe три символа, если длина строки больше 5. Иначе вывести первый
символ столько раз, какова длина строки.

"""


def string_transformation(text_from_user):
    if len(text_from_user) > 5:
        return text_from_user[:3] + text_from_user[-3:]
    else:
        return text_from_user[0] * len(text_from_user)


from_user = input('Введите текст: ')
print(string_transformation(from_user))
