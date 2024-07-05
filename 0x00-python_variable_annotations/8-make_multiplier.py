#!/usr/bin/env python3
'''
function that creates a multiplier function
to multiply a float by a given multiplier.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.'''
    return lambda x: x * multiplier
