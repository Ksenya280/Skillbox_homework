import os
import string


def get_index(smb, to_right, lst):
    index = lst.index(smb)
    if index + to_right > len(lst) - 1:
        index = index + to_right - len(lst)
    else:
        index += to_right
    return index


path = os.path.abspath('text.txt')
file = open(path, 'r')
line_count = 0
encrypted_string = ''

ascii_en = [i for i in string.ascii_letters]
ascii_ru = [chr(i) for i in range(ord('а'), ord('я') + 1)]
ascii_ru += [chr(i) for i in range(ord('А'), ord('Я') + 1)]

for row in file:
    line_count += 1

    for symbol in row:
        if symbol in ascii_ru:
            encrypted_string += ascii_ru[get_index(symbol, line_count, ascii_ru)]
        elif symbol in ascii_en:
            encrypted_string += ascii_en[get_index(symbol, line_count, ascii_en)]
        else:
            encrypted_string += symbol

file.close()

path = os.path.abspath('cipher_text.txt')
file_2 = open(path, 'w')
file_2.write(encrypted_string)
file_2.close()

