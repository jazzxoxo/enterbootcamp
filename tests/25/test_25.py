import random
import string

import pytest

from how_many_keys import how_many_keys

@pytest.mark.timeout(1.0)
def test__25_01():
    assert how_many_keys({}) == 0
    assert how_many_keys({"a":1}) == 1
    assert how_many_keys({"a":1, "b":2, "c":3}) == 3
