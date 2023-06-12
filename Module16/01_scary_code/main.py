a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
number_five = a.count(5)
print('Кол-во цифр 5 при первом объединении:',number_five)

for _ in range(number_five):
    a.remove(5)

a.extend(c)
print('Кол-во цифр 3 при втором объединении:', a.count(3))
print('Итоговый список:', a)