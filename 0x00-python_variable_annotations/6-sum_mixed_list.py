#!/usr/bin/env python3
"""
Mixed Type Addition Function
"""
from typing import Union


def sum_mixed_list(mxd_list: 'list[Union[float, int]]') -> float:
    """
    a type-annotated function sum_mixed_list which takes a
    list mxd_lst of integers and floats and returns their sum as a float.
    """
    sum: float = 0
    for x in mxd_list:
        sum += x
    return sum
