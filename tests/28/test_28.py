import random
import string

import pytest

from parameters_to_dict import parameters_to_dict

@pytest.mark.timeout(1.0)
def test__28_01():
    assert parameters_to_dict(10000, 10) == {0: 10000, 1:10}
    assert parameters_to_dict("a", "10") == {0: "a", 1:"10"}