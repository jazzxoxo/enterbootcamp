import importlib
import io
import sys
from contextlib import contextmanager
from unittest import mock

import pytest

MODULE_NAME = 'greet_name'

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


def test_input_asked(monkeypatch):
    """Whether input() is called."""
    with mock.patch('builtins.input') as f:
        execute_module(MODULE_NAME)
        f.assert_called()


def test_greeting_printed(capsys):
    output = execute_module_with_input_and_output(capsys, MODULE_NAME, "test")[0]
    assert 'Hello, ' in output, "Check spelling, the text should be \"Hello, [name]\"."


def test_greeting_with_name(capsys):
    output = execute_module_with_input_and_output(capsys, MODULE_NAME, "tom")[0]
    assert 'tom' in output, "If input is provided, the program should use the input for greeting."