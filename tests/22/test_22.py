import random
import string

import pytest

from combine import combine

@pytest.mark.timeout(1.0)
def test__19_01():
    assert sort(combine([1],[0])) == [0,1]
    assert sort(combine([1, 2],[3, 4])) == [1,2,3,4]