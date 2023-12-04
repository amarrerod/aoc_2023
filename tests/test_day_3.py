#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_day_3.py
@Time    :   2023/12/04 09:15:07
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

import pytest

from advent_of_code_2023.day_3 import get_adjacent_numbers, get_gear_ratio


def test_day_3_part_one():
    input = "advent_of_code_2023/examples/day_3.txt"
    with open(input, "r") as f:
        lines = f.readlines()

    expected = 4361

    assert get_adjacent_numbers(lines) == expected


def test_day_3_part_two():
    input = "advent_of_code_2023/examples/day_3.txt"
    with open(input, "r") as f:
        lines = f.readlines()

    expected = 467835
    assert get_gear_ratio(lines) == expected
