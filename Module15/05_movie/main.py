films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

new_films = []
quantity = int(input('Сколько фильмов хотите добавить? '))
for _ in range(quantity):
    print('Введите название фильма: ', end='')
    movie = input()
    if movie in films:
        new_films.append(movie)
    else:
        print('Ошибка: фильма', movie, 'у нас нет :(')

print('\nВаш список любимых фильмов: ')
print(new_films)
