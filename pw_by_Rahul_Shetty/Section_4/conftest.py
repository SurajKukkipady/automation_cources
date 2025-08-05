import pytest

@pytest.fixture(scope="function")
def pre_setup():
    print("\nThis is a the setup function from conftest")