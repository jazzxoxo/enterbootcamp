import random
import string

import pytest

from chessboard import chessboard

@pytest.mark.timeout(1.0)
def test__30_01():
    assert chessboard(2) == ["a1","a2","b1","b2"]
    assert chessboard(1) == ["a1"]
    assert chessboard(2) == ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]