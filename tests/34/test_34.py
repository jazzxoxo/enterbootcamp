import random
import string

import pytest

from knight import knight

@pytest.mark.timeout(1.0)
def test__34_01():
    assert knight("A1").sort() == ["B3", "C2"].sort() 
    assert knight("H8").sort() == ["F7", "G6"].sort()
    assert knight("E5").sort() == ["G4","G6", "F7", "F3", "D7", "D3", "C6", "C4"].sort()