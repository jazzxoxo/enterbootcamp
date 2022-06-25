import random
import string

import pytest

from palindrome import palindrome

@pytest.mark.timeout(1.0)
def test__35_01():
    assert palindrome("Racecar") == True
    assert palindrome("PhoNE") == False
    assert palindrome("RaCeCaR") == True
    assert palindrome("aaaaaaaaaaaAAAA") == True