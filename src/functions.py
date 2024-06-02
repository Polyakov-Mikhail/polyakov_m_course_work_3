import json
import datetime


def data_json():
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
    last_operation = sorted_operations[-5:]

    return last_operation


def date_formatting_operation():
    """Перевод даты в формат ДД.ММ.ГГГГ"""
    last_operation = data_json()
    for data_corrected in last_operation:
        data_corrected["date"] = datetime.datetime.fromisoformat(data_corrected['date']).strftime('%d.%m.%Y')
    return last_operation


def hide_and_split():
    pass
