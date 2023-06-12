def height(man):
    if man not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[man])


p_tree = {}
number = int(input('Введите количество человек: '))
for i in range(number - 1):
    print(i, 'пара:')
    child, parent = input().split()
    p_tree[child] = parent

heights = {}
for man in set(p_tree.keys()).union(set(p_tree.values())):
    heights[man] = height(man)

print('«Высота» каждого члена семьи:')
for key, value in sorted(heights.items()):
    print(key, value)