#!/usr/bin/env python3
import sys


def problem_1(fname):
    
    with open(fname, "r") as f:
        return sum([int(x) for x in f.readlines()])


def problem_2(fname):
    frequencies = set([0])
    freq = 0
    with open(fname, "r") as f:
        lines = [int(x) for x in f.readlines()]
        while 1:
            for line in lines:
                freq += int(line)
                if freq in frequencies:
                    return freq
                frequencies.add(freq)


if __name__ == "__main__":
    print("Problem 1: {0}".format(problem_1(sys.argv[1])))
    print("Problem 2: {0}".format(problem_2(sys.argv[1])))
