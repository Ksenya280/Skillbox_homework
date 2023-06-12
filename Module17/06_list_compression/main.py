import random

n = int(input('Количество чисел в списке: '))
list = [random.randint(0,2) for _ in range(n)]
print('Список до сжатия:',list)
list_after = [x for x in list if x]
print('Список после сжатия:', list_after)