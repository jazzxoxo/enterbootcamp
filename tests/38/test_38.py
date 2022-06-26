import random
import string

import pytest

from date_to_date import date_to_date

@pytest.mark.timeout(1.0)
def test__38_01():
    assert date_to_date("24.02.1918","28.06.2022") == 38111
    assert date_to_date("22.06.2013","12.04.2023") == 3582 
    assert date_to_date("28.06.2022","03.07.2022") == 5