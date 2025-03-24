# func_type_checker
project ensure that the function is called with the correct type of arguments

```python
from func_type_checker import enforces_types

# This function will raise a TypeError if a or b are not integers or if any argument is not type annotated
@enforces_types
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)  # returns 3
add(1.0, 2)  # raises TypeError

# This function will raise a TypeError if a is not integer
@enforces_types(strict=False)
def add(a: int, b) -> int:
    return a + b

add(1, 2)  # returns 3
add(1.0, 2)  # raises TypeError

# to apply enforces_types in all function of a module with strict = True and not apply to function func1
from func_type_checker import apply_enforce_types_to_module

apply_enforce_types_to_module(module_name=__name__, exclude=['func1'],strict=True) #insert this line at the end of the module
```
