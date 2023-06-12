nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def list_of_lists(lists):
    if not lists:
        return []
    return list_of_lists(lists[:-1]) + ([lists[-1]] if not isinstance(lists[-1], list) else list_of_lists(lists[-1]))

print('Ответ:', list_of_lists(nice_list))

