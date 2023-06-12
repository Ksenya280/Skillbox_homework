text = input('Введите строку: ')
count = 0          
shifr = ''     
for i in range(len(text)):
    sim = text[i]
    count += 1
    if i == len(text) - 1: 
        shifr = shifr + text[i] + str(count)
        break
    if text[i] != text[i+1]:
        shifr = shifr + text[i] + str(count)
        count = 0
print ('Закодированная строка:', shifr)