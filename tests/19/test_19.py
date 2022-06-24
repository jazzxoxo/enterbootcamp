import random
import string

import pytest

from growth import growth

@pytest.mark.timeout(1.0)
def test__19_01():
    assert growth(10000, 10) == 25937