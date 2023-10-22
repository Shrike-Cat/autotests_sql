import configuration
import data
import requests


def post_new_order(create_order):   # Создаем новый заказ
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                    json=create_order,
                    headers=data.headers)


def get_order_track(track_order):  # Получаем заказа по треку
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_ORDER,
                        params={"t": track_order})
