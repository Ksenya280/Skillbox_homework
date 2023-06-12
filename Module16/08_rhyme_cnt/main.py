N = int(input('Колличество человек: '))
number = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', number, 'человек.')
mens_list = list(range(1, N + 1))
out = 0

for _ in range(N - 1):
   print('Текущий круг людей', mens_list)
   start_count = out % len(mens_list)
   out = (start_count + number - 1) % len(mens_list)
   print('Начало счёта с номера', mens_list[start_count])
   print('Выбывает человек под номером', mens_list[out])
   mens_list.remove(mens_list[out])
   print()
print('Остался человек под номером', mens_list)
