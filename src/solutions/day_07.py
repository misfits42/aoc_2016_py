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
    valid_count = 0
    for address in input_data:
        if check_tls_support(address):
            valid_count += 1
    return valid_count


def solve_part2(input_data):
    """
    Counts the number of the "IPv7" addresses in the input data that support
    Super-Secret Listening (SSL), by checking which addresses contain an
    Area-Broadcast Accessor (ABA) anywhere in the supernet sequences and a
    Byte Allocation Block (BAB) within the hypernet sequence.
    """
    regex_aba_left = re.compile(
        r"[a-z]*([a-z])([a-z])\1[a-z]*\[[a-z]*\2\1\2[a-z]*\][a-z]*")
    regex_aba_right = re.compile(
        r"[a-z]*\[[a-z]*([a-z])([a-z])\1[a-z]*\][a-z]*\2\1\2[a-z]*")
    valid_count = 0
    for address in input_data:
        ()
        # match_left = regex_aba_left.search(address)
        # match_right = regex_aba_right.search(address)
        # if match_left and match_left.group(1) != match_left.group(2):
        #     print(
        #         f"match left // {match_left.group(1)}{match_left.group(2)}{match_left.group(1)}")
        #     valid_count += 1
        # elif match_right and match_right.group(1) != match_right.group(2):
        #     print(
        #         f"match right // {match_right.group(1)}{match_right.group(2)}{match_right.group(1)}")
        #     valid_count += 1
        # else:
        #     print("no match")
    return valid_count


def check_tls_support(address):
    """
    Checks if the given "IPv7" address supports Transport-Layer Snooping (TLS),
    meaning it contains at least one Autonomous Bridge Bypass Annotation (ABBA)
    in a supernet sequence and none in a hypernet sequence
    """
    # Check for incorrectly formatted address
    regex_correct_format = re.compile(r"[a-z]+\[[a-z]+\][a-z]+")
    if regex_correct_format.search(address) is None:
        return False
    # Split out the left supernet, right supernet and hypernet sequences
    regex_supernet = r"([a-z]+\[|\][a-z]+\[|\][a-z]+)"
    regex_hypernet = r"\[([a-z]+)\]"
    supernets = [re.sub(r"\[|\]", "", chars)
                 for chars in re.findall(regex_supernet, address)]
    hypernets = re.findall(regex_hypernet, address)
    # Check for any ABBAs in the hypernet sequence
    for hypernet in hypernets:
        for i in range(0, len(hypernet) - 3):
            slot = hypernet[i:i+4]
            if slot[0] == slot[3] and slot[1] == slot[2] and slot[0] != slot[1]:
                return False
    # Check left supernet for ABBAs
    for supernet in supernets:
        for i in range(0, len(supernet) - 3):
            slot = supernet[i:i+4]
            if slot[0] == slot[3] and slot[1] == slot[2] and slot[0] != slot[1]:
                return True
    return False
