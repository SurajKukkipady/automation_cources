import pytest
import src.my_function as my_function

def test_add():
    result = my_function.add(2, 3)
    assert result == 5

