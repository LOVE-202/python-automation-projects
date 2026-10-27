import pytest


@pytest.mark.parametrize("a,b,expected",
                   [       (2,3,6),
                         ( 4,5,20),
                          (0,10,0),]
                          )
def test_num(a,b,expected):
    assert a*b==expected


@pytest.mark.parametrize("x,y",[
        (1, 2),
        (3, 4),]
)