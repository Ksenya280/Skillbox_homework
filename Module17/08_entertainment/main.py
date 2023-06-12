import random

num_stick = int(input("Kоличество палок: "))
stick_ls = ['I' for _ in range(num_stick)]
num_stones = int(input("Количество бросков: "))


for throw in range(num_stones):
    print('Бросок', throw + 1, end = '. ')
    left_i = random.randint(1, num_stick)
    print('Сбиты палки с номера', left_i)
    right_i = random.randint(left_i, num_stick)
    print('по номер ', right_i)


for stick in range(left_i, right_i + 1):
    stick_ls[stick - 1] = '.'

print('\nРезультат:', ''.join(stick_ls))


