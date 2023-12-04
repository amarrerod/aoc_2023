#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   timer.py
@Time    :   2023/12/04 14:55:44
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

import time

import time
import functools


def clock(func, include_args=False):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__

        print(f"[{elapsed:0.8f}s] {name} -> {result!r}")
        return result

    return clocked
