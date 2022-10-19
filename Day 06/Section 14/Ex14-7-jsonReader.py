import json
with open('doctList.json', 'r') as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)

for dict in dict_list:
    print('이름: {}'.format(dict['name']))
    print('나이: {}'.format(dict['age']))
    print('키: {}'.format(dict['spec'][0]))
    print('몸무게: {}'.format(dict['spec'][1]))
    print()