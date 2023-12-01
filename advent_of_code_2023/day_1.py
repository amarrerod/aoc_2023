#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day_1.py
@Time    :   2023/12/01 09:54:24
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""

import re

valid_numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


regex = r"(?=(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(\d))"


def cast_number(number: str):
    """Returns the digit representation of a written number

    Args:
        number (str): Number represented in letters.

    Returns:
        str: A string with the digit representation of the number
    """
    return valid_numbers[number] if len(number) > 1 else number


def get_number_2(line):
    numbers = [list(filter(bool, x)) for x in re.findall(regex, line)]
    digits = [cast_number(numbers[0][0]), cast_number(numbers[-1][0])]
    n = int("".join(digits))
    return n


def get_number(line):
    chars = list(filter(lambda x: x.isdigit(), line))
    return int(f"{chars[0]}{chars[-1]}")


def solve_puzzle():
    input_file = "advent_of_code_2023/inputs/day_1.txt"

    with open(input_file, "r") as f:
        lines = f.readlines()
    part_one = sum([get_number(l) for l in lines])
    part_two = sum([get_number_2(l) for l in lines])

    print(f"The result is of day one part one is:  {part_one}")
    print(f"The result is of day one part two is:  {part_two}")


if __name__ == "__main__":
    solve_puzzle()
