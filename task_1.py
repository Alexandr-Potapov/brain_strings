"""Вывести на экран три числа в порядке, обратном вводу."""


def numbers_output():
    list_of_numbers = []

    for number_count in range(3):
        while True:
            from_user = input('Введите число №%s: ' % (number_count + 1))

            if from_user.isdigit():
                list_of_numbers.append(int(from_user))
                break
            else:
                print('Вы ввели не число! Повторите ввод')

    print(list_of_numbers[::-1])


numbers_output()
