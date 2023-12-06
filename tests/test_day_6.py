#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_day_6.py
@Time    :   2023/12/06 08:37:52
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""


import pytest
from advent_of_code_2023.day_6 import get_times_and_distances, ways_to_beat_race
import operator
import functools


def test_day_6_part_one():
    expected = 288
    input_file = "advent_of_code_2023/examples/day_6.txt"
    with open(input_file, "r") as f:
        lines = f.readlines()

    times, distances = get_times_and_distances(lines)
    result = functools.reduce(
        operator.mul,
        [ways_to_beat_race(t, d) for t, d in zip(times, distances)],
        1,
    )
    assert result == expected


def test_day_6_part_two():
    expected = 71503
    input_file = "advent_of_code_2023/examples/day_6.txt"
    with open(input_file, "r") as f:
        lines = f.readlines()

    time, distance = get_times_and_distances(lines, True)
    result = ways_to_beat_race(time, distance)

    assert result == expected
