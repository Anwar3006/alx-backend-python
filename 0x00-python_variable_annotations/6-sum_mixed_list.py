#!/usr/bin/env python3
from typing import Union

def sum_mixed_list(input_list: 'list[Union[float, int]]') -> float:
    sum: float = 0
    for x in input_list:
        sum += x
    return sum

mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans)