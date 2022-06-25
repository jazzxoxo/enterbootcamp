import random
import string

import pytest

from palindrome import palindrome

@pytest.mark.timeout(1.0)
def test__35_01():
    assert palindrome(["X","O","O","","X","O","","",""]) == True
    assert palindrome(["X","O","","X","O","X","O","",""]) == False
    assert palindrome(["","","","","","","","",""]) == False