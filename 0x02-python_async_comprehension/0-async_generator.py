#!/usr/bin/env python3
""" Task 0's Module documentation """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Function generates a sequence of 10 numbers."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
