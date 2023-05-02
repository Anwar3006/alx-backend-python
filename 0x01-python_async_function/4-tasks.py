#!/usr/bin/env python3
"""
Importing coroutines to use in other coroutines
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency.
    """
    randList: list = []
    modList: list = []
    for i in range(n):
        randList.append(await task_wait_random(max_delay))
    modList = sorted(randList)
    return modList
