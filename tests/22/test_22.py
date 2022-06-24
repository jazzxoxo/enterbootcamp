import random
import string

import pytest

from combine import combine

@pytest.mark.timeout(1.0)
def test__22_01():
<<<<<<< HEAD
    assert (combine([1],[0])).sort() == [1,0]
    assert (combine([1, 2],[3, 4])).sort() == [1,2,3,4]
=======
    assert combine([1],[0]) == [1,0]
    assert combine([1, 2],[3, 4]) == [1,2,3,4]
>>>>>>> d738e4cf841a3fcd24bdaa3937165d27b3c1a4c0
