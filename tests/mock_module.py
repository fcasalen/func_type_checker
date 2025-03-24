from func_type_checker import apply_enforce_types_to_module

def any_func(a: int, b) -> str:
    return str(a) + b

apply_enforce_types_to_module(module_name=__name__, strict=False)