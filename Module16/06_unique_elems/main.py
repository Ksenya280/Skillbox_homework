first_list = []
second_list = []
for i in range(3):
    print('Введите', i + 1, '-e','число для первого списка: ', end = '')
    name = input()
    first_list.append(name)

for i in range(7):
    print('Введите', i + 1, '-e','число для второго списка: ', end = '')
    name = input()
    second_list.append(name)

print('Первый список:', first_list)
print('Второй список:', second_list)

first_list.extend(second_list)

unique_numbers = list(set(first_list))
print('Новый первый список с уникальными элементами:',unique_numbers)
