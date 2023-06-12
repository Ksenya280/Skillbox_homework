text = input('Введите строку: ').split()
longword = ''
for word in text:
    if len(word) > len(longword):
        longword = word

print('Самое длинное слово:', longword)
print('Длина этого слова:', len(longword))