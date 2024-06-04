from src.functions import data_json, date_formatting_operation, hide_and_split


def test_data_json():
    assert {
        "id": 147815167,
        "state": "EXECUTED",
        "date": "2018-01-26T15:40:13.413061",
        "operationAmount": {
            "amount": "50870.71",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 4598300720424501",
        "to": "Счет 43597928997568165086"
    } in data_json("../polyakov_m_course_work_3/tests/test_operations.json")
    assert {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {
          "amount": "48223.05",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431"
    } in data_json("../polyakov_m_course_work_3/tests/test_operations.json")


def test_date_formatting_operation():
    assert date_formatting_operation("2018-04-14T19:35:28.978265") == "14.04.2018"
    assert date_formatting_operation("2018-11-29T07:18:23.941293") == "29.11.2018"


def test_hide_and_split():
    assert hide_and_split("Счет 90424923579946435907") == "Счет **5907"
    assert hide_and_split("Счет 84163357546688983493") == "Счет **3493"
    assert hide_and_split("Maestro 4598300720424501") == "Maestro 4598 30** **** 4501"
    assert hide_and_split("Visa Gold 9447344650495960") == "Visa Gold 9447 34** **** 5960"
