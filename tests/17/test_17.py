import random
import string
import importlib

importlib.import_module("17")

import pytest

@pytest.mark.timeout(1.0)
def test__17_01():
    assert length("123") == 3
    assert length("1") == 1