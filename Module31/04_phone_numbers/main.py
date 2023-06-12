import re

phone_numbers = ['9999999999', '999999-999', '99999x9999']

for i, number in enumerate(phone_numbers):
    if not re.match(r'^[89]\d{9}$', number):
        print(f'номер {i + 1}: не подходит')
    else:
        print(f'номер {i + 1}: всё в порядке')

