#!/usr/bin/env python3
'''Task 2's module.
'''
import asyncio
import time
from typing import List
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''Executes wait_random n times.
    '''
    wait_times = []
    for i in range(n):
        wait_time = await wait_random(max_delay)
        wait_times.append(wait_time)
    return sorted(wait_times)


def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
