import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


def save_data(data):
    sorted_data = sorted(data)
    with open('result.txt', 'w', encoding='utf8') as save_file:
        for row in sorted_data:
            save_file.write('\t'.join([str(item) for item in row]) + '\n')


line_number = 0
my_list = []
with open('coordinates.txt', 'r', encoding='utf-8') as coordinate_file:
    for row in coordinate_file:
        line_number += 1
        num_list = row.split()
        try:
            res1 = f(int(num_list[0]), int(num_list[1]))
            res2 = f2(int(num_list[0]), int(num_list[1]))
            number = random.randint(0, 100)
            my_list.append([number, res1, res2])
        except Exception:
            print('Что-то пошло не так')

    save_data(my_list)
