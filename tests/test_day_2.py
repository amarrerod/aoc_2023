#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_day_2.py
@Time    :   2023/12/02 09:05:36
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

import pytest

from advent_of_code_2023.day_2 import valid_games, fewer_cubes


def test_day_2_part_one():
    input = "advent_of_code_2023/examples/day_2.txt"
    with open(input, "r") as f:
        lines = f.readlines()

    expected = 8
    bag_configuration = {"red": 12, "green": 13, "blue": 14}

    assert sum([valid_games(l, bag_configuration) for l in lines]) == expected


def test_day_2_part_two():
    input = "advent_of_code_2023/examples/day_2.txt"
    with open(input, "r") as f:
        lines = f.readlines()

    expected = 2286
    assert sum([fewer_cubes(l) for l in lines]) == expected
