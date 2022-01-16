#!/usr/bin/env python3
import sys


def problem_1(fname):
    
    with open(fname, "r") as f:
        polymer = f.read().strip()

    return len(react_polymer(polymer))


def problem_2(fname):
    
    with open(fname, "r") as f:
        polymer = f.read().strip()

    min_polymer_length = None
    elements = list(set([x.lower() for x in set(polymer)]))
    for el in elements:
        reformed_polymer = polymer.translate({ord(c): None for c in [el.lower(), el.upper()]})
        minimised_polymer = react_polymer(reformed_polymer)
        if min_polymer_length is None or len(minimised_polymer) < min_polymer_length:
            min_polymer_length = len(minimised_polymer)
    return min_polymer_length


def elements_react(e1, e2):
    return (e1.lower() == e2.lower()) and (e1 != e2)


def react_polymer(polymer):
    i = 1
    while i < len(polymer):
        if i == 0:
            i += 1
            continue
        if elements_react(polymer[i], polymer[i - 1]):
            polymer = polymer[:i - 1] + polymer[i + 1:]
            i -= 1
        else:
            i += 1

    return polymer


if __name__ == "__main__":
    print("Problem 1: {0}".format(problem_1(sys.argv[1])))
    print("Problem 2: {0}".format(problem_2(sys.argv[1])))
