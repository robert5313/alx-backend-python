#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
from typing import List
import random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''Executes wait_random n times.
    '''
    wait_times = []
    for i in range(n):
        wait_time = random.random() * max_delay
        await asyncio.sleep(wait_time)
        wait_times.append(wait_time)
    return sorted(wait_times)
