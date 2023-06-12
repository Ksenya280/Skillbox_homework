import json

with open('json_old.json', mode='r', encoding='utf-8') as file:
    old_data = json.load(file)

with open('json_new.json', mode='r', encoding='utf-8') as file:
    new_data = json.load(file)

diff_list = ['services', 'staff', 'datetime']

result = {}

for key in diff_list:
    if old_data['data'][key] != new_data['data'][key]:
        result[key] = new_data['data'][key]

with open('result.json', mode='w', encoding='utf-8') as file:
    json.dump(result, file)

print(result)