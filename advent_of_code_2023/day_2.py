#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day_2.py
@Time    :   2023/12/02 07:56:56
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2023, Alejandro Marrero
@Desc    :   None
"""


import re
import operator
import functools

regex = r"(?:\s*(\d+)\s(blue)|(\d+)\s(red)|(\d+)\s(green))"


def fewer_cubes(line):
    """Counts the minimum amount of cubes of each color
    required to play the game

    Args:
        line (str): Game

    Returns:
        int: Power of the cubes.
        The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
    """
    line_splitted = [l.strip() for l in line.split(";")]
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for l in line_splitted:
        colors = [tuple(filter(bool, x)) for x in re.findall(regex, l)]
        for n, color in colors:
            n = int(n)
            if min_cubes[color] < n:
                min_cubes[color] = n
    # Multiply the min cubes for each color
    power = functools.reduce(operator.mul, min_cubes.values(), 1)
    return power


def feasible_game(bag, game):
    for bag_c, game_c in zip(bag, game):
        if game_c > bag_c:
            return False
    return True


def valid_games(line, bag_configuration):
    # Get the game ID
    game_id = int(re.findall(r"Game\s(\d+):", line)[0])
    line_splitted = [l.strip() for l in line.split(";")]
    for l in line_splitted:
        game_counter = {"red": 0, "green": 0, "blue": 0}
        colors = [tuple(filter(bool, x)) for x in re.findall(regex, l)]
        for n, color in colors:
            game_counter[color] += int(n)

        if not feasible_game(bag_configuration.values(), game_counter.values()):
            return 0
    return game_id


def solve_puzzle():
    input_file = "advent_of_code_2023/inputs/day_2.txt"

    with open(input_file, "r") as f:
        lines = f.readlines()

    bag_configuration = {"red": 12, "green": 13, "blue": 14}
    part_one = sum([valid_games(l, bag_configuration) for l in lines])
    part_two = sum([fewer_cubes(l) for l in lines])
    print(f"The result is of day two part one is:  {part_one}")
    print(f"The result is of day two part two is:  {part_two}")


if __name__ == "__main__":
    solve_puzzle()
