#!/usr/bin/env python3
import sys
import copy


def problem_1(fname):
    gestation = 6
    maturity = 2
    cycles = 5
    fish = []
    with open(fname, "r") as f:
        fish = [int(x) for x in f.readline().strip().split(",")]

    while cycles > 0:
        new_fish = []
        for i, days in enumerate(fish):
            if days == 0:
                fish[i] = gestation
                new_fish.append(gestation + maturity)
            else:
                fish[i] = days - 1
        fish.extend(new_fish)
        cycles -= 1

    return len(fish)


def problem_2(fname):
    gestation = 7
    maturity = 2
    cycles = 256
    offset_days = [0 for x in range(gestation + maturity)]

    with open(fname, "r") as f:
        fish = [int(x) for x in f.readline().strip().split(",")]

    for num in fish:
        offset_days[num] = offset_days[num] + 1

    for i in range(cycles):
        offset_days = offset_days[1:7] + [offset_days[0] + offset_days[7]] + [offset_days[8]] + [offset_days[0]]

    return sum(offset_days)


if __name__ == "__main__":
    print("Problem 1: {0}".format(problem_1(sys.argv[1])))
    print("Problem 2: {0}".format(problem_2(sys.argv[1])))
