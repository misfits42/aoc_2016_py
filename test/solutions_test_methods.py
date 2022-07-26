"""
This module contains the test methods required to verify that the coded solvers
produce the correct solutions for AOC 2016.
"""


import unittest
from src.solutions import day_01, day_02, day_03, day_04, day_05, day_06, \
    day_07, day_08, day_09, day_10, day_11, day_12, day_13, day_14, day_15, \
    day_16, day_17, day_18, day_19, day_20, day_21, day_22, day_23, day_24, \
    day_25


class SolutionsTestMethods(unittest.TestCase):
    """
    Contains the test methods for each problem part in AOC 2016, checking valid
    answers.
    """

    def test_day_01_p1(self):
        """
        Solution test method for AOC 2016 Day 1 Part 1.
        """
        input_data = day_01.process_input_file()
        solution = day_01.solve_part1(input_data)
        self.assertEqual(332, solution)

    def test_day_01_p2(self):
        """
        Solution test method for AOC 2016 Day 1 Part 2.
        """
        input_data = day_01.process_input_file()
        solution = day_01.solve_part2(input_data)
        self.assertEqual(166, solution)

    def test_day_02_p1(self):
        """
        Solution test method for AOC 2016 Day 2 Part 1.
        """
        input_data = day_02.process_input_file()
        solution = day_02.solve_part1(input_data)
        self.assertEqual("78985", solution)

    def test_day_02_p2(self):
        """
        Solution test method for AOC 2016 Day 2 Part 2.
        """
        input_data = day_02.process_input_file()
        solution = day_02.solve_part2(input_data)
        self.assertEqual("57DD8", solution)

    def test_day_03_p1(self):
        """
        Solution test method for AOC 2016 Day 3 Part 1.
        """
        input_data = day_03.process_input_file()
        solution = day_03.solve_part1(input_data)
        self.assertEqual(862, solution)

    def test_day_03_p2(self):
        """
        Solution test method for AOC 2016 Day 3 Part 2.
        """
        input_data = day_03.process_input_file()
        solution = day_03.solve_part2(input_data)
        self.assertEqual(1577, solution)

    def test_day_04_p1(self):
        """
        Solution test method for AOC 2016 Day 4 Part 1.
        """
        input_data = day_04.process_input_file()
        solution = day_04.solve_part1(input_data)
        self.assertEqual(173787, solution)

    def test_day_04_p2(self):
        """
        Solution test method for AOC 2016 Day 4 Part 2.
        """
        input_data = day_04.process_input_file()
        solution = day_04.solve_part2(input_data)
        self.assertEqual(548, solution)

    def test_day_05_p1(self):
        """
        Solution test method for AOC 2016 Day 5 Part 1.
        """
        input_data = day_05.process_input_file()
        solution = day_05.solve_part1(input_data)
        self.assertEqual("f77a0e6e", solution)

    def test_day_05_p2(self):
        """
        Solution test method for AOC 2016 Day 5 Part 2.
        """
        input_data = day_05.process_input_file()
        solution = day_05.solve_part2(input_data)
        self.assertEqual("999828ec", solution)

    def test_day_06_p1(self):
        """
        Solution test method for AOC 2016 Day 6 Part 1.
        """
        input_data = day_06.process_input_file()
        solution = day_06.solve_part1(input_data)
        self.assertEqual("dzqckwsd", solution)

    def test_day_06_p2(self):
        """
        Solution test method for AOC 2016 Day 6 Part 2.
        """
        input_data = day_06.process_input_file()
        solution = day_06.solve_part2(input_data)
        self.assertEqual("lragovly", solution)

    def test_day_07_p1(self):
        """
        Solution test method for AOC 2016 Day 7 Part 1.
        """
        input_data = day_07.process_input_file()
        solution = day_07.solve_part1(input_data)
        self.assertEqual(115, solution)

    def test_day_07_p2(self):
        """
        Solution test method for AOC 2016 Day 7 Part 2.
        """
        input_data = day_07.process_input_file()
        solution = day_07.solve_part2(input_data)
        self.assertEqual(231, solution)

    def test_day_08_p1(self):
        """
        Solution test method for AOC 2016 Day 8 Part 1.
        """
        input_data = day_08.process_input_file()
        solution = day_08.solve_part1(input_data)
        self.assertEqual(123, solution)

    def test_day_08_p2(self):
        """
        Solution test method for AOC 2016 Day 8 Part 2.
        """
        input_data = day_08.process_input_file()
        solution = day_08.solve_part2(input_data)
        self.assertEqual("AFBUPZBJPS", solution)

    def test_day_09_p1(self):
        """
        Solution test method for AOC 2016 Day 9 Part 1.
        """
        input_data = day_09.process_input_file()
        solution = day_09.solve_part1(input_data)
        self.assertEqual(98135, solution)

    def test_day_09_p2(self):
        """
        Solution test method for AOC 2016 Day 9 Part 2.
        """
        input_data = day_09.process_input_file()
        solution = day_09.solve_part2(input_data)
        self.assertEqual(10964557606, solution)

    def test_day_10_p1(self):
        """
        Solution test method for AOC 2016 Day 10 Part 1.
        """
        input_data = day_10.process_input_file()
        solution = day_10.solve_part1(input_data)
        self.assertEqual(98, solution)

    def test_day_10_p2(self):
        """
        Solution test method for AOC 2016 Day 10 Part 2.
        """
        input_data = day_10.process_input_file()
        solution = day_10.solve_part2(input_data)
        self.assertEqual(4042, solution)

    def test_day_11_p1(self):
        """
        Solution test method for AOC 2016 Day 11 Part 1.
        """
        input_data = day_11.process_input_file()
        solution = day_11.solve_part1(input_data)
        self.assertEqual(47, solution)

    def test_day_11_p2(self):
        """
        Solution test method for AOC 2016 Day 11 Part 2.
        """
        input_data = day_11.process_input_file()
        solution = day_11.solve_part2(input_data)
        self.assertEqual(71, solution)

    def test_day_12_p1(self):
        """
        Solution test method for AOC 2016 Day 12 Part 1.
        """
        input_data = day_12.process_input_file()
        solution = day_12.solve_part1(input_data)
        self.assertEqual(318003, solution)

    def test_day_12_p2(self):
        """
        Solution test method for AOC 2016 Day 12 Part 2.
        """
        input_data = day_12.process_input_file()
        solution = day_12.solve_part2(input_data)
        self.assertEqual(9227657, solution)

    def test_day_13_p1(self):
        """
        Solution test method for AOC 2016 Day 13 Part 1.
        """
        input_data = day_13.process_input_file()
        solution = day_13.solve_part1(input_data)
        self.assertEqual(90, solution)

    def test_day_13_p2(self):
        """
        Solution test method for AOC 2016 Day 13 Part 2.
        """
        input_data = day_13.process_input_file()
        solution = day_13.solve_part2(input_data)
        self.assertEqual(135, solution)

    def test_day_14_p1(self):
        """
        Solution test method for AOC 2016 Day 14 Part 1.
        """
        input_data = day_14.process_input_file()
        solution = day_14.solve_part1(input_data)
        self.assertEqual(25427, solution)

    def test_day_14_p2(self):
        """
        Solution test method for AOC 2016 Day 14 Part 2.
        """
        input_data = day_14.process_input_file()
        solution = day_14.solve_part2(input_data)
        self.assertEqual(22045, solution)

    def test_day_15_p1(self):
        """
        Solution test method for AOC 2016 Day 15 Part 1.
        """
        input_data = day_15.process_input_file()
        solution = day_15.solve_part1(input_data)
        self.assertEqual(203660, solution)

    def test_day_15_p2(self):
        """
        Solution test method for AOC 2016 Day 15 Part 2.
        """
        input_data = day_15.process_input_file()
        solution = day_15.solve_part2(input_data)
        self.assertEqual(2408135, solution)

    def test_day_16_p1(self):
        """
        Solution test method for AOC 2016 Day 16 Part 1.
        """
        input_data = day_16.process_input_file()
        solution = day_16.solve_part1(input_data)
        self.assertEqual("00000100100001100", solution)

    def test_day_16_p2(self):
        """
        Solution test method for AOC 2016 Day 16 Part 2.
        """
        input_data = day_16.process_input_file()
        solution = day_16.solve_part2(input_data)
        self.assertEqual("00011010100010010", solution)

    def test_day_17_p1(self):
        """
        Solution test method for AOC 2016 Day 17 Part 1.
        """
        input_data = day_17.process_input_file()
        solution = day_17.solve_part1(input_data)
        self.assertEqual("RLDRUDRDDR", solution)

    def test_day_17_p2(self):
        """
        Solution test method for AOC 2016 Day 17 Part 2.
        """
        input_data = day_17.process_input_file()
        solution = day_17.solve_part2(input_data)
        self.assertEqual(498, solution)

    def test_day_18_p1(self):
        """
        Solution test method for AOC 2016 Day 18 Part 1.
        """
        input_data = day_18.process_input_file()
        solution = day_18.solve_part1(input_data)
        self.assertEqual(1974, solution)

    def test_day_18_p2(self):
        """
        Solution test method for AOC 2016 Day 18 Part 2.
        """
        input_data = day_18.process_input_file()
        solution = day_18.solve_part2(input_data)
        self.assertEqual(19991126, solution)

    def test_day_19_p1(self):
        """
        Solution test method for AOC 2016 Day 19 Part 1.
        """
        input_data = day_19.process_input_file()
        solution = day_19.solve_part1(input_data)
        self.assertEqual(1808357, solution)

    def test_day_19_p2(self):
        """
        Solution test method for AOC 2016 Day 19 Part 2.
        """
        input_data = day_19.process_input_file()
        solution = day_19.solve_part2(input_data)
        self.assertEqual(1407007, solution)

    def test_day_20_p1(self):
        """
        Solution test method for AOC 2016 Day 20 Part 1.
        """
        input_data = day_20.process_input_file()
        solution = day_20.solve_part1(input_data)
        self.assertEqual(22887907, solution)

    def test_day_20_p2(self):
        """
        Solution test method for AOC 2016 Day 20 Part 2.
        """
        input_data = day_20.process_input_file()
        solution = day_20.solve_part2(input_data)
        self.assertEqual(109, solution)

    def test_day_21_p1(self):
        """
        Solution test method for AOC 2016 Day 21 Part 1.
        """
        input_data = day_21.process_input_file()
        solution = day_21.solve_part1(input_data)
        self.assertEqual("gfdhebac", solution)

    def test_day_21_p2(self):
        """
        Solution test method for AOC 2016 Day 21 Part 2.
        """
        input_data = day_21.process_input_file()
        solution = day_21.solve_part2(input_data)
        self.assertEqual("dhaegfbc", solution)

    def test_day_22_p1(self):
        """
        Solution test method for AOC 2016 Day 22 Part 1.
        """
        input_data = day_22.process_input_file()
        solution = day_22.solve_part1(input_data)
        self.assertEqual(960, solution)

    def test_day_22_p2(self):
        """
        Solution test method for AOC 2016 Day 22 Part 2.
        """
        input_data = day_22.process_input_file()
        solution = day_22.solve_part2(input_data)
        self.assertEqual(225, solution)

    def test_day_23_p1(self):
        """
        Solution test method for AOC 2016 Day 23 Part 1.
        """
        input_data = day_23.process_input_file()
        solution = day_23.solve_part1(input_data)
        self.assertEqual(12330, solution)

    def test_day_23_p2(self):
        """
        Solution test method for AOC 2016 Day 23 Part 2.
        """
        input_data = day_23.process_input_file()
        solution = day_23.solve_part2(input_data)
        self.assertEqual(479008890, solution)

    def test_day_24_p1(self):
        """
        Solution test method for AOC 2016 Day 24 Part 1.
        """
        input_data = day_24.process_input_file()
        solution = day_24.solve_part1(input_data)
        self.assertEqual(442, solution)

    def test_day_24_p2(self):
        """
        Solution test method for AOC 2016 Day 24 Part 2.
        """
        input_data = day_24.process_input_file()
        solution = day_24.solve_part2(input_data)
        self.assertEqual(660, solution)

    def test_day_25_p1(self):
        """
        Solution test method for AOC 2016 Day 25 Part 1.
        """
        input_data = day_25.process_input_file()
        solution = day_25.solve_part1(input_data)
        self.assertEqual(182, solution)

    def test_day_25_p2(self):
        """
        Solution test method for AOC 2016 Day 25 Part 2.
        """
        input_data = day_25.process_input_file()
        solution = day_25.solve_part2(input_data)
        self.assertEqual(True, solution)


if __name__ == "__main__":
    unittest.main()
