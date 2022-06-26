import random
import string

import pytest

from value_from_key import value_from_key

@pytest.mark.timeout(1.0)
def test__26_01():
    assert value_from_key({"a":1}, "a") == 1
    assert value_from_key({"a":1, "b":2, "c":3}, "c") == 3
    assert value_from_key({"a":1, "b":2, "c":3}, "a") == 1
    assert value_from_key({"a":1, "b":2, "c":3}, "b") == 2
