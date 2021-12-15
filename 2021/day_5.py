#!/usr/bin/env python3
import math
import sys


def problem_1(fname):
    cells = {}
    with open(fname, "r") as f:
        for line in f.readlines():
            x1, y1, x2, y2 = [int(x) for pair in line.strip().split(" -> ") for x in pair.split(",")]
            x_diff = x2 - x1
            y_diff = y2 - y1
            if x_diff != 0 and y_diff != 0:
                continue
            dx = x_diff // abs(x_diff) if x_diff else 0
            dy = y_diff // abs(y_diff) if y_diff else 0
            x = x1
            y = y1
            for i in range(max(abs(x_diff), abs(y_diff)) + 1):
                cell_location = "{0},{1}".format(x, y)
                cells[cell_location] = cells.get(cell_location, 0) + 1
                x += dx
                y += dy

    return len([item for item in cells.items() if item[1] > 1])


def problem_2(fname):
    cells = {}
    with open(fname, "r") as f:
        for line in f.readlines():
            x1, y1, x2, y2 = [int(x) for pair in line.strip().split(" -> ") for x in pair.split(",")]
            x_diff = x2 - x1
            y_diff = y2 - y1
            dx = x_diff // abs(x_diff) if x_diff else 0
            dy = y_diff // abs(y_diff) if y_diff else 0
            x = x1
            y = y1
            for i in range(max(abs(x_diff), abs(y_diff)) + 1):
                cell_location = "{0},{1}".format(x, y)
                cells[cell_location] = cells.get(cell_location, 0) + 1
                x += dx
                y += dy

    return len([item for item in cells.items() if item[1] > 1])


if __name__ == "__main__":
    print("Problem 1: {0}".format(problem_1(sys.argv[1])))
    print("Problem 2: {0}".format(problem_2(sys.argv[1])))
