import pytest

@pytest.fixture()
def nums():
    return [1,2,3]
def test_length(nums):
    assert len(nums)==3
def test_first(nums):
    assert nums[0]==1