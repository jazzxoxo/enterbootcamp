import random
import string

import pytest

from occur import occur

@pytest.mark.timeout(1.0)
def test__17_01():
    assert occur("Hello!","l") == 2
    assert occur("", "a") == 0