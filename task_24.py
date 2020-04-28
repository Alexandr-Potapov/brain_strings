"""Дана строка. Определить, содержит ли строка только символы 'a', 'b', 'c' или нет."""


def is_string_valid(test_from_user):
    final_set = {'a', 'b', 'c'}
    set_from_user = set(test_from_user)

    result_set_difference = set_from_user.difference(final_set)

    return len(result_set_difference) == 0


from_user = input('Введите текст: ')
print("Содержит ли текст только символы 'a', 'b', 'c'? %s" % is_string_valid(from_user))
