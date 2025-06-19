import allure
import pytest
from data import DataResponse
from generators import DataCreatedUser
from user_methods import UserMethods


class TestCreatingUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user_returns_success_and_token(self, delete_user, request):
        user_body = DataCreatedUser.generate_body()
        response = UserMethods.created_user(user_body)
        token = response.json()["accessToken"]
        request.node.funcargs["delete_user"] = token
        actual_body = response.json()

        assert response.status_code == DataResponse.StatusCode.SUCCESS_200
        assert actual_body["success"] == DataResponse.Common.TRUE_SUCCESS

    @allure.title("Создание уже зарегистрированного пользователя")
    def test_create_user_already_exists_returns_403(self, creating_user):
        token, user_body = creating_user
        response = UserMethods.created_user(user_body)
        expected_body = DataResponse.CREATING_REGISTERED_USER
        actual_body = response.json()

        assert response.status_code == DataResponse.StatusCode.FORBIDDEN_403
        assert actual_body == expected_body

    @allure.title("Создание пользователя без заполненного одного из обязательных полей")
    @pytest.mark.parametrize("email, password, name", [
        ("", 123456, "ivanorlov"),
        ("emailexample@derinntal.ru", "", "ivanorlov"),
        ("emailexample@derinntal.ru", 123456, "")
    ])
    def test_create_user_with_missing_required_field_returns_error(self, email, password, name):
        user_body = {"email": email, "password": password, "name": name}
        response = UserMethods.created_user(user_body)
        expected_body = DataResponse.CREATING_USER_WITHOUT_FILLED_FIELD
        actual_body = response.json()

        assert response.status_code == DataResponse.StatusCode.FORBIDDEN_403
        assert actual_body == expected_body
