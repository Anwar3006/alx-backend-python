#!/usr/bin/env python3
"""
Coroutine to measure runtime of other coroutines
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.
    """
    startTime = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - startTime) / n
