#!/usr/bin/env python3
import sys
import functools


def problem_1(fname):
    gamma, epsilon = "", ""
    with open(fname, "r") as f:
        lines = f.readlines()
        for i in range(len(lines[0]) - 1):
            most_freq = most_freq_char(lines, i)
            gamma += most_freq
            epsilon += "1" if most_freq == "0" else "0"
    print(gamma, epsilon)
    return gamma, epsilon


def problem_2(fname):
    with open(fname, "r") as f:
        lines = f.readlines()
        oxy = lines[:]
        co2 = lines[:]
        for i in range(len(lines[0]) - 1):
            oxy_char = most_freq_char(oxy, i)
            co2_char = "0" if most_freq_char(co2, i) == "1" else "1"
            if len(oxy) > 1:
                oxy = [x for x in oxy if x[i] == oxy_char]
            if len(co2) > 1:
                co2 = [x for x in co2 if x[i] == co2_char]
    return co2[0].strip(), oxy[0].strip()


def most_freq_char(strs, index):
    z, o = 0, 0
    for line in strs:
        o += int(line[index])
        z += abs(int(line[index]) - 1)

    return "1" if o >= z else "0"


def binary_product(vals):
    return functools.reduce(lambda a, b: int(a, 2) * int(b, 2), vals)


if __name__ == "__main__":
    print("Problem 1: {0}".format(binary_product(problem_1(sys.argv[1]))))
    print("Problem 2: {0}".format(binary_product(problem_2(sys.argv[1]))))
