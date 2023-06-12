list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

can_continue = True
for x in list_1:
    for y in list_2:
        result = x * y
        print(x, y, result)
        if result == to_find:
            print('Found!!!')
            can_continue = False
            break
    if not can_continue:
        break



def iter_list(list_one: list, list_two: list, search: int):
    for num in list_one:
        for y in list_two:
            result = num * y
            print(num, y, result)
            if result == search:
                yield True
            yield False


solution = iter_list(list_1, list_2, to_find)

for i in solution:
    if next(solution):
        print('Found!!!')
        solution.close()

