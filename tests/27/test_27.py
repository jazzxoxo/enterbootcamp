import random
import string

import pytest

from sum_of_lists_inside_a_dictionary import sum_of_lists_inside_a_dictionary

@pytest.mark.timeout(1.0)
def test__27_01():
    assert sum_of_lists_inside_a_dictionary({"a":[1]}) == {"a":1}
    assert sum_of_lists_inside_a_dictionary({"a":[1,2,3]}) == {"a":6}
    assert sum_of_lists_inside_a_dictionary({"a":[1], "b":[2,3]}) == {"a":1,"b":5}