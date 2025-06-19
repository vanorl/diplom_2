import allure

from data import DataResponse
from user_methods import UserMethods


class TestLoginUser:

    @allure.title("Авторизация под существующим пользователем")
    def test_login_with_valid_credentials_returns_success(self, creating_user):
        token, user_body = creating_user
        login_body = {
            "email": user_body["email"],
            "password": user_body["password"]
        }
        response = UserMethods.login_user(login_body)
        actual_body = response.json()

        assert response.status_code == DataResponse.StatusCode.SUCCESS_200
        assert actual_body["success"] == DataResponse.Common.TRUE_SUCCESS

    @allure.title("Авторизация с неверным логином и паролем")
    def test_login_with_invalid_credentials_returns_unauthorized(self, creating_user):
        token, user_body = creating_user
        login_body = {
            "email": f'wrong{user_body["email"]}',
            "password": f'wrong{user_body["password"]}'
        }
        response = UserMethods.login_user(login_body)
        expected_body = DataResponse.AUTHORIZATION_WITH_INCORRECT_USERNAME_AND_PASSWORD
        actual_body = response.json()

        assert response.status_code == DataResponse.StatusCode.UNAUTHORIZED_401
        assert actual_body == expected_body
