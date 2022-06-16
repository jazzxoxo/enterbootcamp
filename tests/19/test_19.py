import random
import string

import pytest

from occur import occur

@pytest.mark.timeout(1.0)
def test__19_01():
    assert occur(10000, 10) == 25937