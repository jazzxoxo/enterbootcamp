import random
import string

import pytest

from date_to_date import date_to_date

@pytest.mark.timeout(1.0)
def test__19_01():
    assert date_to_date("28.06", "03.07") == 5
    assert date_to_date("03.07", "28.06") == 5