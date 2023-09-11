import sender_stand_request
import data


def get_kit_body(name):  # присвоение имени набору
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):  # позитивная проверка
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


def negative_assert_symbol(name):  # негативная проверка
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


def test1_kit_body_name_1_letter_positive():
    positive_assert("a")


def test2_kit_body_name_511_letters_positive():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


def test3_kit_body_name_none_letter_negative():
    negative_assert_symbol("")


def test4_kit_body_name_512_letters_negative():
    negative_assert_symbol(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test5_kit_body_name_english_letters_positive():
    positive_assert("QWErty")


def test6_kit_body_name_russian_letters_positive():
    positive_assert("Мария")


def test7_kit_body_name_special_symbols_positive():
    positive_assert("\"№%@\",")


def test8_kit_body_name_space_allowed_positive():
    positive_assert("Человек и КО")


def test9_kit_body_name_numbers_allowed_positive():
    positive_assert("123")


def negative_assert_noname(kit_body):  # негативная проверка
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400


def test10_create_new_kit_no_name_negative():     # Для Ревью. Поправил данный тест, как мне кажется все в соответствии с уроком который вы упоминали. Кусок кода с токеном решил не трогать т.к. пока не чувствую уверенности в своих силах и к этому решению я приходил с большим трудом. Сейчас прохожу курс на Степике, смогу лучше делать, но чуть позже :)
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_noname(kit_body)


def test11_create_new_kit_other_type_of_parameter_negative():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
