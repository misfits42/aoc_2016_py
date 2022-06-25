"""
Solutions for AOC 2016 Day 2.
"""


from src.utils.cartography import Location2D



def process_input_file():
    """
    Processes the AOC 2016 Day 2 input file into the format required by the
    solver functions. Returned value is a list containing the strings listed
    in the input file.
    """
    with open("./inputs/day_02.txt", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()
                if len(line.strip()) > 0]


def solve_part1(input_data):
    """
    Follows the instructions listed in the input data to determine the code to
    the Easter Bunny HQ bathroom door.
    """
    door_code = []
    code_grid = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    location = Location2D(1, 1) # Start at the "5" button
    for instruction in input_data:
        for char in instruction:
            match char:
                case "U":
                    if location.loc_y > 0:
                        location = Location2D(location.loc_x, location.loc_y - 1)
                case "L":
                    if location.loc_x > 0:
                        location = Location2D(location.loc_x - 1, location.loc_y)
                case "R":
                    if location.loc_x < len(code_grid[location.loc_y]) - 1:
                        location = Location2D(location.loc_x + 1, location.loc_y)
                case "D":
                    if location.loc_y < len(code_grid) - 1:
                        location = Location2D(location.loc_x, location.loc_y + 1)
        door_code.append(code_grid[location.loc_y][location.loc_x])
    return "".join(door_code)


def solve_part2(input_data):
    return -1
