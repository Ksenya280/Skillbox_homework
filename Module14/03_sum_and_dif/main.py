n = int(input('Введите число: '))


def sum(n):
    suma = 0
    while n > 0:
        digit = n % 10
        suma += digit
        n //= 10
    print("Сумма чисел:", suma)
    return suma


def quan(n):
    s = 0
    while n:
        s += 1
        n //= 10
    print('Колличество цифр в числе:', s)
    return s


difference = sum(n) - quan(n)

print('Разность суммы и количества цифр:', difference)
