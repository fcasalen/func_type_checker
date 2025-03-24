from .mock_module import any_func

import pytest
import re

def test_any_func():
    assert any_func(1, '2') == '12(){}'
    with pytest.raises(TypeError, match=re.escape(
        "Type errors found in function any_func from module tests.mock_module:\n\n"
        "Invalid Argument(s) type(s):\n"
        "- a must be of type int, but got str"
    )):
        any_func('1', 2)