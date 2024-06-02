import json


def data_json(quantity_last_operations):
    """Функция получает последние N операций из файла json"""

    executed_states = []

    with open("../operations.json", encoding='utf-8') as file:
        data = json.loads(file.read())

    for executed in data:
        if executed == {}:
            continue
        else:
            if executed['state'] == 'EXECUTED':
                executed_states.append(executed)

    sorted_operations = sorted(executed_states, key=lambda x: x.get('date', '0'))
    last_operation = sorted_operations[-quantity_last_operations:]

    return last_operation


a = data_json(2)
for b in a:
    print(b)


def date_formatting_operation():
    pass
