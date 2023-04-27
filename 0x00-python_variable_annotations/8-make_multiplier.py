#!/usr/bin/env python3
"""function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier"""
# This is how you annotate a callable (function) value
# x: Callable[[int, float], float] = f
# def register(callback: Callable[[str], int]) -> None: ...
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multi(mult: float) :
        mult * mult
    return multi(multiplier)

print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))
