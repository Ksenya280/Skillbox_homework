word = input("Введите слово: ")

for i in range(len(word)//2):
    if word[i] != word[-1-i]:
        print('\nСлово не является палиндромом')
        break
else:
    print('\nСлово является палиндромом')