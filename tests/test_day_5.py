#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_day_5.py
@Time    :   2023/12/05 10:39:22
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""


import pytest
import sys
from advent_of_code_2023.day_5 import get_seeds_conversions, convert_seed_to_location


@pytest.fixture
def seeds_conversions():
    input = "advent_of_code_2023/examples/day_5.txt"
    with open(input, "r") as f:
        lines = f.readlines()

    seeds, conversions = get_seeds_conversions(lines)
    return (seeds, conversions)


def test_day_5_part_one(seeds_conversions):
    expected = 35
    seeds = seeds_conversions[0]
    conversions = seeds_conversions[1]
    result = min([convert_seed_to_location(s, conversions) for s in seeds])

    assert result == expected


def test_day_5_part_two(seeds_conversions):
    expected = 46
    seeds = seeds_conversions[0]
    conversions = seeds_conversions[1]
    seeds_ranges = tuple(seeds[i : i + 2] for i in range(0, len(seeds), 2))

    min_location = sys.maxsize
    for r in seeds_ranges:
        for seed in range(r[0], r[0] + r[1]):
            loc = convert_seed_to_location(seed, conversions)
            if loc < min_location:
                min_location = loc

    assert min_location == expected
