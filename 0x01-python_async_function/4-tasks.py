#!/usr/bin/env python3
""" Task 4's Module documentation """

import asyncio
import random
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times"""

    listDelays = []
    for _ in range(n):
        listDelays.append(task_wait_random(max_delay))
    return sorted(await asyncio.gather(*listDelays))
