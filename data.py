class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CREATED_USER = '/api/auth/register'
    LOGIN_USER = '/api/auth/login'
    CREATED_ORDER = '/api/orders'
    GET_ORDERS_USER = '/api/orders'
    DELETE_USER = '/api/auth/user'


class Ingredients:
    BODY_WITHOUT_INGREDIENTS = {'ingredients': []}
    BODY_INVALID_HASH_INGREDIENT = {'ingredients': ['61c0c5a71d1f82001bdaaa6cwrong']}

    @staticmethod
    def ingredients_body():
        bun = '61c0c5a71d1f82001bdaaa6c'
        main = '61c0c5a71d1f82001bdaaa6e'
        sause = '61c0c5a71d1f82001bdaaa73'
        return {'ingredients': [bun, main, sause]}


class DataResponse:
    ORDER_WITHOUT_INGREDIENTS = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }

    CREATING_REGISTERED_USER = {
        "success": False,
        "message": "User already exists"
    }

    CREATING_USER_WITHOUT_FILLED_FIELD = {
        "success": False,
        "message": "Email, password and name are required fields"
    }

    AUTHORIZATION_WITH_INCORRECT_USERNAME_AND_PASSWORD = {
        "success": False,
        "message": "email or password are incorrect"
    }


    class StatusCode:
        SUCCESS_200 = 200
        BAD_REQUEST_400 = 400
        UNAUTHORIZED_401 = 401
        FORBIDDEN_403 = 403
        SERVER_ERROR_500 = 500

    class Common:
        TRUE_SUCCESS = True

class UserNegativeCases:
    user_negative_cases = [
        {"email": "", "password": "123456", "name": "ivanorlov"},
        {"email": "emailexample@derinntal.ru", "password": "", "name": "ivanorlov"},
        {"email": "emailexample@derinntal.ru", "password": "123456", "name": ""}
    ]