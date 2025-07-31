import src.shapes as shapes
import pytest
import math

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(4, 5)

def test_area(my_rectangle):
    assert my_rectangle.area() == 4*5

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (4 + 5)