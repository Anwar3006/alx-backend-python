#!/usr/bin/env python3
"""
Importing coroutines to use in other coroutines
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency.
    """
    randList: list = []
    modList: list = []
    for i in range(n):
        randList.append(await wait_random(max_delay))
    modList = sorted(randList)
    return modList
