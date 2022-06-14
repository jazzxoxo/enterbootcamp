import importlib
import io
import sys
from contextlib import contextmanager
from unittest import mock

import pytest

MODULE_NAME = "0"

@contextmanager
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

def execute_module_with_output(capsys, module_name):
    """Execute module, pass input, return (stdout, stderr)."""
    execute_module(module_name)
    x = capsys.readouterr()
    return x.out, x.err

def test_printed(capsys):
    output = execute_module_with_output(capsys, MODULE_NAME)[0]
    assert "Hello, World!" in output, "spelling"
