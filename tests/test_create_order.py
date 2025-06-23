import allure
from data import Ingredients, DataResponse
from order_methods import OrderMethods


class TestCreatingOrder:

    @allure.title("Успешное создание заказа")
    def test_create_order_with_auth_returns_success(self, creating_user):
        token, user_body = creating_user
        order_body = Ingredients.ingredients_body()
        response = OrderMethods.created_order(order_body, token)
        actual_body = response.json()

        assert response.status_code == DataResponse.StatusCode.SUCCESS_200
        assert actual_body["success"] == DataResponse.Common.TRUE_SUCCESS

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth_returns_success(self, creating_user):
        token = ''
        order_body = Ingredients.ingredients_body()
        response = OrderMethods.created_order(order_body, token)
        actual_body = response.json()

        assert response.status_code == DataResponse.StatusCode.SUCCESS_200
        assert actual_body["success"] == DataResponse.Common.TRUE_SUCCESS

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients_returns_400(self, creating_user):
        token, user_body = creating_user
        order_body = Ingredients.BODY_WITHOUT_INGREDIENTS
        response = OrderMethods.created_order(order_body, token)
        actual_body = response.json()
        expected_body = DataResponse.ORDER_WITHOUT_INGREDIENTS

        assert response.status_code == DataResponse.StatusCode.BAD_REQUEST_400
        assert actual_body == expected_body

    @allure.title("Создание заказа с невалидным хешем ингредиента")
    def test_create_order_with_invalid_ingredient_hash_returns_500(self, creating_user):
        token, user_body = creating_user
        order_body = Ingredients.BODY_INVALID_HASH_INGREDIENT
        response = OrderMethods.created_order(order_body, token)

        assert response.status_code == DataResponse.StatusCode.SERVER_ERROR_500
