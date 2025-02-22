#!/usr/bin/env python3
"""augment code with the correct duck-typed annotations."""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """First element of the list .if the list is empty None."""
    if lst:
        return lst[0]
    else:
        return None
