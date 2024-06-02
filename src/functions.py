import json


def data_json():
    """Функция получает все операции из файла json"""
    with open("../operations.json", encoding='utf-8') as file:
        data = json.loads(file.read())

    return data


def executed_state_data():
    """Функция получает только выполненные операции (EXECUTED)"""
    executed_states = []
    data = data_json()
    for executed in data:
        if executed == {}:
            continue
        else:
            if executed['state'] == 'EXECUTED':
                executed_states.append(executed)

    return executed_states


def last_five_operation():
    """Функция получает последние 5 операций"""
    all_operation = executed_state_data()
    sorted_operations = sorted(all_operation, key=lambda x: x.get('date', '0'))
    last_operation = sorted_operations[-5:]
    return last_operation


# a = last_five_operation()
# for b in a:
#     print(b)
