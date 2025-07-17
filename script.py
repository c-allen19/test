import pytest

def test_add_positive():
    from maths_class import maths # Replace with your actual package and module
    assert maths(2,3).add() == 5


def test_divide_by_zero():
    from maths_class import maths
    with pytest.raises(ZeroDivisionError):
        maths(1,0).divide()

    
test_add_positive()
test_divide_by_zero()