from src.math_operations import multiply


def test_multiply():

    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0