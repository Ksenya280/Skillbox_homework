import random


def get_chance():
    result = True
    chance = random.randint(1, 13)
    if chance == 13:
        result = False
    return result


MAX_NUMBER = 777
sum_num = 0
file_name = 'out_file.txt'
first_record = True


def save_number(number):
    global first_record
    if first_record:
        open(file_name, 'w').close()
        first_record = False
    with open(file_name, 'a', encoding='utf8') as file:
        file.write(str(number) + '\n')


while True:
    new_number = int(input('Введите число: '))
    sum_num += new_number
    if sum_num >= MAX_NUMBER:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
        save_number(new_number)
        break

    if get_chance():
        save_number(new_number)
    else:
        try:
            rnd_exception = random.randint(1, 13)
            if rnd_exception == 13:
                raise IndexError('Вас постигла неудача!')

        except Exception as e:
            print('Вас постигла неудача!')
        break
