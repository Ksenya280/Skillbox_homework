def equal_three_num():
    first_yer = int(input("Введите первый год: "))
    second_year = int(input("Второй год: "))
    print(f'Годы от {first_yer} до {second_year} с тремя одинаковыми цифрами: ')
    bill = 0
    while True:
        for interval in range(first_yer, second_year + 1):
            count = interval
            while count > 0:
                frac = count % 10
                count //= 10
                frac = str(frac)
                interval = str(interval)
                for compare in interval:
                    if frac == compare:
                        bill += 1
                    elif bill == 3:
                        print(interval)
                    else:
                        bill = 0
        break

equal_three_num()
