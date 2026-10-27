import pytest

@pytest.mark.parametrize("a,b,expected",[
    (2,3,5),
    (1,4,5),
    (0,5,5),
])
def test_add(a,b,expected):
    assert a+b==expected