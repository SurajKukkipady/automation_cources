import pytest
import src.shapes as shapes

@pytest.mark.parametrize("side_length, expected_area", [
    (2, 4),(3, 9),(4, 16),(5, 25)])
def test_multiple_square_area(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area