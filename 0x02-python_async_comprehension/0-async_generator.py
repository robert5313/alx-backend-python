#!/usr/bin/env python3
'''Module 0 challenge task.
'''

import asyncio
import random

async def async_generator():
    '''Generate a random sequence of numbers.
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
