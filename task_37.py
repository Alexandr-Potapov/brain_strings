"""Даны два слова. Найдите только те символы слов, которые встречаются в обоих словах только один раз."""


def find_symbols(first_word_from_user, second_word_from_user):
    all_found_symbols = []

    first_set = set(first_word_from_user)
    second_set = set(second_word_from_user)

    set_intersection = first_set.intersection(second_set)

    for symbol in set_intersection:
        if first_word_from_user.count(symbol) == second_word_from_user.count(symbol) == 1:
            all_found_symbols.append(symbol)

    return all_found_symbols


first_word = input('Введите первое слово: ')
second_word = input('Введите второе слово: ')
print("Общие символы в словах, которые встречаются только 1 раз: %s" % find_symbols(first_word, second_word))
