import pytest

@pytest.fixture(scope="function") # scope can be function, class, module, or session
def setup():
    print("This is a the setup function")
    return "Pass"

@pytest.fixture(scope="function") # scope can be function, class, module, or session
def setup2():
    print("This is a the setup function 2")
    yield
    print("This is the teardown function 2")

@pytest.mark.smoke
def test_initiation_1(setup, setup2):
    print("This is the first test case")
    assert setup == "Pass"

@pytest.mark.smoke
def test_initiation_2(setup):
    print("This is the second test case")

@pytest.mark.skip
def test_initiation_3(setup):
    print("This is the third test case")

#  pytest -m smoke to run only smoke tests