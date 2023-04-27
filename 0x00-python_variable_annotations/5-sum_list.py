#!/usr/bin/env python3
from typing import List

def sum_list(input_list: List[float]) -> float:
    sum: float = 0
    for x in input_list:
        sum += x
    return sum
