#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day_4.py
@Time    :   2023/12/04 09:18:40
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

from advent_of_code_2023.timer import clock
from collections import deque
import re


def wining_numbers(line):
    line = line.strip()
    card, rest = line.split(":")
    card = re.findall(r"Card\s+(\d+)", card)[0]
    rest = rest.split("|")
    wining_numbers = set(map(int, filter(lambda x: len(x) != 0, rest[0].split(" "))))
    my_numbers = set(map(int, filter(lambda x: len(x) != 0, rest[1].split(" "))))
    matches = len(wining_numbers & my_numbers)
    return int(card), matches


@clock
def won_copies(lines):
    memo = dict(tuple(wining_numbers(line) for line in lines))
    total_cards = 0
    for or_card in range(1, len(lines) + 1):
        total_cards += memo[or_card] + 1
        won_cards = deque(list(range(or_card + 1, or_card + memo[or_card] + 1)))
        while len(won_cards) != 0:
            copy_card = won_cards.popleft()
            total_cards += memo[copy_card]
            won_cards.extend(
                list(range(copy_card + 1, copy_card + memo[copy_card] + 1))
            )
    return total_cards


def points_in_card(line):
    _, w = wining_numbers(line)
    return 2 ** (w - 1) if w > 1 else w


def solve_puzzle():
    input_file = "advent_of_code_2023/inputs/day_4.txt"

    with open(input_file, "r") as f:
        lines = f.readlines()
    total_points = sum([points_in_card(l) for l in lines])
    print(f"The result is of day four part one is:  {total_points}")

    part_two = won_copies(lines)
    print(f"The result is of day four part two is:  {part_two}")


if __name__ == "__main__":
    solve_puzzle()
