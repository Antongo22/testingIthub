import pytest

def is_even(number):
    return number % 2 == 0

@pytest.mark.parametrize("number, expected", [
    (2, False), # провальный
    (3, False), 
    (0, True),
    (-2, True),
    (-3, True)  # провальный
])
def test_is_even(number, expected):
    assert is_even(number) == expected



def calculate_area(length, width):
    if length < 0 or width < 0:
        return -1
    return length * width


@pytest.mark.parametrize("length, width, expected_area", [
    (5, 3, 10), # провальный
    (0, 10, 0),
    (7, 7, 49),
    (3.5, -2, -1),
    (10, -5, -50) # провальный
])
def test_calculate_area(length, width, expected_area):
    assert calculate_area(length, width) == expected_area




def classify_triangle(a, b, c):
    if a == b == c:
        return "равносторонний"
    elif a == b or b == c or a == c:
        return "равнобедренный"
    else:
        return "разносторонний"


@pytest.mark.parametrize("a", [3, 5, 6, 10])
@pytest.mark.parametrize("b", [3, 5, 8, 10])
@pytest.mark.parametrize("c", [3, 8, 6, 10])
def test_classify_triangle(a, b, c):
    if a == b == c:
        expected_type = "ошибка" # провальный
    elif a == b or b == c or a == c:
        expected_type = "равнобедренный"
    else:
        expected_type = "разносторонний"
    assert classify_triangle(a, b, c) == expected_type