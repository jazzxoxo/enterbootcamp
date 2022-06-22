import random
import string

import pytest

from combine import combine

@pytest.mark.timeout(1.0)
def test__22_01():
    assert combine([0,2,3],1) == [0,1,2,3]
    assert combine([1, 2],5) == [1,2,5]