#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument
    waits for a random delay between 0 and max_delay seconds
    and eventually returns it.
    """
    randValue = random.uniform(0, max_delay)
    await asyncio.sleep(randValue)
    return randValue
