#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_day_4.py
@Time    :   2023/12/04 10:31:11
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

import pytest

from advent_of_code_2023.day_4 import points_in_card, won_copies


def test_day_4_part_one():
    input = "advent_of_code_2023/examples/day_4.txt"
    with open(input, "r") as f:
        lines = f.readlines()

    expected = 13

    assert sum([points_in_card(l) for l in lines]) == expected


def test_day_3_part_two():
    input = "advent_of_code_2023/examples/day_4.txt"
    with open(input, "r") as f:
        lines = f.readlines()

    expected = 30
    assert won_copies(lines) == expected
