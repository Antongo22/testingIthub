import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"
USER_URL = f"{BASE_URL}/user"
STORE_URL = f"{BASE_URL}/store/order"


@pytest.fixture
def create_user():
    user_data = {
        "id": 123,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1
    }
    response = requests.post(USER_URL, json=user_data)
    assert response.status_code == 200, "User creation failed"
    return user_data


def test_create_user(create_user):
    response = requests.get(f"{USER_URL}/{create_user['username']}")
    assert response.status_code == 200, "User not found after creation"
    data = response.json()
    assert data['username'] == create_user['username'], "User data mismatch"




@pytest.fixture
def create_order():
    order_data = {
        "id": 1,
        "petId": 100,
        "quantity": 2,
        "shipDate": "2023-10-31T00:00:00.000Z",
        "status": "placed",
        "complete": True
    }
    response = requests.post(STORE_URL, json=order_data)
    assert response.status_code == 200, "Order creation failed"
    return order_data


def test_get_order(create_order):
    response = requests.get(f"{STORE_URL}/{create_order['id']}")
    assert response.status_code == 200, "Order not found"
    data = response.json()
    assert data['status'] == create_order['status'], "Order status mismatch"


def test_delete_order(create_order):
    response = requests.delete(f"{STORE_URL}/{create_order['id']}")
    assert response.status_code == 200, "Failed to delete order"
    
    response = requests.get(f"{STORE_URL}/{create_order['id']}")
    assert response.status_code == 404, "Order still exists after deletion"
