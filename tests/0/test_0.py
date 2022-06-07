import importlib
import io
import sys
from contextlib import contextmanager
from unittest import mock

import pytest

MODULE_NAME = '0'

@contextmanager
def execute_module(module_name):
    """Execute module by name."""
    reload = module_name in sys.modules
    mod = importlib.import_module(module_name)
    if reload:
        importlib.reload(mod)
    return mod

def test_printed():
    output = execute_module(MODULE_NAME)
    assert 'Hello, World!' in output, "Check spelling, the text should be \"Hello, World!\"."#palun tööta