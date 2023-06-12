import os
def custom_key (gamers) :
    return gamers [2]
def result (lst1):
    min_result = 0
    gamers = []
    for row in lst1:
        lst2 = []
        data = row.split()
        if data[0].isdigit():
            min_result += int(data[0])
        else:
            lst2 += data
            lst2[1] = lst2[1][0] + '.'
            lst2[0], lst2[1] = lst2[1], lst2[0]
            if int(lst2[2]) > min_result:
                gamers.append(lst2)
    return sorted(gamers)

tour_1 = open('first_tour.txt', 'r', encoding = 'utf-8')
gamers = result(tour_1)

gamers.sort(key = custom_key, reverse = True)

with open('second_tour.txt', 'w', encoding = 'utf-8') as f_out:
    f_out.write(''.join(str(len(gamers)) + '\n'))
    row = 1
    for i in gamers:
        j = f'{row}) '+' '.join(i) + '\n'
        f_out.write(j)
        row += 1
    f_out.close()