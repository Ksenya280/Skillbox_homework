import random

first_teams = [round(random.uniform(5, 10), 2) for i in range(20)]
second_teams = [round(random.uniform(5, 10), 2) for i in range(20)]
finall_result = list(map(max, first_teams, second_teams))

print('Первая команда:', first_teams)
print('Вторая команда:', second_teams)
print('Победители тура:', finall_result)
