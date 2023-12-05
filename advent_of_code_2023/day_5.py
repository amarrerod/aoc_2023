#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day_5.py
@Time    :   2023/12/05 09:21:27
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""


from advent_of_code_2023.timer import clock
from collections import deque
import re

categories = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]

all_categories = [
    f"{categories[i]}-to-{categories[i + 1]} map:" for i in range(len(categories) - 1)
]


def cast_conversions(conversions):
    conversions = tuple(int(x) for c in conversions for x in c.split(" "))
    t = tuple(conversions[i : i + 3] for i in range(0, len(conversions), 3))
    return t


def convert_seed_to_location(seed, conversions):
    location = seed
    for _, conversions in conversions.items():
        for (source, r), dest in conversions.items():
            if location >= source and location <= source + r:
                location = ((location - source) / ((source + r) - source)) * (
                    (dest + r) - (dest)
                ) + dest
                break
    return location


def get_seeds_conversions(lines):
    lines = list(filter(bool, [l.strip() for l in lines]))
    seeds = list(map(int, re.findall("(\d+)", lines[0])))
    conversions = {k: {} for k in all_categories}
    for i in range(len(all_categories)):
        information = []
        if i == len(all_categories) - 1:
            information = lines[lines.index(all_categories[i]) + 1 :]

        else:
            information = lines[
                lines.index(all_categories[i]) + 1 : lines.index(all_categories[i + 1])
            ]

        for dest, source, r in cast_conversions(information):
            conversions[all_categories[i]][(source, r)] = dest
    return seeds, conversions


def solve_puzzle():
    input_file = "advent_of_code_2023/inputs/day_5.txt"

    with open(input_file, "r") as f:
        lines = f.readlines()

    seeds, conversions = get_seeds_conversions(lines)
    solution_part_one = min([convert_seed_to_location(s, conversions) for s in seeds])

    print(f"The solution of day 5 part one is: {solution_part_one}")


if __name__ == "__main__":
    solve_puzzle()
