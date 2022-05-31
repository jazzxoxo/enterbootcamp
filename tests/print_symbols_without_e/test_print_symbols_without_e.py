import importlib
import io
import sys
from contextlib import contextmanager
from unittest import mock

import pytest

MODULE_NAME = 'print_symbols'

@contextmanager
def replace_stdin(target):
    """
    This is used to replace standard in (for input()).
    """
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig


def execute_module(module_name):
    """
    Execute module by name.

    This is a helper function to (re)import a module.
    Keeps track whether module has been loaded already.
    """
    reload = module_name in sys.modules
    mod = importlib.import_module(module_name)
    if reload:
        importlib.reload(mod)
    return mod


def execute_module_with_input_and_output(capsys, module_name, input_string):
    """
    Execute module, pass input, return (stdout, stderr).


    capsys - a context from pytest, this should be passed in from the test function
    where it is used.
    module_name - indicates which module (python file) to load/execute.
    input_string - is an input for this module. So, when the module is executed,
    the given input is sent to the program (for input() function).

    This function returns a tuple (standard output, standard error).

    Usage:
    output = execute_module_with_input_and_output(capsys, "my_module", "12\n13")

    This sends the string "12\n13" into the given module (program).
    If the program asks 2 x input() it would receive "12" and then "13".
    output[0] is a string with all the output (print() result) of the module.
    output[1] has all the std err contents.
    """
    with replace_stdin(io.StringIO(input_string)):
        execute_module(module_name)
        x = capsys.readouterr()
        return x.out, x.err


def test_input_asked(monkeypatch):
    """
    Whether input() is called.

    We can test whether a certain function/method is called.
    If not, then this test fails.
    This can be used to give hints to the developer.
    """
    with mock.patch('builtins.input') as f:
        execute_module(MODULE_NAME)
        f.assert_called()


def __test_result(capsys, input_string):
    output = execute_module_with_input_and_output(capsys, MODULE_NAME, input_string)[0].strip()
    expected = str([x for x in input_string if x not in ' e'])
    assert expected == output



def test_print_nothing_to_remove(capsys):
    __test_result(capsys, "hallo")
    __test_result(capsys, "123")


def test_print_remove_space(capsys):
    __test_result(capsys, "  o  ")
    __test_result(capsys, "  ")


def test_print_remove_e(capsys):
    __test_result(capsys, "hei")
    __test_result(capsys, "eee")


def test_print_remove_e_and_space(capsys):
    __test_result(capsys, "  e  ")
    __test_result(capsys, "ee ee")
    __test_result(capsys, "tere pere")
