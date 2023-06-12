guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'гостей:', guests)
    come = input('Гость пришел или ушел? ')
    if come == 'пора спать':
        break
    name = input('Имя гостя: ')
    if come == 'пришел':
        if len(guests) >= 6:
            print('Прости,', name, 'но мест нет')
        else:
            print('Привет,', name)
            guests.append(name)

    elif come == 'ушел':
        print('Пока,', name)
        guests.remove(name)

print('\nВечеринка закончилась, все легли спать.')



