#!/usr/bin/env python3
'''Module task 1.
'''
<<<<<<< HEAD
import asyncio
=======
>>>>>>> af09ea1f28df6de41242719804fe1bf08bd78c25
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


<<<<<<< HEAD
async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
=======
async def async_comprehension() -> List[float]:
    '''Creates a list of 10 numbers the generator.
    '''
    return [num async for num in async_generator()]
>>>>>>> af09ea1f28df6de41242719804fe1bf08bd78c25
