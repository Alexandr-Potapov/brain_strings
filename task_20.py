"""Проверить баланс круглых скобок в символьном выражении."""


def find_count(some_text):
    count_left_bracket = some_text.count('(')
    count_right_bracket = some_text.count(')')

    if count_left_bracket > count_right_bracket:
        message_to_user = "Кол-во '(' больше"
    elif count_left_bracket < count_right_bracket:
        message_to_user = "Кол-во ')' больше"
    else:
        message_to_user = "Кол-во '(' и ')' равно"

    print(message_to_user)


text_from_user = input('Введите произвольный текст:\n')
find_count(text_from_user)
