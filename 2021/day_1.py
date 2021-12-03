#!/usr/bin/env python3
import sys


def problem_1(fname):
    greater_than_prior = 0
    prior = None
    with open(fname, "r") as f:
        for depth in f.readlines():
            if prior is None:
                prior = int(depth)
                continue
            if int(depth) > prior:
                greater_than_prior += 1
            prior = int(depth)
    return greater_than_prior


def problem_2(fname):
    greater_than_prior = 0
    prior = None
    windowed_sums = []
    with open(fname, "r") as f:
        depths = [int(x) for x in f.readlines()]
        for i in range(len(depths) - 2):
            windowed_sums.append(sum(depths[i:i + 3]))
        for depth in windowed_sums:
            if prior is None:
                prior = depth
                continue
            if depth > prior:
                greater_than_prior += 1
            prior = depth
    return greater_than_prior


if __name__ == "__main__":
    print(problem_2(sys.argv[1]))
