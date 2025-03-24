from .mock_module_strict import any_func

import pytest
import re

def test_any_func():
    with pytest.raises(TypeError, match=re.escape(
        "Type errors found in function any_func from module tests.mock_module_strict:\n\n"
        "Missing type hints for argument(s): b\n\n"
        "Invalid Argument(s) type(s):\n"
        "- a must be of type int, but got str"
    )):
        any_func('1', 2)