count = 0
container = []
number = int(input('Кол-во контейнеров: '))
for _ in range(number):
    weith = (int(input('Введите вес контейнера: ')))
    if weith >= 200:
        print('Ошибка! Вес не может быть больше 200!')
    else:
        container.append(weith)

new = int(input('\nВведите вес нового контейнера: '))
while count < len(container) and container[count] >= new:
    count += 1
print('\nНомер, который получит новый контейнер:', count + 1)