data = dict()
number_orders = int(input('Введите количество заказов: '))
for number in range(1, number_orders + 1):
    order = input(f'{number} заказ: ').split()
    if order[0] in data:
        if order[1] in data[order[0]]:
            data[order[0]][order[1]] += int(order[2])
        else:
            data[order[0]][order[1]] = order[2]
    else:
        data[order[0]] = dict({order[1]: int(order[2])})

for i_elem in sorted(data):
    print(f'\n{i_elem}:')
    for element in sorted(data[i_elem]):
        print(f'\t{element}: {data[i_elem][element]}')