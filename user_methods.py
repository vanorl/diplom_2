import allure
import requests
from data import Url


class UserMethods:

    @staticmethod
    @allure.step('Создание пользователя')
    def created_user(body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATED_USER}', json=body)

    @staticmethod
    @allure.step('Авторизация пользователем')
    def login_user(body):
        return requests.post(f'{Url.BASE_URL}{Url.LOGIN_USER}', json=body)


    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(token):
        header = {"Authorization": token}
        return requests.delete(f'{Url.BASE_URL}{Url.DELETE_USER}', headers=header)
