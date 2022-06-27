import random
import string

import pytest

from tic_tac_toe import tic_tac_toe

@pytest.mark.timeout(1.0)
def test__37_01():
    assert tic_tac_toe(["X","O","O","","X","O","","",""]) == True
    assert tic_tac_toe(["X","O","","X","O","X","O","",""]) == False
    assert tic_tac_toe(["","","","","","","","",""]) == False