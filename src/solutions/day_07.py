"""
Solutions for AOC 2016 Day 7.
"""


import re


def process_input_file():
    """
    Processes the AOC 2016 Day 7 input file into the format required by the
    solver functions. Returned value is a list containing the "IPv7" addresses
    included in the input file.
    """
    with open("./input/day_07.txt", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()
                if len(line.strip()) > 0]


def solve_part1(input_data):
    """
    Counts the number of the "IPv7" addresses in the input data that support
    Transport-Layer Snooping (TLS), by checking how many contain an Autonomous
    Bridge Bypass Annotation (ABBA) outside of the square braces and not within.
    """
    regex_abba_square_bracket = re.compile(
        r"[a-z]*\[[a-z]*([a-z])([a-z])\2\1[a-z]*\][a-z]*")
    regex_abba = re.compile(r"([a-z])([a-z])\2\1")
    valid_count = 0
    for address in input_data:
        match_abba_square_bracket = regex_abba_square_bracket.search(address)
        if match_abba_square_bracket and \
                match_abba_square_bracket.group(1) != match_abba_square_bracket.group(2):
            continue
        match_abba = regex_abba.search(address)
        if match_abba and match_abba.group(1) != match_abba.group(2):
            valid_count += 1
    return valid_count


def solve_part2(input_data):
    return -1
