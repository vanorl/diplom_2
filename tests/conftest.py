import pytest
from data import Ingredients
from generators import DataCreatedUser
from order_methods import OrderMethods
from user_methods import UserMethods


@pytest.fixture
def creating_user():
    user_body = DataCreatedUser.generate_body()
    body = UserMethods.created_user(user_body)
    token = body.json()["accessToken"]
    yield token, user_body
    UserMethods.delete_user(token)

@pytest.fixture
def creating_user_and_order(creating_user):
    user_body = DataCreatedUser.generate_body()
    body = UserMethods.created_user(user_body)
    token = body.json()["accessToken"]
    order_body = Ingredients.ingredients_body()
    OrderMethods.created_order(order_body, token)
    yield token
    UserMethods.delete_user(token)

@pytest.fixture
def delete_user(request):
    token = None
    yield token
    UserMethods.delete_user(token)
