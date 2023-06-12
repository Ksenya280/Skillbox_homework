def reversed(number):
    int_part = int(number)
    float_part = number - int_part
    reversed_int = 0
    reversed_float = 0
    while 0 < int_part:
        reversed_int = reversed_int * 10 + int_part % 10
        int_part //= 10
    while 1e-8 < float_part:
        reversed_float = reversed_float / 10 + int(float_part * 10) / 10
        float_part = float_part * 10 % 1
    return reversed_int + reversed_float


first_number = reversed(float(input('Введите первое число: ')))
second_number = reversed(float(input('Введите второе число: ')))
print('Первое число наоборот:', first_number)
print('Второе число наоборот:', second_number)
print(f'Сумма: {first_number + second_number}')