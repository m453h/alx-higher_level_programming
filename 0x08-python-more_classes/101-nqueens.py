#!/usr/bin/python3
"""Defines a NQueens solution class."""

import sys


class NQueens:

    def __init__(self):
        """Initialize a new NQueens solution instance"""

        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)
        try:
            self.n = int(sys.argv[1])
        except ValueError:
            print("N must be a number")
            sys.exit(1)

        if self.n < 4:
            print("N must be at least 4")
            sys.exit(1)

        self.solutions = []

    def run(self):
        """Runs the NQueens solution"""
        x.solve([], [], [])
        x.display_solution()

    def solve(self, queens, diff_of_xy, sum_of_xy):
        """Solves the NQueens solution

        Args:
            queens (list): the positions of the queens on the board
            diff_of_xy (list): the differences of the positions of the queens
            sum_of_xy (list): the sums of the positions of the queens
        """
        if len(queens) == self.n:
            self.solutions.append(list(queens))
            return

        for i in range(self.n):
            if i in queens or (len(queens) - i) in diff_of_xy\
             or (len(queens) + i) in sum_of_xy:
                continue

            self.solve(
                queens + [i],
                diff_of_xy + [len(queens) - i],
                sum_of_xy + [len(queens) + i])

    def display_solution(self):
        """Displays the NQueens solution"""
        for soln in self.solutions:
            print([[i, soln[i]] for i in range(self.n)])


if __name__ == "__main__":
    x = NQueens()
    x.run()
