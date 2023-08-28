#!/usr/bin/env python3
<<<<<<< HEAD
'''Module 0 task.
=======
'''Task 0 module.
>>>>>>> af09ea1f28df6de41242719804fe1bf08bd78c25
'''
import asyncio
import random
from typing import Generator


<<<<<<< HEAD
async def async_generator():
    '''Generate a sequence of random numbers.
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint() * 10
=======
async def async_generator() -> Generator[float, None, None]:
    '''Generates a random sequence of 10 numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
>>>>>>> af09ea1f28df6de41242719804fe1bf08bd78c25
