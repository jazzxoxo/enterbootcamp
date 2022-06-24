import random
import string

import pytest

from decimal_to_binary import decimal_to_binary

@pytest.mark.timeout(1.0)
def test__24_01():
    assert decimal_to_binary(0) == "0"
    assert decimal_to_binary(7) == "111"
    assert decimal_to_binary(16) == "10000"
    assert decimal_to_binary(20) == "10100"
    assert decimal_to_binary(2) == "10"
    assert decimal_to_binary(1) == "1"