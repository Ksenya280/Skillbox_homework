dataset = {}
for i in range(0, int(input('Количество стран: '))):
    value = input(f'{i + 1} страна: ').split()
    for town in value[1:]:
        dataset[town] = value[0]
for i in range(1, 4):
    city = input(f'\n{i} город: ')
    country = dataset.get(city)
    if country:
        print(f'Город {city} расположен в стране {country}.')
    else:
        print(f'По городу {city} данных нет.')
