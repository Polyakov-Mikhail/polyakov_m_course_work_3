import json


def data_json():
    with open("../operations.json") as file:
        data = json.loads(file.read())

    return data


print(data_json())
