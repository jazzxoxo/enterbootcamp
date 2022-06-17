import importlib
import io
import sys
from contextlib import contextmanager
from unittest import mock

import pytest

MODULE_NAME = '7'

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
    output = execute_module_with_input_and_output(capsys, MODULE_NAME, "Hello!\ne")[0]
    expected = "1"
    assert expected == output.strip(), "".join((output.strip(), " != ", expected))

def test_2(capsys):
    output = execute_module_with_input_and_output(capsys, MODULE_NAME, "aaa\na")[0]
    expected = "3"
    assert expected == output.strip(), "".join((output.strip(), " != ", expected))

def test_3(capsys):
    output = execute_module_with_input_and_output(capsys, MODULE_NAME, "Hello!\nl")[0]
    expected = "2"
    assert expected == output.strip(), "".join((output.strip(), " != ", expected))

def test_4(capsys):
    output = execute_module_with_input_and_output(capsys, MODULE_NAME, "adssdfasdgsadf\nx")[0]
    expected = "0"
    assert expected == output.strip(), "".join((output.strip(), " != ", expected))