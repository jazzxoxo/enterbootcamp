import importlib
import io
import sys
from contextlib import contextmanager
from unittest import mock

import pytest

MODULE_NAME = '36'

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

def test_1(capsys):
    output = execute_module_with_input_and_output(capsys, MODULE_NAME, "Hello!")[0]
    expected = "Hallo!"
    assert expected == output.strip(), "".join((repr(output.strip()), " != ", repr(expected)))

def test_2(capsys):
    output = execute_module_with_input_and_output(capsys, MODULE_NAME, "aAeE")[0]
    expected = "eEaA"
    assert expected == output.strip(), "".join((repr(output.strip()), " != ", repr(expected)))

def test_3(capsys):
    output = execute_module_with_input_and_output(capsys, MODULE_NAME, "Hello, Orissaare!")[0]
    expected = "Hallo, Orisseera!"
    assert expected == output.strip(), "".join((repr(output.strip()), " != ", repr(expected)))