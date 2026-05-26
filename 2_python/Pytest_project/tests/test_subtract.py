from src.math_operations import subtract


def test_subtract():

    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1
    assert subtract(10, 5) == 5