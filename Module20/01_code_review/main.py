students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt


pairs = []
for i in students:
    pairs += (i, students[i]['age'])


my_lst = f(students)[0]
l = f(students)[1]
print(my_lst, l)

# исправленный код
def interest_len(data):
    pairs = []
    interests = []
    last_names = ''
    for i in data:
        interests += data[i]['interests']
        last_names += data[i]['surname']
        pairs = [(i, j['age']) for i, j in students.items()]

    return interests, len(last_names), pairs


inter_len = interest_len(students)
print('Список пар "ID студента - Возраст":', inter_len[2])
print('Полный список интересов всех студентов:', set(inter_len[0]))
print('Общая длина всех фамилий студентов:', inter_len[1])


