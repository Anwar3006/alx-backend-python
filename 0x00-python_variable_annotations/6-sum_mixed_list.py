#!/usr/bin/env python3
from typing import Union

def sum_mixed_list(input_list: 'list[Union[float, int]]') -> float:
    """
    a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.
    """
    sum: float = 0
    for x in input_list:
        sum += x
    return sum
