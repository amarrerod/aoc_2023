#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day_3.py
@Time    :   2023/12/03 07:44:38
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

import re
import functools
import operator


def get_gear_ratio(lines):
    schematic = [l.strip("\n") for l in lines]
    w, h = len(schematic[0]), len(schematic)

    gear_ratio = 0
    for y in range(h):
        for x in range(w):
            if schematic[y][x] == "*":
                gear = []
                for j in range(max(y - 1, 0), min(y + 2, h)):
                    s, e = x, x
                    while s > 0 and schematic[j][s - 1].isdigit():
                        s -= 1
                    while e < w - 1 and schematic[j][e + 1].isdigit():
                        e += 1

                    gear.extend(map(int, re.findall("\d+", schematic[j][s : e + 1])))
                if len(gear) == 2:
                    gear_ratio += gear[0] * gear[1]
    return gear_ratio


def get_adjacent_numbers(lines):
    schematic = [l.strip("\n") for l in lines]
    w, h = len(schematic[0]), len(schematic)
    p = {}
    for y in range(h):
        for x in range(w):
            if schematic[y][x] not in "0123456789.":
                for j in range(max(y - 1, 0), min(y + 2, h)):
                    s, e = x, x
                    while s > 0 and schematic[j][s - 1].isdigit():
                        s -= 1
                    while e < w - 1 and schematic[j][e + 1].isdigit():
                        e += 1
                    for m in re.finditer("\d+", schematic[j][s : e + 1]):
                        p[(s + m.start(), j)] = int(m.group())
    return sum(p.values())


def solve_puzzle():
    input_file = "advent_of_code_2023/inputs/day_3.txt"

    with open(input_file, "r") as f:
        lines = f.readlines()

    part_one = get_adjacent_numbers(lines)
    part_two = get_gear_ratio(lines)
    print(f"The result is of day two part one is:  {part_one}")
    print(f"The result is of day two part two is:  {part_two}")


if __name__ == "__main__":
    solve_puzzle()
