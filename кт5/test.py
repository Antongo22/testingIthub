import pytest
import requests
from pydantic import BaseModel, EmailStr
import allure

BASE_URL = "https://petstore.swagger.io/v2"
USER_URL = f"{BASE_URL}/user"
STORE_URL = f"{BASE_URL}/store/order"


class UserModel(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    phone: str
    userStatus: int


class OrderModel(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool


@pytest.fixture
@allure.step("Создание тестового пользователя")
def create_user():
    user_data = UserModel(
        id=123,
        username="testuser",
        firstName="Test",
        lastName="User",
        email="testuser@example.com",
        password="password123",
        phone="1234567890",
        userStatus=1
    )
    response = requests.post(USER_URL, json=user_data.dict())
    assert response.status_code == 200, "User creation failed"
    return user_data


@allure.feature("User Management")
@allure.story("Create and retrieve a user")
def test_create_user(create_user):
    with allure.step("Получение пользователя по имени"):
        response = requests.get(f"{USER_URL}/{create_user.username}")
    assert response.status_code == 200, "User not found after creation"
    
    data = response.json()
    validated_data = UserModel(**data)
    assert validated_data.username == create_user.username, "User data mismatch"


@pytest.fixture
@allure.step("Создание тестового заказа")
def create_order():
    order_data = OrderModel(
        id=1,
        petId=100,
        quantity=2,
        shipDate="2023-10-31T00:00:00.000Z",
        status="placed",
        complete=True
    )
    response = requests.post(STORE_URL, json=order_data.dict())
    assert response.status_code == 200, "Order creation failed"
    return order_data


@allure.feature("Order Management")
@allure.story("Retrieve an order")
def test_get_order(create_order):
    with allure.step("Получение заказа по ID"):
        response = requests.get(f"{STORE_URL}/{create_order.id}")
    assert response.status_code == 200, "Order not found"
    
    data = response.json()
    validated_data = OrderModel(**data)
    assert validated_data.status == create_order.status, "Order status mismatch"


@allure.feature("Order Management")
@allure.story("Delete an order")
def test_delete_order(create_order):
    with allure.step("Удаление заказа"):
        response = requests.delete(f"{STORE_URL}/{create_order.id}")
    assert response.status_code == 200, "Failed to delete order"
    
    with allure.step("Проверка отсутствия заказа после удаления"):
        response = requests.get(f"{STORE_URL}/{create_order.id}")
    assert response.status_code == 404, "Order still exists after deletion"
