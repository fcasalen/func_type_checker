from functools import wraps
from typing import get_args, get_origin, Callable, Union
from types import UnionType
import inspect
import sys

def enforce_types(strict:bool=True):
    """
    A decorator factory that enforces type hints at runtime. If the type hints are violated,
    a TypeError is raised.

    Args:
        strict (bool): If True, raises an error if a function argument does not have a type hint. Defaults to True.

    Returns:
        Callable: The decorator.
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            type_errors = []
            no_type_hints = []
            for name, value in bound_args.arguments.items():
                if name in sig.parameters:
                    parameter = sig.parameters[name]
                    expected_type = parameter.annotation
                    if parameter.kind in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD):
                        continue
                    print(name, expected_type)
                    if strict and expected_type is inspect.Parameter.empty:
                        no_type_hints.append(name)
                        continue
                    if expected_type is inspect.Parameter.empty:
                        continue
                    origin = get_origin(expected_type)
                    args_types = get_args(expected_type)
                    if origin in [Union, UnionType]:
                        if not isinstance(value, args_types):
                            type_errors.append(
                                f"{name} must be of type {'|'.join([f.__name__ for f in args_types])}, "
                                f"but got {type(value).__name__}"
                            )
                    else:
                        expected_type = type(None) if None else expected_type
                        if not isinstance(value, expected_type):
                            type_errors.append(
                                f"{name} must be of type {expected_type.__name__}, "
                                f"but got {type(value).__name__}"
                            )
            error_msg = ''
            if no_type_hints:
                error_msg += 'Missing type hints for argument(s): '
                error_msg += ", ".join(no_type_hints) + '\n\n'
            if type_errors:
                error_msg += 'Invalid Argument(s) type(s):\n- '
                error_msg += "\n- ".join(type_errors)
            if error_msg != '':
                raise TypeError(f'Type errors found in function {func.__name__} from module {func.__module__}:\n\n{error_msg.strip()}')
            return func(*args, **kwargs)
        return wrapper
    return decorator

def apply_enforce_types_to_module(module_name:str, exclude:list[str]=None, strict:bool=True):
    """Applies the enforce_types decorator to all functions in the given module.

    Args:
        module_name (str): the name of the module to apply the decorator to
        exclude (list[str], optional): a list of function names to exclude. Defaults to None.
        strict (bool, optional): If True, raises an error if a function argument does not have a type hint. Defaults to True.
    """
    exclude = exclude or []
    module = sys.modules[module_name]
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) and obj.__module__ == module_name and name not in exclude:
            setattr(module, name, enforce_types(strict)(obj))