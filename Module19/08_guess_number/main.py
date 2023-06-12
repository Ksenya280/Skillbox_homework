max_number = int(input('Введите максимальное число: '))
first_set = set(range(1, max_number + 1))
for i in iter(lambda: input('Нужное число есть среди вот этих чисел: '), 'Помогите!'):
    second_set = set(map(int, i.split()))
    if input('Ответ Артёма: ') == 'Да':
        first_set &= second_set
    else:
        first_set -= second_set
print('Артём мог загадать следующие числа:', *first_set)