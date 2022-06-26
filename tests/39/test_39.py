import random
import string

import pytest

from date_to_date import date_to_date

@pytest.mark.timeout(1.0)
def test__39_01():
    assert morse("Hello, World!") == ".... . .-.. .-.. --- --..--   .-- --- .-. .-.. -.. -.-.--"
    assert morse("Orissaare") == "--- .-. .. ... ... .- .- .-. ."   
    assert morse("Enter Bootcamp") == ". -. - . .-.   -... --- --- - -.-. .- -- .--."