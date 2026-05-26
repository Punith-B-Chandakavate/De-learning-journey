import pytest
import sys


@pytest.mark.skipif(
    sys.version_info < (3, 10),
    reason="Requires Python 3.10"
)
def test_version():

    assert True