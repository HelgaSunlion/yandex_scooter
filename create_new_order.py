import requests
import configuration
import data

def test_create_order_and_check_tracking():
    # Шаг 1: Выполнить запрос на создание заказа
    response_create_order = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                                          json=data.create_order,
                                          headers=data.headers)

    # Проверить, что код ответа равен 201 (или другой код, который указывает на успешное создание заказа)
    assert response_create_order.status_code == 201

    # Получить номер трека заказа из ответа на создание заказа
    track_number = response_create_order.json().get("track")

    # Шаг 2: Выполнить запрос на получение заказа по треку заказа
    response_get_order = requests.get(configuration.URL_SERVICE + configuration.TRACK_NUMBER.replace("t=123456", f"t={track_number}"))

    # Проверить, что код ответа равен 200
    assert response_get_order.status_code == 200
