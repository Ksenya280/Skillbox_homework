
word = input('Введите слово: ')
letter = len([i for i in set(word) if word.count(i) == 1])
print('Количество уникальных букв:',letter )