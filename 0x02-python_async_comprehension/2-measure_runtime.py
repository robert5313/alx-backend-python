#!/usr/bin/env python3
'''Task 2's module.
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


<<<<<<< HEAD
def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
=======
async def measure_runtime() -> float:
    '''Executes async_comprehension 4 times and the execution time.
    '''
    new_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - new_time
>>>>>>> af09ea1f28df6de41242719804fe1bf08bd78c25
