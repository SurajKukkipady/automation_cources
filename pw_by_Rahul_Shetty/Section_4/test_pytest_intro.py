# Pytest is a testing engine for python
# A function that starts with test_ is considered a test case by pytest

import pytest

@pytest.fixture(scope="function") # scope can be function, class, module, or session
def setup():
    print("This is a the setup function")

def test_initiation_1(setup):
    print("This is the first test case")

def test_initiation_2(setup):
    print("This is the second test case")

# scope can be function, class, module, or session
# if scope is function, the setup function will be called before each test case
# if scope is class, the setup function will be called before each test case in the class
# if scope is module, the setup function will be called before each test case in the module
# if scope is session, the setup function will be called once before all test cases in the session