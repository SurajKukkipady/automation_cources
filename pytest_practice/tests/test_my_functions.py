import pytest
import src.my_function as my_function
import time

def test_add():
    result = my_function.add(2, 3)
    assert result == 5

def test_divide():
    result = my_function.divide(10, 2)
    assert result == 5

def test_divivde_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_function.divide(10, 0)

def test_add_strings():
        result = my_function.add("hello", "world")
        assert result == "helloworld"

@pytest.mark.slow
def test_very_slow():
     time.sleep(5)
     result = my_function.divide(10, 2)
     assert result == 5

@pytest.mark.skip(reason="This feature is currently under development")
def test_add():
    assert my_function.add(1, 1) == 2

@pytest.mark.xfail(reason="Known issue with division by zero handling")
def test_divide_by_zero():
    assert my_function.divide(1, 0) == 0