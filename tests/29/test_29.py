import random
import string

import pytest

from file_to_dict import file_to_dict

@pytest.mark.timeout(1.0)
def test__29_01():
    assert file_to_dict("test.txt") == {1: "Hello", "Hello": "2"}