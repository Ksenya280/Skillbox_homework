def find_coin(x, y, r):
    if (x ** 2 + y ** 2) ** 0.5 <= r:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')

print('Введите координаты монетки:')
x_m = float(input('X: '))

y_m = float(input('Y: '))

r = int(input('Введите радиус: '))

find_coin(x_m, y_m, r)
