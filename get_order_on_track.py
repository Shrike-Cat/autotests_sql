import sender_stend_request
import data

#Гульцева Анастасия, 9 когорта - Финальный проект. Инженер по тестированию плюс


def test_get_order_track_success_response():  # тест1
    response = sender_stend_request.post_new_order(data.create_order)
    track_order = response.json()["track"]
    order_response = sender_stend_request.get_order_track(
        track_order)  # В переменную order_respons сохраняем результат запроса на получение заказа по треку
    assert order_response.status_code == 200  # Проверка, что код ответа 200
