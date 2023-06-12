number = int(input('Введите число: '))
number_list = []

for num in range(1, number):
    if num % 2 != 0:
        number_list.append(num)

print('Список из нечётных чисел от одного до',number, ':', number_list)
