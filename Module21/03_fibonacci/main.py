def fibonacci(num):
    if num in (1, 2):
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


number = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число:', fibonacci(number))