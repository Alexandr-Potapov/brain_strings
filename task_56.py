"""

Даны два предложения. Для каждого слова первого предложения определите количество его вхождений во второе предложение.

"""


def find_words_count(first_sentence, second_sentence):
    words_in_first_sentence = set(first_sentence.split(' '))
    words_in_second_sentence = second_sentence.split(' ')
    return {word: words_in_second_sentence.count(word) for word in words_in_first_sentence}


first_text = input('Введите первое предложение: ')
second_text = input('Введите второе предложение: ')
print(find_words_count(first_text, second_text))
