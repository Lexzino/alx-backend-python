#!/usr/bin/env python3
'''Task 0's module documentation.'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for random number of seconds.'''
    
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)

    return wait_time