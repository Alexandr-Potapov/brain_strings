"""Вывести на экран первых n простых чисел."""


import math


def is_prime(some_number):
    if some_number == 2:
        return True

    divider = 2
    limit = int(math.sqrt(some_number))

    while divider <= limit:
        if some_number % divider == 0:
            return False

        divider += 1

    return True


def simple_numbers():
    while True:
        numbers_count = input('Введите желаемое кол-во простых чисел: ')

        if numbers_count.isdigit():
            numbers_count = int(numbers_count)
            break
        else:
            print('Ошибка ввода!')

    number = 2

    while numbers_count > 0:
        if is_prime(number):
            print(number)
            numbers_count -= 1

        number += 1


simple_numbers()
