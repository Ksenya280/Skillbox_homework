first_list = []
second_list = []
count = 0
quantity_skates = int(input('Колличество коньков: '))
for i in range(quantity_skates):
    print('Размеры', i + 1, '-й пары: ', end='')
    size = int(input())
    first_list.append(size)

quantity_people = int(input('\nКолличество людей: '))
for j in range(quantity_people):
    print('Размер ноги', j + 1, '-го человека: ', end='')
    size_leg = int(input())
    second_list.append(size_leg)

for num in second_list:
    for i in range(len(first_list)):
        if first_list[i] >= num:
            first_list.remove(first_list[i])
            count += 1
            break
print('Наибольшее кол-во людей, которые могут взять ролики:', count)
