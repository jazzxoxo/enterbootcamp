import importlib
import io
import sys
from contextlib import contextmanager
from unittest import mock

import pytest

MODULE_NAME = "0"

@contextmanager
def replace_stdin(target):
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig

#def test_print_hello(capsys):
#    import hello
#    importlib.reload(hello)
#    captured = capsys.readouterr()
#    assert "Hello, World!" in captured.out, "Does the code print \"Hello world!\"? The first letter should be a capital H."

def execute_module(module_name):
    """Execute module by name."""
    reload = module_name in sys.modules
    mod = importlib.import_module(module_name)
    if reload:
        importlib.reload(mod)
    return mod

def test_printed(capsys):
    output = execute_module(MODULE_NAME)
    assert "Hello, World!" in output, "spelling"
