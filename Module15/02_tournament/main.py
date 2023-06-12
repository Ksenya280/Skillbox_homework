participant_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day = []
for i in range (1, len(participant_list), 2):
    first_day.append(participant_list[i])
print('Первый день:', first_day)
