import pytest

@pytest.fixture
def my_fixture():
    """give constant 42"""
    return 42


@pytest.fixture
def captured_print(capsys):
    """fixture using inbuilt fixture "capsys". """
    print("hello")

