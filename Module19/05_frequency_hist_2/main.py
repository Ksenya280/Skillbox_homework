text = input('Введите текст: ')
frequency = dict()
print('Оригинальный словарь частот:')
for symbol in set(text):
    print(f'{symbol} : {text.count(symbol)}')
    frequency[text.count(symbol)] = frequency.get(text.count(symbol), []) + [symbol]
print('Инвертированный словарь частот:')
for letter in frequency:
    print(f'{letter}: {frequency[letter]}')