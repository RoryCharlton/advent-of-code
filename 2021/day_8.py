#!/usr/bin/env python3
import sys


def problem_1(fname):
    
    with open(fname, "r") as f:
        uniques = 0
        for line in f.readlines():
            encoding, output = line.split(" | ")
            for digit in output.split():
                length = len(digit)
                if length in [2, 3, 4, 7]:
                    uniques += 1
    return uniques


def problem_2(fname):
    total = 0
    with open(fname, "r") as f:
        for line in f.readlines():
            encoder = {}
            encoding, output = line.split(" | ")
            encoding = encoding.strip().split()
            fives = [x for x in encoding if len(x) == 5]
            sixes = [x for x in encoding if len(x) == 6]
            encoder[1] = [x for x in encoding if len(x) == 2][0]
            encoder[4] = [x for x in encoding if len(x) == 4][0]
            encoder[7] = [x for x in encoding if len(x) == 3][0]
            encoder[8] = [x for x in encoding if len(x) == 7][0]
            encoder[9] = [x for x in sixes if chars_in(encoder[4], x)][0] # ick
            encoder[6] = [x for x in sixes if num_chars_in(encoder[1], x) == 1][0]
            encoder[3] = [x for x in fives if chars_in(encoder[1], x) == 1][0]
            encoder[5] = [x for x in fives if chars_in(x, encoder[6])][0]
            encoder[0] = [x for x in sixes if x not in [encoder[6], encoder[9]]][0]
            encoder[2] = [x for x in fives if x not in [encoder[3], encoder[5]]][0]

            keys = {"".join(sorted(v)): k for k, v in encoder.items()}
            entry = ""
            for digit in output.strip().split():
                entry += str(keys["".join(sorted(digit))])
            total += int(entry)

    return total
            

def chars_in(subset, superset):
    for char in subset:
        if char not in superset:
            return False
    return True


def num_chars_in(subset, superset):
    return len([x for x in subset if x in superset])


if __name__ == "__main__":
    print("Problem 1: {0}".format(problem_1(sys.argv[1])))
    print("Problem 2: {0}".format(problem_2(sys.argv[1])))
