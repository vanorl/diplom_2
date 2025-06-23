import allure
import requests
from data import Url


class OrderMethods:

    @staticmethod
    @allure.step('Создание заказа')
    def created_order(body, token):
        header = {"Authorization": token}
        return requests.post(f'{Url.BASE_URL}{Url.CREATED_ORDER}', headers=header, json=body)