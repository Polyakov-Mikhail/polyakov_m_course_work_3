import json
import datetime
import os


def data_json(user_data_json):
    """Функция получает последние 5 операций из файла json"""

    executed_states = []
    path_operations = os.path.abspath(user_data_json)

    with open(path_operations, encoding='utf-8') as file:
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


def date_formatting_operation(data):
    """Перевод даты в формат ДД.ММ.ГГГГ"""
    data_corrected = datetime.datetime.fromisoformat(data).strftime('%d.%m.%Y')
    return data_corrected


def hide_and_split(card):
    """
    номер карты отображается в формате  XXXX XX** **** XXXX
    номер счета отображается в формате  **XXXX (видны только последние 4 цифры номера счета)
    """
    card_number = card.split()[-1]
    name_card = card.split()[:-1]
    if len(card_number) == 16:
        private_number = card_number[:4] + " " + card_number[4:6] + "** " + "**** " + card_number[-4:]
        correct_number = f'{" ".join(name_card)} ' + private_number
    else:
        correct_number = f'{card[:-len(card_number)]}{("**" + (card_number[-4:]))}'
    return correct_number


