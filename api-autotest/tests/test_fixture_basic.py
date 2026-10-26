import pytest

@pytest.fixture
def numbers():
    return [1,2,3]
def test_length(numbers):
    assert len(numbers)==3
def test_first_element(numbers):
    assert numbers[0]==1