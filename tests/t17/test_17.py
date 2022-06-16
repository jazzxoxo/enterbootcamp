import random
import string

from t17 import lenght

import pytest

@pytest.mark.timeout(1.0)
def test__17_01():
    assert lenght("123") == 3
    assert lenght("1") == 1