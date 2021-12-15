#!/usr/bin/env python3
import sys


def problem_1(fname):
    terms = []
    with open(fname, "r") as f:
        terms = [int(x) for x in f.readline().strip().split(",")]

    pos = median(terms)

    distances = [abs(x - pos) for x in terms]

    return sum(distances)


def median(terms):
    return sorted(terms)[len(terms) // 2]


def problem_2(fname):
    terms = []
    with open(fname, "r") as f:
        terms = [int(x) for x in f.readline().strip().split(",")]

    pos = sum(terms) // len(terms)

    distances = [sum(range(abs(x - pos) + 1)) for x in terms]

    return sum(distances)


if __name__ == "__main__":
    print("Problem 1: {0}".format(problem_1(sys.argv[1])))
    print("Problem 2: {0}".format(problem_2(sys.argv[1])))
