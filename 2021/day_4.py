#!/usr/bin/env python3
import sys


def problem_1(fname):
    boards = []
    with open(fname, "r") as f:
        lines = f.readlines()
        numbers = [int(x) for x in lines.pop(0).split(",")]
        for i in range(len(lines) // 6):
            rows = [[int(x.strip()) for x in row.strip().split()] for row in lines[(6 * i) + 1 : (6 * i) + 6]]
            boards.append(Board(rows))

    for i, num in enumerate(numbers):
        coord = boards[0].call_number(num)

        for j, board in enumerate(boards):
            coord = board.call_number(num)
            if coord and board.is_board_complete(*coord):
                return board.sum_uncalled() * num

    return "N/A"


def problem_2(fname):
    boards = []
    with open(fname, "r") as f:
        lines = f.readlines()
        numbers = [int(x) for x in lines.pop(0).split(",")]
        for i in range(len(lines) // 6):
            rows = [[int(x.strip()) for x in row.strip().split()] for row in lines[(6 * i) + 1 : (6 * i) + 6]]
            boards.append(Board(rows))

    for i, num in enumerate(numbers):
        coord = boards[0].call_number(num)

        for j, board in list(enumerate(boards))[::-1]:
            coord = board.call_number(num)
            if coord and board.is_board_complete(*coord):
                if len(boards) == 1:
                    return board.sum_uncalled() * num
                boards.pop(j)

    return "N/A"


class Board(object):
    def __init__(self, rows):
        self._places = [[False for i in range(5)] for j in range(5)]
        self._card = rows
        self._coordinates = {}
        for y, row in enumerate(rows):
            for x, value in enumerate(row):
                self._coordinates[value] = (x, y)


    def call_number(self, num):
        coord = self._coordinates.get(num, None)
        if coord is not None:
            self._places[coord[1]][coord[0]] = True
        return coord


    def is_board_complete(self, x, y):
        return (False not in self._places[y]) or (False not in [row[x] for row in self._places])


    def sum_uncalled(self):
        total = 0
        for y, row in enumerate(self._places):
            for x, called in enumerate(row):
                if called is False:
                    total += self._card[y][x]
        return total


    def print_board(self):
        for y, row in enumerate(self._places):
            for x, called in enumerate(row):
                print(" [{0}] ".format(self._card[y][x]) if called else " {0} ".format(self._card[y][x]), end="")
            print()


if __name__ == "__main__":
    print("Problem 1: {0}".format(problem_1(sys.argv[1])))
    print("Problem 2: {0}".format(problem_2(sys.argv[1])))
