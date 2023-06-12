list = ['Введите имя и фамилию нового контакта (через пробел): ', 'Введите номер телефона: ']
phonebook_dict = {}

while True:
    print('Введите номер действия:\n')
    print('1. Добавить контакт')
    print('2. Найти человека')
    action = input()

    if action == '1':
        string = str()
        for i in list:
            s = input(i)
            string += ' ' + s
        string = string.split()
        key = (string[0], string[1])
        if key in phonebook_dict:
            print('Такой человек уже есть в контактах.')
        else:
            phonebook_dict[key] = string[2]
            print('Текущий словарь контактов:', phonebook_dict)

    if action == '2':
        action = input('Введите фамилию для поиска: ')
        for k in phonebook_dict.keys():
            if action == k[1]:
                print(k[0], k[1], phonebook_dict[k])