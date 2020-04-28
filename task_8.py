"""Проверить, является ли четырехзначное число палиндромом."""


def is_palindrom():
    while True:
        from_user = input('Введите четырехзначное число: ')

        if not from_user.isdigit() or int(from_user) // 1000 == 0:
            print('Ошибка ввода!')
            continue

        return from_user == from_user[::-1]


print('Является ли введенное число палиндромом: %s' % is_palindrom())
