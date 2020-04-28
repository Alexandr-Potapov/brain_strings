"""Вывести название дня недели по его номеру."""


def day_of_week_output():
    days_of_week = ['Понедельник',
                    'Вторник',
                    'Среда',
                    'Четверг',
                    'Пятница',
                    'Суббота',
                    'Воскресенье']
    while True:
        day_number = input('Введите номер дня недели: ')

        if not day_number.isdigit() or int(day_number) not in range(1, 8):
            print('Неверный ввод! Введите число в диапазоне 1-7!')
            continue

        print(days_of_week[int(day_number) - 1])
        break


day_of_week_output()
