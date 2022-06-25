import random
import string

import pytest

from person import person

@pytest.mark.timeout(1.0)
def test__32_01():
    assert person("liisa.txt") == "Their name is Liisa, they are 18 years old and live in Tartu."
    assert person("hanna.txt") == "Their name is Hanna, they are 30 years old and live in Narva."
    assert person("elisabeth.txt") == "Their name is Elisabeth, they are 20 years old and live in Tallinn."