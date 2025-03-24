from func_type_checker import apply_enforce_types_to_module

def any_func(a: int, b, *args, **kwargs) -> str:
    return str(a) + b + str(args) + str(kwargs)

apply_enforce_types_to_module(__name__)