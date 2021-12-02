#!/usr/bin/env python3
import sys


def problem_1(fname):
    horiz = 0
    depth = 0
    with open(fname, "r") as f:
        for instr in f.readlines():
            action, dist = instr.split(" ", 1)
            if action == "forward":
                horiz += int(dist)
            elif action == "up":
                depth -= int(dist)
            elif action == "down":
                depth += int(dist)
    return horiz * depth


def problem_2(fname):
    horiz = 0
    depth = 0
    aim = 0
    with open(fname, "r") as f:
        for instr in f.readlines():
            action, dist = instr.split(" ", 1)
            if action == "forward":
                horiz += int(dist)
                depth += aim * int(dist)
            elif action == "up":
                aim -= int(dist)
            elif action == "down":
                aim += int(dist)
    return horiz * depth


if __name__ == "__main__":
    print(problem_2(sys.argv[1]))
