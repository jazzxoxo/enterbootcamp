import random
import string
import importlib

importlib.import_module("17")

import pytest

@pytest.mark.timeout(1.0)
def test__17_01():
    assert 17.length("123") == 3
    assert 17.length("1") == 1