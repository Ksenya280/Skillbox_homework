n = int(input('Введите число: '))
i = 1
while i <= n:
    i = i + 1
    if n % i == 0:
        print('Наименьший делитель, отличный от единицы:', i)
        break
