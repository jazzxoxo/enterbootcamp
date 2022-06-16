import random
import string
import importlib
import sys

import pytest

module = importlib.import_module("17.py")

@pytest.mark.timeout(1.0)
def test__17_01():
    assert module.length("123") == 3
    assert module.length("1") == 1