import importlib
import io
import sys
from contextlib import contextmanager
from unittest import mock

import pytest

MODULE_NAME = 'lemonade'

@contextmanager
def replace_stdin(target):
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig


def execute_module(module_name):
    """Execute module by name."""
    reload = module_name in sys.modules
    mod = importlib.import_module(module_name)
    if reload:
        importlib.reload(mod)
    return mod


def execute_module_with_input_and_output(capsys, module_name, input_string):
    """Execute module, pass input, return (stdout, stderr)."""
    with replace_stdin(io.StringIO(input_string)):
        execute_module(module_name)
        x = capsys.readouterr()
        return x.out, x.err

def test_printed(capsys):
    output = execute_module_with_input_and_output(capsys, MODULE_NAME, "10")[0]
    expected = "0"
    assert expected == output.strip()

def test_printed(capsys):
    output = execute_module_with_input_and_output(capsys, MODULE_NAME, "100")[0]
    expected = "9"
    assert expected == output.strip()