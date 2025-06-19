import random


class DataCreatedUser:

    @staticmethod
    def generate_body():
        return {"email": f'orlov{random.randint(1000, 9999)}@yandex.ru',
                "password": f'{random.randint(100000, 999999)}',
                "name": f'ivan{random.randint(100, 999)}'
                }
