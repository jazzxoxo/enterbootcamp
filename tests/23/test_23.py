import random
import string

import pytest

from append_and_sort import append_and_sort

@pytest.mark.timeout(1.0)
def test__23_01():
    assert append_and_sort([0,2,3],1) == [0,1,2,3]
    assert append_and_sort([1, 2],5) == [1,2,5]