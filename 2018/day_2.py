#!/usr/bin/env python3
import sys


def problem_1(fname):
    doubles, triples = 0, 0
    with open(fname, "r") as f:
        for line in f.readlines():
            letters = {}
            for letter in line:
                letters[letter] = letters.get(letter, 0) + 1

            counts = letters.values()
            if 2 in counts:
                doubles += 1
            if 3 in counts:
                triples += 1

    return  doubles * triples


def problem_2(fname):
    with open(fname, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            for j in range(i, len(lines)):
                if i != j:
                    dist, indices = string_distance(lines[i], lines[j])
                    if dist == 1:
                        if indices[0] == len(lines[i]) - 1:
                            return lines[i][:-1]
                        return lines[i][:indices[0]] + lines[i][indices[0] + 1:]
    return "N/A"


def string_distance(str1, str2):
    differing_indices = [x for x in range(len(str1)) if str1[x] != str2[x]]
    return len(differing_indices), differing_indices


if __name__ == "__main__":
    print("Problem 1: {0}".format(problem_1(sys.argv[1])))
    print("Problem 2: {0}".format(problem_2(sys.argv[1])))
