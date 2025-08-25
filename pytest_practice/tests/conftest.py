import pytest
import src.shapes as shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(4, 5)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5,6)