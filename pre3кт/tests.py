import pytest

@pytest.fixture
def resource():
    print("\nSetup: создаем ресурс")
    resource = {"name": "test_resource"}
    
    yield resource
    print("\nTeardown: удаляем ресурс")
    resource.clear()


@pytest.mark.parametrize("input_value, expected", [
    (1, 2),  
    (3, 6),  
    (5, 10)  
])
def test_double(input_value, expected):
    assert input_value * 2 == expected


def test_resource_name(resource):
    assert resource["name"] == "test_resource"

@pytest.mark.parametrize("key, expected", [
    ("name", "test_resource"),
    ("invalid_key", None)
])
def test_resource_key(resource, key, expected):
    assert resource.get(key) == expected


