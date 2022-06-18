import random
import string

import pytest

from read_file import read_file

@pytest.mark.timeout(1.0)
def test__19_01():
    assert read_file("hello.txt") == "Hello, World!", "".join((read_file("hello.txt"), "!=", "Hello, World!"))