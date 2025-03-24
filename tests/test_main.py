from func_type_checker import enforce_types

import pytest
import re

def test_enforce_types():
    @enforce_types()
    def any_func(a: int, b: str) -> str:
        return str(a) + b
    assert any_func(1, '2') == '12'
    with pytest.raises(TypeError, match=re.escape(
        "Type errors found in function any_func from module tests.test_main:\n\n"
        "Invalid Argument(s) type(s):\n"
        "- a must be of type int, but got str\n"
        "- b must be of type str, but got int"
    )):
        any_func('1', 2)
    @enforce_types()
    def any_func(a: int, b) -> str:
        return str(a) + b
    with pytest.raises(TypeError, match=re.escape("Missing type hints for argument(s): b")):
        any_func(1, '2')
    @enforce_types(strict=False)
    def any_func(a: int, b) -> str:
        return str(a) + b
    assert any_func(1, '2') == '12'