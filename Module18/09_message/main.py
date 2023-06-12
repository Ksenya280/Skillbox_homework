message = input('Сообщение: ')
new_message = ''
i_start = 0
for i in range(len(message)):
    if message[i].isalpha() == False:
        new_word = message[i_start:i]
        new_message += new_word[::-1] + message[i]
        i_start = i+1
    elif message[i].isalpha() == True and i == len(message) - 1:
        new_word = message[i_start:i]
        new_message += new_word[::-1]
print(new_message)