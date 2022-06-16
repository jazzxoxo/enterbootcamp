import importlib
import io
import sys
from contextlib import contextmanager
from unittest import mock

import pytest

MODULE_NAME = '16'

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

def errormsg(o, e):
    m = (str(round(int(o.strip()))), " != ", e.strip())
    return "".join(m)

def test_1(capsys):
    output = execute_module_with_input_and_output(capsys, MODULE_NAME, "3\n4")[0]
    expected = "31875000"
    assert str(round(int(output.strip()))) == expected, errormsg(output, expected)

