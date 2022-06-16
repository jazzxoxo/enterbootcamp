import random
import string
import importlib

import pytest

@pytest.mark.timeout(1.0)
def test__17_01():
    assert importlib.import_module("17").length("123") == 3
    assert importlib.import_module("17").length("1") == 1