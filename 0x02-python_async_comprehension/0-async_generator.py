#!/usr/bin/env python3
'''Module 0 task.
'''

import asyncio
import random

async def async_generator():
    '''Generate a sequence of random numbers.
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint() * 10
