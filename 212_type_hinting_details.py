# %% Setup
from typing import Any, Literal


class DemoType:
    pass


# %% assign type hints to variables:

my_integer: int = 123

my_string: str = "abc"

my_whatever: DemoType = ...

# %% assign type hints to variables for complex types:
from typing import Dict, List, Tuple, Union

my_list_a: List = ...
my_list_b: List[int] = ...
my_list_c: List[Union[int, float]] = ...

my_list_d: List[Union[int, float]] = [1, 2, 3, 3.23, 'a']

my_dict_a: Dict = ...
my_dict_b: Dict[str, Any] = ...

my_dict_c: Dict[str, Any] = {'a': 123,
                             'b': 456,
                             3: 'abc'}

# %% casting values even if not sensible

from typing import cast

my_int: int = cast(int, "abc")

# %% tuple are special cases

my_tuple: Tuple = (123, 'abc', '123')

my_tuple_b: Tuple[int, str, str] = (123, 'abc', '123')

my_unkown_object = 'dummy'

# %%  Type hints with functions:
from typing import Sequence, NoReturn, Mapping, Optional, Literal

def do_something(my_input: Sequence[int],
                 my_other_input: Mapping[int, str]) -> NoReturn:
    ...

def get_something(my_input: int) -> Optional[int]:
    if my_input:
        return my_input
    else:
        return None

def do_stuff(my_input: Sequence[int],
             which_mode: Literal['all', 'nothing']) -> NoReturn:
    ...
