from src.functions import data_json, date_formatting_operation, hide_and_split


def test_data_json():
    pass


def test_date_formatting_operation():
    assert date_formatting_operation("2018-04-14T19:35:28.978265") == "14.04.2018"
    assert date_formatting_operation("2018-11-29T07:18:23.941293") == "29.11.2018"


def test_ide_and_split():
    assert hide_and_split("Счет 90424923579946435907") == "Счет **5907"
    assert hide_and_split("Счет 84163357546688983493") == "Счет **3493"
    assert hide_and_split("Maestro 4598300720424501") == "Maestro 4598 30** **** 4501"
    assert hide_and_split("Visa Gold 9447344650495960") == "Visa Gold 9447 34** **** 5960"
