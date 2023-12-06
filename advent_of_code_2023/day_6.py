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
import operator
import functools
import re


def get_times_and_distances(lines, second_part: bool = False):
    lines = [l.strip() for l in lines]
    times = tuple(re.findall("(\d+)", lines[0]))
    distances = tuple(re.findall("(\d+)", lines[1]))
    if second_part:
        time = int("".join(times))
        dist = int("".join(distances))
        return time, dist
    else:
        times = tuple(map(int, times))
        distances = tuple(map(int, distances))
    return times, distances


def ways_to_beat_race(time, best_distance):
    n_ways = 0
    for i in range(1, time - 1):
        dist = i * (time - i)
        if dist > best_distance:
            n_ways += 1
    return n_ways


def solve_puzzle():
    input_file = "advent_of_code_2023/inputs/day_6.txt"

    with open(input_file, "r") as f:
        lines = f.readlines()

    times, distances = get_times_and_distances(lines)
    solution_part_one = functools.reduce(
        operator.mul,
        [ways_to_beat_race(t, d) for t, d in zip(times, distances)],
        1,
    )
    print(f"The solution of Day 6 part one is: {solution_part_one}")
    time, distance = get_times_and_distances(lines, True)
    solution_part_two = ways_to_beat_race(time, distance)
    print(f"The solution of Day 6 part two is: {solution_part_two}")


if __name__ == "__main__":
    solve_puzzle()
