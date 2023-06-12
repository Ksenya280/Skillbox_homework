import random
lst = []
for i in (range(0,10)):
    lst.append(random.randint(0,10))

print('Оригинальный список:', lst)    
print('Новый список:',list(zip(lst[::2], lst[1::2])))


# Второй вариант решения

# import random
# lst = [random.randint(0, 10) for _ in range(10)]
#
# new_list = [(v, lst[i * 2 + 1]) for i, v in enumerate(lst[::2])]
#
#
# print('Оригинальный список:', lst, '\nНовый список:', new_list)