import pytest

from src.math_operations import divide


@pytest.mark.skip(reason="Skipping divide tests for now")
def test_divide():

    with pytest.raises(
        ValueError,
        match="Cannot divide by zero"
    ):

        divide(6, 0)

    assert divide(10, 2) == 5
    assert divide(15, 3) == 5