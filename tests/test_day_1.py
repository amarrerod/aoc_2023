#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_advent_of_code_2023.py
@Time    :   2023/12/01 11:34:00
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""


import pytest

from advent_of_code_2023.day_1 import get_number, get_number_2


def test_day_1_part_one():
    input = "advent_of_code_2023/examples/day_1_part_1.txt"
    with open(input, "r") as f:
        lines = f.readlines()

    expected = 142
    assert sum([get_number(l) for l in lines]) == expected


def test_day_1_part_two():
    input = "advent_of_code_2023/examples/day_1_part_2.txt"
    with open(input, "r") as f:
        lines = f.readlines()

    expected = 281
    assert sum([get_number_2(l) for l in lines]) == expected
